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
#  {[**Author**]}      Ashien the Skyfox
#  {[**Version**]}     4.2.4
#  {[**Date**]}        2025-11-20
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
#   -v4.2.1: Collision Color chek update.
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
# Written by Ashien the Skyfox (https://github.com/Ashien-SkyFox)
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
        def __init__(self, map_data):
            # Tile size and spacing
            self.sizing_factor = conf.map_sizing_factor  # Sizing factor for the map tiles
            self.tile_spacing = int(((self.sizing_factor * screensize_x) / 2) + ((self.sizing_factor * screensize_y) / 2))  # Calculating tile spacing based on screen size
            self.tile_size = conf.map_tile_size  # Tile size based on sizing factor

            # Load tile images
            self.wall_tile = pygame.image.load('pictures/tiles/Basic_wall.png').convert_alpha() # Loading tile images
            self.start_point_tile = pygame.image.load('pictures/tiles/Start_point.png').convert_alpha() # Loading tile images
            self.finish_point_tile = pygame.image.load('pictures/tiles/Finisch_point.png').convert_alpha() # Loading tile images

            # Others
            self.tile_start_rect = self.start_point_tile.get_rect() # Getting the rectangle of the start point tile

            # Store map data
            self.map_data = map_data # Storing the map data
            self.width = len(map_data[0]) * self.tile_size[0] # Calculating the width of the map based on the number of columns and tile size
            self.height = len(map_data) * self.tile_size[1] # Calculating the height of the map based on the number of rows and tile size
            self.tile_group = pygame.sprite.Group() # Group to hold all tile sprites
            self.create_tiles() # Creating the tile sprites

            

            # Map location Variables
            self.location = vector(0, 0) # Top-left corner of the map
        
        def tile_type_to_image(self, tile_type):
            match tile_type: # Mapping tile types to images
                case 1:
                    return self.wall_tile # Basic wall tile
                case 2:
                    return self.start_point_tile # Start point tile
                case 3:
                    return self.finish_point_tile # Finish point tile
                case _:
                    return None # Empty tile
                    
        def create_tiles(self):
            # Creating tile sprites based on map data
            self.scaled_tile_images = []
            for row_index, row in enumerate(self.map_data): # Creating tile sprites based on map data
                scaled_row = []
                for col_index, tile_type in enumerate(row): # Iterating through each tile in the map
                    tile_image = self.tile_type_to_image(tile_type) # Getting the image for the current tile type
                    if tile_image:
                        scaled_image = pygame.transform.scale(tile_image, self.tile_size) # Scale once and store
                        scaled_row.append(scaled_image)
                    else:
                        scaled_row.append(None)
                self.scaled_tile_images.append(scaled_row)

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
            return self.get_sprite_group(ship_position) # Return the group of tile sprites for collision detection
        
        def get_sprite_group(self, ship_position):
            self.tile_group.empty() # Clear existing sprites
            offset_x = self.location.x
            offset_y = self.location.y
            for row_index, row in enumerate(self.scaled_tile_images):
                for col_index, tile_image in enumerate(row):
                    if tile_image:
                        x = col_index * self.tile_spacing + offset_x
                        y = row_index * self.tile_spacing + offset_y
                        """Create a sprite group for all tiles in the map. Useful for collision detection."""
                        tile_sprite = pygame.sprite.Sprite() # Create a new sprite (for the collision detection of the single tile)
                        tile_sprite.image = tile_image # Set the tile image
                        tile_sprite.rect = tile_sprite.image.get_rect(topleft=(x, y)) # Set the rectangle of the sprite
                        self.tile_group.add(tile_sprite) # Add the sprite to the group

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