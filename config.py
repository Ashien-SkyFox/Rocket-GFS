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
#  {[**File**]}        config.py
#  {[**Author**]}      Cutie Ashien
#  {[**Version**]}     6.1.0
#  {[**Date**]}        2026-07-01
#  {[**Python**]}      3.11.x
#  {[**License**]}     MIT
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Description**]}
#
#                  This module contains configuration settings and constants for Rocket.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Changelog**]}
#
#  -v6.1.0: Thruster effects raw.
#      - Added configuration offsets for the five thruster nozzle positions.
#      - Added/kept key mapping and ratio settings used by the raw thruster flame effects.
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#  -v6.0.0: Full release of the game with all features and levels.
#      - Added multiple levels with increasing difficulty and unique objectives.
#      - Implemented a highscore system to track player performance across levels.
#      - Added a main menu with level selection and highscore display.
#      - Improved graphics and visual effects for a more immersive experience.
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#  - v5.1.3: Objective system update.
#      - Half rework of objective system
#
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
#     - v4.0.1: Structure overhaul(config).
#       - Moved the config values to a separate config file (config.py).
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

### Library Imports ###
import pygame

# setting some necessary variables
vector = pygame.math.Vector2


# Debug settings
debug_mode = True

# screen size
pygame.display.init()
display_info = pygame.display.Info()
screensize_x = int(display_info.current_w * 0.75)
screensize_y = int(display_info.current_h * 0.75)
"""
Problems: If you would want to change the screen size you would have to change it in multiple places or else the pictures would not be in the right place
Fixed: I created variables for the screen size and used them in the code with multiplications
"""

##########################################################
##########################################################

# Ship settings
##### Ajustable Favtors #####
# Trustor key bindings
ship_thruster_key_outer_left = pygame.K_g
ship_thruster_key_inner_left = pygame.K_h
ship_thruster_key_middle = pygame.K_j
ship_thruster_key_inner_right = pygame.K_k
ship_thruster_key_outer_right = pygame.K_l

# Thruster ratios
ship_inner_thruster_ratio = 0.4
ship_outer_thruster_ratio = 0.8
ship_middle_thruster_ratio = 0.8
ship_turn_outer_factor = 0.7
ship_turn_inner_factor = 0.7

# Gravity settings
ship_gravity = vector(0, 1.8)  # Gravity vector affecting the ship

# Ship physics
ship_acceleration = 0.2
ship_rotate_friction = 0.95

# Collision Variables
ship_collision_locktime = 5
ship_collision_move_upward = 0.01
ship_rotate_angle_collision = 45
ship_rotate_to_ground_speed = 3
ship_speedx_fade_fast_rate = 0.65

# color checks
unsafe_color = (255, 12, 0, 255) # red as unsave for walls
start_point_color = (0, 255, 233, 255) # start point color representing the start point in the map
end_point_color = (255, 0, 229, 255) # end point color representing the end point in the map
objective_stay_color = (255, 140, 0, 255) # yellow color representing the stay objective
objective_flyby_color = (8, 255, 0, 255) # green color representing the flyby objective
objective_colors = [objective_stay_color, objective_flyby_color]
valid_collision_colors = [unsafe_color, start_point_color, end_point_color] + objective_colors

##########################################################
##########################################################

map_sizing_factor = 0.3  # Sizing factor for the map tiles
map_tile_size = (int((map_sizing_factor * screensize_x) + (map_sizing_factor * screensize_y)) / 2, int((map_sizing_factor * screensize_x) + (map_sizing_factor * screensize_y)) / 2) # Calculating the tile size based on screen size and sizing factor

# -------------------------------------------------------------- #
# Objective related
# -------------------------------------------------------------- #
# Objective kinds and allocated numbers for map creation
objective_kinds = {
    1: {
        'type': 'flyby',
        'tile_path': r'pictures\tiles\Flyby - frontend.png'
    },
    2: {
        'type': 'stay',
        'duration': 3.0, # Default duration for stay objective
        'tile_path': r'pictures\tiles\Stay - frontend.png'
    }
}

# Pngs for all
wall_tile = r'pictures/tiles/Basic_wall.png' # Loading tile images
start_point_tile = r'pictures/tiles/Start_point.png' # Loading tile images
finish_point_tile = r'pictures/tiles/Finisch_point.png' # Loading tile images
rocket_ship = r'pictures/Rocket - frontend.png' # Loading tile images
star_glitter_background = r'pictures/Star_glitter.png' # Moving background texture

# Background motion (pixels per second)
background_scroll_speed_x = 24
background_scroll_speed_y = 8
background_parallax_factor = 0.2
background_star_scale = 0.35
background_star_alpha_min = 25
background_star_alpha_max = 110

# Thrusters
# Thrusterlayout ofseet
left_thruster_offset = vector(-0.35, 0.5)
left_middle_thruster_offset = vector(-0.15, 0.5)
middle_thruster_offset = vector(0, 0.5)
right_middle_thruster_offset = vector(0.15, 0.5)
right_thruster_offset = vector(0.35, 0.5)