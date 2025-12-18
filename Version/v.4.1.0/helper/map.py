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
#  {[**Version**]}     4.1.0
#  {[**Date**]}        2025-11-07
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
            self.sizing_factor = 0.3 # Used for tile size calculation
            self.tile_spacing = int(((self.sizing_factor * screensize_x) / 2) + ((self.sizing_factor * screensize_y) / 2))  # Calculating tile spacing based on screen size
            self.tile_size = (int((self.sizing_factor * screensize_x) + (self.sizing_factor * screensize_y)) / 2, int((self.sizing_factor * screensize_x) + (self.sizing_factor * screensize_y)) / 2) # Calculating the tile size based on screen size

            # Load tile images
            self.wall_tile = pygame.image.load('pictures/tiles/Basic_wall.png').convert_alpha() # Loading tile images
            self.start_point_tile = pygame.image.load('pictures/tiles/Start_point.png').convert_alpha() # Loading tile images
            self.finish_point_tile = pygame.image.load('pictures/tiles/Finisch_point.png').convert_alpha() # Loading tile images

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