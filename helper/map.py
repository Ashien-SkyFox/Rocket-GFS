##################################################################################################################################################################################################################
# ================================================================================================================================================================================================================
#   ██████╗ ██╗   ██╗      █████╗ ███████╗██╗  ██╗██╗███████╗███╗   ██╗
#   ██╔══██╗╚██╗ ██╔╝     ██╔══██╗██╔════╝██║  ██║██║██╔════╝████╗  ██║
#   ██████╔╝ ╚████╔╝      ███████║███████╗███████║██║█████╗  ██╔██╗ ██║
#   ██╔══██╗  ╚██╔╝       ██╔══██║╚════██║██╔══██║██║██╔══╝  ██║╚██╗██║
#   ██████╔╝   ██║        ██║  ██║███████║██║  ██║██║███████╗██║ ╚████║
#   ╚═════╝    ╚═╝        ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝
# ================================================================================================================================================================================================================
#  {[**Project**]}     Rocket
#  {[**File**]}        map.py
#  {[**Author**]}      Cutie Ashien
#  {[**Version**]}     7.0.0
#  {[**Date**]}        2026-07-15
#  {[**Python**]}      3.11.x
#  {[**License**]}     MIT
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Description**]}
#
#                  This module contains the map-related functionalities of Rocket, like map rendering and tile management.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Changelog**]}
#
#  -v7.0.0: Mini map
#       - Added a mini map to the game that shows the ship's position and orientation relative to the level.
#       - The mini map is displayed in the top-right corner of the screen and updates in
#
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#  -v6.0.0: Full release of the game with all features and levels.
#      - Added multiple levels with increasing difficulty and unique objectives.
#      - Implemented a highscore system to track player performance across levels.
#      - Added a main menu with level selection and highscore display.
#      - Improved graphics and visual effects for a more immersive experience.
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   - v5.1.3: Objective system update.
#       - Half rework of objective system
#      - Fixed crash on load level with no or broken objective
#
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   - v5.1.1: Objective system update.
#       - Fixed minor bugs in the objective system.
#       - Improved objective tracking and display during gameplay.
#       - Enhanced level design to better integrate objectives.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   - v5.1.0: Objective system add.
#       - Added an objective system to the game, allowing for different objectives to be defined and tracked during gameplay.
#       - Implemented an Objective class to represent individual objectives and their states.
#       - Updated the game loop to check for objective completion and update the game state accordingly.
#       - Added functionality to display objective information on the screen during gameplay.
#       - Updated the level design to include specific objectives for each level.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   - v5.0.1: Collision End check and start of refactoring.
#       - Checks if player is at the endpoint and ending the game.
#       - Refactored the collision code to be easier to read and maintain.
#       - Reused cached masks for the ship and tiles to reduce collision overhead.
#       - Limited start and finish color checks to the actual overlap area for better performance.
#       - Restored color-based safe and unsafe landing zones on the start and finish tiles.
#       - Reset the finish countdown correctly when leaving the finish tile.
#       - Added comments to document the optimized collision path.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   - v4.2.1: Collision Color chek update.
#       - Added ability to chek the overlapping pixel for collor
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   - v4.2.0: Collision update.
#       - Implemented collision detection and handling in the ship movement logic.
#       - Added game state management for running and game over states.
#       - Added funtionality to reset the ship and main menu after game over.
#       - Added logic to set the game stat to game over if the collison is not on the top of a block.
#       - Added an reset funktion to the main menu instance to reset it after game over.
#       - Added config valibals for collision locktime, collision fall off and upward movement on collision.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
#     - v4.1.1: Minor bug fixes and improvements.
#       - Fixed minor bugs related to level selection functions.
#       - Improved code readability and maintainability.
#       - Fixed bug that the Ship wouldn't spawn at the center start point in certain situations.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v4.0.4: Structure overhaul(map).
#       - Moved the map class to a separate file (map.py).
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v4.0.0: Structure overhaul and level management update.
#       - Added Files: config.py, levels.py, helper/map.py, helper/ship.py, helper/main_menu.py
#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The code is clearly labeled using comments so you can
# easily navigate through it and understand its structure and functionality.
# Enjoy coding! :3
# ================================================================================================================================================================================================================
# Written by Cutie Ashien (https://github.com/Ashien-SkyFox)
##################################################################################################################################################################################################################

### Import Operating System Module (nessesary to load files)###
import os # Importing the os library for file path operations
import sys # Import sys to modify the Python path


# Move to main directory and ensure parent directory is in sys.path
main_dir = os.path.join(os.path.dirname(__file__), '..')
os.chdir(main_dir)
if main_dir not in sys.path:
    sys.path.insert(0, main_dir)
"""
    Luckly it was just copy paste this time (out of ship.py) :3
    I still want to give up on python packaging sometimes tho :/
"""

# ------------------------------------------------------------------------------ #

### File Imports ###
import levels as levels # Importing levels module
import config as conf # Importing config module
import helper.main_menu as mm # Importing map helper module
import helper.objectives as objectives_helper # Importing objective helper module

# ------------------------------------------------------------------------------ #

### Library Imports ###
import pygame # Importing the pygame library for game development

# ------------------------------------------------------------------------------ #

### Config Imports ###
vector = conf.vector # Importing vector from config module
screensize_x = conf.screensize_x # Importing screen size x from config module
screensize_y = conf.screensize_y # Importing screen size y from config module

### TileMap Class ###
class TileMap:
        def __init__(self, map_data, map_i):
            self.duration_data = map_data[2].get(map_i, False)
            # Tile size and spacing
            self.sizing_factor = conf.map_sizing_factor  # Sizing factor for the map tiles
            self.tile_spacing = int(((self.sizing_factor * screensize_x) / 2) + ((self.sizing_factor * screensize_y) / 2))  # Calculating tile spacing based on screen size
            self.tile_size = conf.map_tile_size  # Tile size based on sizing factor

            # Load tile images
            self.wall_tile = pygame.image.load(conf.wall_tile).convert_alpha() # Loading tile images
            self.start_point_tile = pygame.image.load(conf.start_point_tile).convert_alpha() # Loading tile images
            self.finish_point_tile = pygame.image.load(conf.finish_point_tile).convert_alpha() # Loading tile images
            self.objective_tile = None
            self.objective = None
            objective_data = map_data[1].get(map_i, False)
            self.objective_definition = objectives_helper.get_objective_definition(objective_data)
            if self.objective_definition is not None:
                try:
                    self.objective_tile = pygame.image.load(self.objective_definition["tile_path"]).convert_alpha() # Loading tile image from objectives.py metadata
                    self.objective = self.objective_definition["type"]
                except (KeyError, FileNotFoundError, TypeError, pygame.error):
                    self.objective_definition = None
                    self.objective_tile = None
                    self.objective = None
            # Others
            self.tile_start_rect = self.start_point_tile.get_rect() # Getting the rectangle of the start point tile

            # Store map data
            self.map_data = levels.grapp_level(map_i) # Getting the map data for the selected map
            self.width = len(self.map_data[0]) * self.tile_size[0] # Calculating the width of the map based on the number of columns and tile size
            self.height = len(self.map_data) * self.tile_size[1] # Calculating the height of the map based on the number of rows and tile size
            self.map_columns = len(self.map_data[0]) if self.map_data else 0
            self.map_rows = len(self.map_data)
            self.world_width = max(1, (self.map_columns - 1) * self.tile_spacing + self.tile_size[0])
            self.world_height = max(1, (self.map_rows - 1) * self.tile_spacing + self.tile_size[1])
            self.tile_group = pygame.sprite.Group() # Group to hold all tile sprites
            self.objective_instance = None
            self.objective_world_position = None
            self.finish_world_position = None
            self.create_tiles() # Creating the tile sprites

            

            # Map location Variables
            self.location = vector(0, 0) # Top-left corner of the map

        def has_active_objective(self):
            return self.objective_instance is not None and not isinstance(self.objective_instance, objectives_helper.NoneObjective)
        
        def tile_type_to_image(self, tile_type):
            match tile_type: # Mapping tile types to images
                case 1:
                    return self.wall_tile # Basic wall tile
                case 2:
                    return self.start_point_tile # Start point tile
                case 3:
                    return self.finish_point_tile # Finish point tile
                case 4:
                    if self.objective_tile is not None:
                        return self.objective_tile # Objective tile
                    else:
                        return None # No tile if objective tile is not set
                case _:
                    return None # Empty tile
                    
        def create_tiles(self):
            # Creating tile sprites based on map data
            self.scaled_tile_images = []
            self.tile_sprites = []
            for row_index, row in enumerate(self.map_data): # Creating tile sprites based on map data
                scaled_row = []
                for col_index, tile_type in enumerate(row): # Iterating through each tile in the map
                    tile_image = self.tile_type_to_image(tile_type) # Getting the image for the current tile type
                    if tile_image:
                        scaled_image = pygame.transform.scale(tile_image, self.tile_size) # Scale once and store
                        scaled_row.append(scaled_image)
                        tile_sprite = pygame.sprite.Sprite() # Creating a sprite for the tile
                        tile_sprite.image = scaled_image # Assigning the scaled image to the sprite
                        tile_sprite.mask = pygame.mask.from_surface(scaled_image) # Creating a mask for pixel-perfect collision detection
                        tile_sprite.tile_type = tile_type # Storing the tile type in the sprite for later use
                        tile_sprite.grid_x = col_index * self.tile_spacing # Calculating the grid x position of the tile
                        tile_sprite.grid_y = row_index * self.tile_spacing # Calculating the grid y position of the tile
                        tile_sprite.rect = tile_sprite.image.get_rect(topleft=(tile_sprite.grid_x, tile_sprite.grid_y)) # Setting the rectangle of the sprite based on its grid position
                        if tile_type == 3:
                            self.finish_world_position = vector(
                                tile_sprite.grid_x + (self.tile_size[0] / 2),
                                tile_sprite.grid_y + (self.tile_size[1] / 2)
                            )
                        if tile_type == 4 and self.objective_definition is not None:
                            if self.objective_instance is None:
                                self.objective_instance = objectives_helper.create_objective(
                                    self.objective_definition["type"],
                                    (tile_sprite.grid_x, tile_sprite.grid_y),
                                    self.tile_size,
                                    self.duration_data
                                )
                            else:
                                self.objective_instance.size = self.tile_size
                                self.objective_instance.set_position((tile_sprite.grid_x, tile_sprite.grid_y))
                                self.objective_instance.rect.size = self.tile_size

                            if self.has_active_objective():
                                self.objective_world_position = vector(
                                    tile_sprite.grid_x + (self.tile_size[0] / 2),
                                    tile_sprite.grid_y + (self.tile_size[1] / 2)
                                )
                        self.tile_sprites.append(tile_sprite) # Adding the tile sprite to the list of tile sprites
                    else:
                        scaled_row.append(None)
                self.scaled_tile_images.append(scaled_row)

            self.tile_group = pygame.sprite.Group(self.tile_sprites) # Creating a sprite group for all tile sprites for easy rendering and collision detection

        def draw_map(self, screen, ship_position):
            self.location.x = -ship_position.x + (0.5 * screensize_x)
            self.location.y = -ship_position.y + (0.5 * screensize_y)
            offset_x = self.location.x
            offset_y = self.location.y
            for row_index, row in enumerate(self.scaled_tile_images):
                for col_index, tile_image in enumerate(row):
                    if tile_image:
                        x = col_index * self.tile_spacing + offset_x
                        y = row_index * self.tile_spacing + offset_y
                        screen.blit(tile_image, (x, y))
                        """Create a sprite group for all tiles in the map. Useful for collision detection."""
            self.draw_minimap(screen, ship_position)
            return self.get_sprite_group(ship_position) # Return the group of tile sprites for collision detection

        def draw_minimap(self, screen, ship_position):
            if screen is None or self.map_columns == 0 or self.map_rows == 0:
                return

            # Fit the full world into the available minimap area while preserving aspect ratio.
            max_minimap_width = max(conf.minimap_min_size, int(screensize_x * conf.minimap_max_width_ratio)) # Calculating the maximum width of the minimap based on screen size and configuration
            max_minimap_height = max(conf.minimap_min_size, int(screensize_y * conf.minimap_max_height_ratio)) # Calculating the maximum height of the minimap based on screen size and configuration
            scale = min(max_minimap_width / self.world_width, max_minimap_height / self.world_height) # Calculating the scale factor to fit the world into the minimap area while preserving aspect ratio
            minimap_width = max(1, int(self.world_width * scale)) # Calculating the width of the minimap based on the world width and scale factor
            minimap_height = max(1, int(self.world_height * scale)) # Calculating the height of the minimap based on the world height and scale factor

            frame_width = minimap_width + (conf.minimap_padding * 2) # Calculating the width of the minimap frame including padding
            frame_height = minimap_height + (conf.minimap_padding * 2) # Calculating the height of the minimap frame including padding
            frame_x = screensize_x - frame_width - conf.minimap_margin # Calculating the x position of the minimap frame based on screen size and margin
            frame_y = conf.minimap_margin # Calculating the y position of the minimap frame based on margin

            # Draw the minimap background and border on a separate alpha surface.
            minimap_surface = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA) # Creating a new surface for the minimap with alpha transparency
            """
            SRCALPHA flag is used to create a surface that supports per-pixel alpha transparency. This allows us to draw the minimap with a transparent background and only show the tiles and ship marker.
            """
            # Draw the minimap background
            pygame.draw.rect(
                minimap_surface,
                conf.minimap_background,
                minimap_surface.get_rect(),
                border_radius=conf.minimap_border_radius,
            )
            # Draw the minimap border
            pygame.draw.rect(
                minimap_surface,
                conf.minimap_border_color,
                minimap_surface.get_rect(),
                width=2,
                border_radius=conf.minimap_border_radius,
            )

            # Draw each tile on the minimap based on its type and position.
            for row_index, row in enumerate(self.map_data):
                for col_index, tile_type in enumerate(row):
                    if tile_type == 0:
                        continue
                    if tile_type == 4 and not self.has_active_objective():
                        continue

                    # Round the projected tile edges instead of x/size separately so touching
                    # world tiles stay flush on the minimap after scaling.
                    tile_color = conf.minimap_tile_colors.get(tile_type, (255, 255, 255))
                    tile_left = conf.minimap_padding + round(col_index * self.tile_spacing * scale)
                    tile_top = conf.minimap_padding + round(row_index * self.tile_spacing * scale)
                    tile_right = conf.minimap_padding + round((col_index * self.tile_spacing + self.tile_size[0]) * scale)
                    tile_bottom = conf.minimap_padding + round((row_index * self.tile_spacing + self.tile_size[1]) * scale)
                    tile_width = max(1, tile_right - tile_left)
                    tile_height = max(1, tile_bottom - tile_top)
                    pygame.draw.rect(
                        minimap_surface,
                        tile_color,
                        pygame.Rect(tile_left, tile_top, tile_width, tile_height),
                        border_radius=1,
                    )

            # Clamp the ship marker so it stays inside the minimap frame at all times.
            ship_marker_x = conf.minimap_padding + int(ship_position.x * scale)
            ship_marker_y = conf.minimap_padding + int(ship_position.y * scale)
            ship_marker_x = max(conf.minimap_padding, min(conf.minimap_padding + minimap_width, ship_marker_x))
            ship_marker_y = max(conf.minimap_padding, min(conf.minimap_padding + minimap_height, ship_marker_y))

            pygame.draw.circle(
                minimap_surface,
                conf.minimap_ship_color,
                (ship_marker_x, ship_marker_y),
                max(3, int(4 * scale) + 2),
            )

            screen.blit(minimap_surface, (frame_x, frame_y)) # Blitting the minimap surface onto the main screen at the calculated position
        
        def get_sprite_group(self, ship_position):
            offset_x = self.location.x
            offset_y = self.location.y
            for tile_sprite in self.tile_sprites:
                tile_sprite.rect.topleft = (tile_sprite.grid_x + offset_x, tile_sprite.grid_y + offset_y)
                if tile_sprite.tile_type == 4 and self.objective_instance is not None:
                    self.objective_instance.set_position(tile_sprite.rect.topleft)

            return self.tile_group # Return the group of tile sprites for collision detection

        def get_type_of_tile_at_position(self, position):
            pass
        
        def get_location_of_spawn_point(self, ship_rect):
            for row_index, row in enumerate(self.map_data):
                for col_index, tile_type in enumerate(row):
                    if tile_type == 2: # Start point tile
                        x = col_index * self.tile_size[0] + ((ship_rect.width * 2 - ship_rect.width / 2) * (self.sizing_factor / 0.3))
                        y = row_index * self.tile_size[1] - (((ship_rect.height * 2 - ship_rect.height / 2) * (self.sizing_factor / 0.3)) * 0.5) 
                        return vector(x, y)
            return vector(0, 0) # Default to (0, 0) if no start point found

        def get_navigation_target_position(self):
            if self.objective_instance is not None and not self.objective_instance.complete and self.objective_world_position is not None:
                return self.objective_world_position
            return self.finish_world_position

        def update_screen_size(self, new_width, new_height):
            global screensize_x, screensize_y
            screensize_x = int(new_width)
            screensize_y = int(new_height)

            self.tile_spacing = int(((self.sizing_factor * screensize_x) / 2) + ((self.sizing_factor * screensize_y) / 2))
            self.tile_size = conf.map_tile_size
            self.world_width = max(1, (self.map_columns - 1) * self.tile_spacing + self.tile_size[0])
            self.world_height = max(1, (self.map_rows - 1) * self.tile_spacing + self.tile_size[1])
            self.create_tiles()