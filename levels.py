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
#  {[**File**]}        levels.py
#  {[**Author**]}      Cutie Ashien
#  {[**Version**]}     5.1.2
#  {[**Date**]}        2026-04-29
#  {[**Python**]}      3.11.x
#  {[**License**]}     MIT
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Description**]}
#
#                 This module contains levels of Rocket.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Changelog**]}
#
#   - v5.1.2: Objective system update.
#       - Fixed minor bugs in the objective system.
#
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   - v5.1.1: Objective system update.
#       - Fixed minor bugs in the objective system.
#       - Improved objective tracking and display during gameplay.
#       - Enhanced level design to better integrate objectives.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   -v5.1.0: Objective system add.
#       - Added an objective system to the game, allowing for different objectives to be defined and tracked during gameplay.
#       - Implemented an Objective class to represent individual objectives and their states.
#       - Updated the game loop to check for objective completion and update the game state accordingly.
#       - Added functionality to display objective information on the screen during gameplay.
#       - Updated the level design to include specific objectives for each level.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v4.1.0: Fluid map selection update.
#       - added functions to retrieve level data dynamically.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#
#     - v4.0.0: Structure overhaul and level management update.
#       - Added Files: config.py, levels.py, helper/map.py, helper/ship.py, helper/main_menu.py
#       - Moved the tilemap to a separate config file (level.py).
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
import sys
from turtle import color # Import sys to modify the Python path


# Move to main directory and ensure parent directory is in sys.path
main_dir = os.path.join(os.path.dirname(__file__), '..')
os.chdir(main_dir)
if main_dir not in sys.path:
    sys.path.insert(0, main_dir)
"""
Coppied from ship.py caus why reinvent the wheel when you can just copy and paste :3
"""

# ------------------------------------------------------------------------------ #

### File Imports ###
import config as conf # Importing config module

# ------------------------------------------------------------------------------ #
objectives = conf.objective_kinds # Importing objective kinds from config for level objectives

# Function to retrieve level data

def grapp_level(number): # Retrieve a specific level by its number
    level_name = f'tilemap_level_{number}' # Construct level variable name
    return globals().get(level_name, None) # Return the level or None if not found

def get_level_info(): # Get a list of all level names
    i = 1
    level_names = {
    }
    objective_level = {
    }
    objective_duration_level = {
    }
    while True:
        level_name = f'tilemap_level_{i}' # Construct level variable name
        if level_name in globals(): # Check if level exists
            level_names[i] = f'Level {i}' # Add to dictionary
            objective_level_name = f'objective_level_{i}' # Construct objective variable name
            duration = f'objective_duration_level_{i}' # Construct duration variable name
            if objective_level_name in globals() and globals()[objective_level_name]: # Check if objective exists and is true
                try:
                    level_names[i] += f' (Objective: {objectives[globals()[objective_level_name]]})' # Add objective tag to level name
                    objective_level[i] = globals()[objective_level_name] # Add objective level to dictionary for later use in level loading
                    objective_duration_level[i] = globals()[duration] # Add duration to dictionary for later use in level loading
                    if objective_duration_level[i] is not False and objective_duration_level[i] is not None: # Check if duration is valid
                        level_names[i] += f' (Duration: {objective_duration_level[i]}s)' # Add duration tag to level name
                except KeyError:
                    level_names[i] += ' (Objective: Unknown)' # Add level with unknown objective if objective kind is not found
                    objective_level[i] = False # Keep this level selectable even if objective metadata is invalid
                    objective_duration_level[i] = False # Set objective duration to false for later use in level loading
                    print(f"Objective {globals()[objective_level_name]} not found in objectives dictionary. Please check Level {i}") # Print error if objective kind is not found
                except Exception as e:
                    level_names[i] += ' (Objective: Error)' # Add level with error in objective
                    objective_level[i] = -1 # Set objective level to -1 for later use in level loading
                    objective_duration_level[i] = None # Set objective duration to false for later use in level loading
                    print(f"Error retrieving objective for level {i}: {e}") # Print error if there is an issue retrieving the objective
            elif objective_level_name in globals() and not globals()[objective_level_name]: # Check if objective exists and is false
                level_names[i] += ' (No Objective)' # Add no objective tag to level name
                objective_level[i] = False # Set objective level to false for later use in level loading
                objective_duration_level[i] = False # Set objective duration to false for later use in level loading
            i += 1 # Increment level number for next iteration
        else:
            break
    mapdata = [level_names, objective_level, objective_duration_level] # Combine level names, objective levels and objective durations into a single list for return
    return mapdata # Return the map data list
# ----------------------------------------------------------------------------- #

#######################################################################################
#######################################################################################
# Create tilemap for easy level design
# List: 0 = empty, 1 = Basic_wall, 2 = Start_point, 3 = Finish_point, 4 = Objective_point
#
# objective: let it be false if there is no objective, otherwise
# 1 = flyby, 2 = stay
#
# duration: only nessesary for objectives with a duration, like stay
# duration in seconds, default is 3.0 seconds
#######################################################################################
#######################################################################################

# ----------------------------------------------------------------------------- #
    
# Map1
objective_level_1 = 1
objective_duration_level_1 = False
tilemap_level_1 = [
    [0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# ----------------------------------------------------------------------------- #

# Map2
objective_level_2 = 2
objective_duration_level_2 = 4
tilemap_level_2 = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# ----------------------------------------------------------------------------- #

# Map3
objective_level_3 = 3
objective_duration_level_3 = False
tilemap_level_3 = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# ----------------------------------------------------------------------------- #

# Map4
objective_level_4 = False
objective_duration_level_4 = False
tilemap_level_4 = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# ----------------------------------------------------------------------------- #
