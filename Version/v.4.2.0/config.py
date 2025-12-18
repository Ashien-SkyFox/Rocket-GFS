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
#  {[**Author**]}      Ashien the Skyfox
#  {[**Version**]}     4.2.0
#  {[**Date**]}        2025-11-18
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
# Written by Ashien the Skyfox (https://github.com/Ashien-SkyFox)
##################################################################################################################################################################################################################

### Library Imports ###
import pygame

# setting some necessary variables
vector = pygame.math.Vector2

# screen size

screensize_x = 1200
screensize_y = 700
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

# Collision locktime
ship_collision_locktime = 10

##########################################################
##########################################################

map_sizing_factor = 0.3  # Sizing factor for the map tiles
map_tile_size = (int((map_sizing_factor * screensize_x) + (map_sizing_factor * screensize_y)) / 2, int((map_sizing_factor * screensize_x) + (map_sizing_factor * screensize_y)) / 2) # Calculating the tile size based on screen size and sizing factor