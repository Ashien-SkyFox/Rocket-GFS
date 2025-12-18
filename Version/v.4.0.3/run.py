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
#  {[**File**]}        run.py
#  {[**Author**]}      Ashien the Skyfox
#  {[**Version**]}     4.0.3
#  {[**Date**]}        2025-11-07
#  {[**Python**]}      3.11.x
#  {[**License**]}     MIT
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Description**]}
#
#      The code is a pygame-based simulation of a rocket coup ship.
#      You have five thrusters that you can control using the G, H, J, K, and L keys to rotate the ship and move it forward.
#      The ship's rotation is influenced by thruster inputs, with fade and speedup factors to simulate somwhat realistic movement.
#      The ship is rendered at the center of the screen, and the game runs at 60 frames per second.
#      The code is structured to allow easy adjustments of thruster ratios and movement factors.
#      Debugging information can be printed to the console to monitor the ship's state.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Purpose**]}
#
#      The Project is an educational project to learn more about programming and game development.
#      The purpose of this code is to create a simple simulation of a rocket ship that can be controlled using keyboard inputs.
#      The code is designed to be modular and easy to understand, allowing for future enhancements and modifications or also for educational purposes.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Changelog**]}
#
#     - v4.0.3: Structure overhaul(ship).
#       - Moved the ship class to a separate file (ship.py).
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v4.0.2: Structure overhaul(main menu).
#       - Moved the main menu class to a separate file (main_menu.py).
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v4.0.1: Structure overhaul(config).
#       - Moved the config values to a separate config file (config.py).
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v4.0.0: Structure overhaul and level management update.
#       - Added Files: config.py, levels.py, helper/map.py, helper/ship.py, helper/main_menu.py
#       - Moved the tilemap to a separate level file (level.py).
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v3.1.0: Main menu and level selection update.
#       - Added a main menu with level selection functionality.
#       - Implemented a loading animation when switching levels.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v3.0.2: Center ship start adjustment.
#       - Adjusted the calculation of center_ship_start for better alignment-
#       - Added contability with different tile sizes.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v3.0.1: Tilemap spacing and sizing & Gravity update.
#       - Adjusted tile spacing and sizing based on screen size for better visual consistency.
#       - Added gravity variable to the Ship class for easier adjustment.
#       - Added gravity effect to the ship's movement for more realistic physics.
#       - Improved overall code structure and readability.
#       - Fixed minor bugs related to ship movement and rendering.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v3.0.0: Map and movment update.
#       - Added a tilemap system for level design.
#       - Implemented map movement based on ship position.
#       - Adjusted tile size based on screen size.
#       - Improved overall code structure and readability.
#       - Fixed minor bugs related to ship movement and rendering.
#       - Added levle selection functionality.
#       - Updated debug function to include new variables.
#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v2.1.0: Minor overhaul to ship rotation logic.
#       - Simplified rotation velocity calculation.
#       - Removed unnecessary variables related to rotation fade and speedup.
#       - Improved code readability by removing redundant comments.
#       - Updated debug function to include new variables.
#       - Fixed minor rotation buggs.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v2.0.0: Major overhaul of the code structure and functionality.
#       - Improved thruster input handling and ship rotation logic.
#       - Added adjustable factors for thruster ratios and movement dynamics.
#       - Enhanced code readability and maintainability.
#       - Fixed image loading path issue.
#       - Added comments and documentation for clarity.
#       - Added class structure for better organization.
#       - Major overhaul of the debug functionality.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v1.0.0: Initial release of the rocket ship simulation.
#       - Basic thruster controls and ship rotation implemented.
#       - Simple rendering of the ship at the center of the screen.
#       - Basic game loop with event handling and frame rate control.
#       - Initial debugging functionality added.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  ⚙️  Notes:
#
#      - required assets in the 'Pictures' folder.
#      - Requires pygame >= 2.5.0
#      - Run `main.py` to start the game
#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  ⚙️  Side notes:
#
#      - This code was created as part of an educational project at the GWS Bühl.
#      - The code originally was written in 2025 and has been updated and improved over time.
#      - The code is open-source and available on GitHub for educational purposes.
#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The code is clearly labeled using comments so you can
# easily navigate through it and understand its structure and functionality.
# Enjoy coding! :3
# ================================================================================================================================================================================================================
# Written by Ashien the Skyfox (https://github.com/Ashien-SkyFox)
##################################################################################################################################################################################################################

### File Imports ###
import levels as levels # Importing levels module
import config as conf # Importing config module
import helper.main_menu as mm # Importing map helper module
import helper.ship as sh # Importing ship helper module

# ------------------------------------------------------------------------------ #

### Library Imports ###
from unittest import case # For match case statements
import pygame # Importing the pygame library for game development
import os # Importing the os library for file path operations
import time # Importing the time library for time-related functions
import math # Importing the math library for mathematical functions

# ------------------------------------------------------------------------------ #

### json Imports ###
# Placeholder for future json imports for highscore system

# ------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------ #

highscore = 0 #placeholder for highscore system

## ------------------------------------------------------------------------------ #

screensize_x = conf.screensize_x
screensize_y = conf.screensize_y
vector = conf.vector


def game_loop():
    pygame.display.set_caption("Rocket - v4.0.0") # Setting the window title
    pygame.init()

    map_selected = 0
    vector = pygame.math.Vector2

    screen = pygame.display.set_mode((screensize_x, screensize_y)) # set the screen size

    clock = pygame.time.Clock() # Creating a clock object to manage the frame rate

    
    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #  

    class TileMap:
        def __init__(self, map_data):
            # Tile size and spacing
            self.sizing_factor = 0.3 # Used for tile size calculation
            self.tile_spacing = int(((self.sizing_factor * screensize_x) / 2) + ((self.sizing_factor * screensize_y) / 2))  # Calculating tile spacing based on screen size
            self.tile_size = (int((self.sizing_factor * screensize_x) + (self.sizing_factor * screensize_y)) / 2, int((self.sizing_factor * screensize_x) + (self.sizing_factor * screensize_y)) / 2) # Calculating the tile size based on screen size

            # Load tile images
            self.wall_tile = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pictures', 'tiles', 'Basic_wall.png')).convert_alpha() # Loading tile images
            self.start_point_tile = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pictures', 'tiles', 'Start_point.png')).convert_alpha() # Loading tile images
            self.finish_point_tile = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pictures', 'tiles', 'Finisch_point.png')).convert_alpha() # Loading tile images

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

        def get_location_of_spawn_point(self, ship_rect):
            for row_index, row in enumerate(self.map_data):
                for col_index, tile_type in enumerate(row):
                    if tile_type == 2: # Start point tile
                        x = col_index * self.tile_size[0] + (50 / (0.2 / self.sizing_factor)) + (ship_rect.width / (0.3 / self.sizing_factor))
                        y = row_index * self.tile_size[1]
                        return vector(x, y)
            return vector(0, 0) # Default to (0, 0) if no start point found

    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #

    main_menu_instance = mm.main_menu(map_selected, highscore)
    ship_instance = sh.Ship()
    ship_orginal = ship_instance.create_ship_image()
    running = True
    def start_game_loop(running=running, map_selected=map_selected):
        while running:
            for event in pygame.event.get(): # Quiting the game loop if the window is closed
                if event.type == pygame.QUIT: 
                    running = False 

            # -------------------------------------------------------------------------------- #

            screen.fill((0, 0, 0)) # Filling the screen with black color to clear previous frame

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #
            if map_selected == 0:
                map = main_menu_instance.main_menu_loop(screen) # Displaying the main menu
                if map in [1, 2]: # If a map is selected

                    main_menu_instance.map_loading_animation(screen) # Displaying the map loading animation
                    map_instance = TileMap(levels.grapp_level(map)) # Creating a tilemap instance based on the selected map
                    ship, ship_rect = ship_instance.get_rect()
                    spawn_position = map_instance.get_location_of_spawn_point(ship_rect) # Getting the spawn position from the tilemap
                    ship_instance.position = spawn_position # Setting the ship position to the spawn position
                    map_instance.tile_group.draw(screen) # Drawing the tilemap on the screen
                    map_selected = -1 # Setting the value to -1 to indicate that a map has been selected

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #

            if map_selected == -1:
                ship_instance.update_thruster_inputs() # Update thruster inputs based on key presses
                ship_instance.ship_rotate() # Update ship movement based on thruster inputs
                ship_instance.move_ship() # Move the ship based on current velocity and acceleration
                position = ship_instance.get_ship_position() # Getting the ship position for map movement
                map_instance.draw_map(screen, position) # Drawing the map on the screen
                ship_instance.render_ship_maps() # Render the ship with updated rotation
                ship, ship_rect = ship_instance.get_rect() # Getting the ship image and rect for rendering
                ship_instance.debug() # Starting the debug
                screen.blit(ship, ship_rect) # Drawing the ship on the screen at the center position

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #
            
            pygame.display.flip() # Updating the display to show the new frame
            clock.tick(60) # Limiting the frame rate to 60 FPS

    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #

    start_game_loop()
    pygame.quit()

game_loop()
"""
Starting the game loop
"""