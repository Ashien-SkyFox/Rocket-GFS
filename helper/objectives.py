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
#  {[**File**]}        objectives.py
#  {[**Author**]}      Cutie Ashien
#  {[**Version**]}     5.1.0
#  {[**Date**]}        2025-11-22
#  {[**Python**]}      3.11.x
#  {[**License**]}     MIT
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Description**]}
#
#                  Objective system for Rocket. Defines the Objective class and related functionality.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Changelog**]}
#
#   -v5.1.0: Objective system add.
#       - Added an objective system to the game, allowing for different objectives to be defined and tracked during gameplay.
#       - Implemented an Objective class to represent individual objectives and their states.
#       - Updated the game loop to check for objective completion and update the game state accordingly.
#       - Added functionality to display objective information on the screen during gameplay.
#       - Updated the level design to include specific objectives for each level.
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


# Move to main directory and ensure parent directory is in sys.path
main_dir = os.path.join(os.path.dirname(__file__), '..')
os.chdir(main_dir)
if main_dir not in sys.path:
    sys.path.insert(0, main_dir)

# ------------------------------------------------------------------------------ #

### File Imports ###
import config as conf # Importing config module

# ------------------------------------------------------------------------------ #

### Library Imports ###
import pygame # Importing the pygame library for game development
import math # Importing the math library for mathematical functions

# ------------------------------------------------------------------------------ #

class Objective:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.complete = False
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

    def set_position(self, position):
        self.rect.topleft = position

    def update(self):
        return "Parrent", "not relevant"
    
    def main_work(self):
        if self.complete:
            return "Completed you can move on", "not relevant"
        else:
            return self.update()

class Stay(Objective):
    def __init__(self, position, size, duration):
        super().__init__(position, size)
        self.duration = duration
        self.complete = False
        self.curent_time = 0
        self.countdown_start = True
        self.countdown_active = False

    def update(self):
        if self.complete:
            return "Completed you can move on", "not relevant"
        
        if self.countdown_start:
                start_time = pygame.time.get_ticks() * 1000 # Get the current time in milliseconds
                countdown_duration = self.duration # Duration of the countdown in milliseconds (e.g., 3000ms = 3 seconds)
                self.countdown_active = True # Flag to indicate that the countdown is active
                self.end_countdown_tick = start_time + countdown_duration # Calculate the time when the countdown should end
                self.countdown_start = False

        while self.countdown_active:
            if pygame.time.get_ticks() >= self.end_countdown_tick:
                self.countdown_active = False
                print("stay done")
                return "Completed you can move on", "not relevant"
            elif pygame.time.get_ticks() <= self.end_countdown_tick:
                self.sec_till_win_remaining = (self.end_countdown_tick - pygame.time.get_ticks()) // 1000 # Calculate the remaining seconds until win
                self.complete = True
                return f"Stay completed in {self.sec_till_win_remaining} s", "not relevant"
    
    def main_work(self):
        if self.complete:
            return "Completed you can move on", "not relevant"
        else:
            return self.update()
        
    def reset(self):
        self.curent_time = 0
        self.countdown_start = True
        self.countdown_active = False


class Flyby(Objective):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.complete = False

    def update(self):
        self.complete = True
        return "Completed you can move on", "not relevant"
    
    def main_work(self):
        if self.complete:
            return "Completed you can move on", "not relevant"
        else:
            return self.update()
        
    def reset(self):
        print("not needed")

OBJECTIVE_TYPES = {
    "flyby": {
        "class": Flyby,
        "tile_path": 'pictures/tiles/Flyby.png',
    },
    "stay": {
        "class": Stay,
        "tile_path": 'pictures/tiles/Stay.png',
        "duration": 3.0,
    },
}


def resolve_objective_kind(objective_data):
    if objective_data is False or objective_data is None:
        return None
    if isinstance(objective_data, str):
        objective_kind = objective_data.lower()
        return objective_kind if objective_kind in OBJECTIVE_TYPES else None
    return conf.objective_kinds.get(objective_data)


def get_objective_definition(objective_data):
    objective_kind = resolve_objective_kind(objective_data)
    if objective_kind is None:
        return None
    return {
        "kind": objective_kind,
        **OBJECTIVE_TYPES[objective_kind],
    }


def create_objective(objective_kind, position, size):
    """Create an objective instance based on the kind, position, and size."""
    if objective_kind not in OBJECTIVE_TYPES:
        return None
    
    objective_class = OBJECTIVE_TYPES[objective_kind]["class"]
    
    # Different objective types may have different constructor signatures
    if objective_kind == "stay":
        duration = OBJECTIVE_TYPES[objective_kind].get("duration", 3.0)
        return objective_class(position, size, duration)
    else:
        return objective_class(position, size)


print("Work in progress, objectives system is being implemented...")