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
#  {[**Version**]}     6.0.0
#  {[**Date**]}        2026-06-04
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
#      - Fixed crash on load level with no or broken objective
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
        self.duration = duration * 1000 # Convert duration from seconds to milliseconds
        self.complete = False
        self.curent_time = 0
        self.countdown_start = True
        self.countdown_active = False

    def update(self):
        if self.complete:
            return "Completed you can move on", "not relevant"
        
        if self.countdown_start:
                start_time = pygame.time.get_ticks() # Get the current time in milliseconds
                countdown_duration = self.duration # Duration of the countdown in milliseconds
                self.countdown_active = True # Flag to indicate that the countdown is active
                self.end_countdown_tick = start_time + countdown_duration # Calculate the time when the countdown should end
                print(f"Countdown started, will end on tick {self.end_countdown_tick}")
                self.countdown_start = False

        while self.countdown_active:
            if pygame.time.get_ticks() >= self.end_countdown_tick:
                self.countdown_active = False
                self.complete = True
                print("stay done")
                return "Completed you can move on", "not relevant"
            elif pygame.time.get_ticks() <= self.end_countdown_tick:
                self.sec_till_win_remaining = self.end_countdown_tick - pygame.time.get_ticks() # Calculate the remaining seconds until win
                self.complete = False
                return f"Stay completed in {self.sec_till_win_remaining/1000:.2f} s", "not relevant"
    
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

class NoneObjective(Objective):
    def __init__(self, position, size):
        super().__init__(position, size)
        self.complete = True

    def main_work(self):
        return "No objective, you can move on", "not relevant"

    def reset(self):
        print("not needed")

OBJECTIVE_TYPES = conf.objective_kinds

def resolve_objective_kind(objective_data):
    if objective_data is False or objective_data is None:
        return None

    if isinstance(objective_data, str):
        objective_kind = objective_data.lower()
        for objective_definition in OBJECTIVE_TYPES.values():
            if objective_definition.get("type") == objective_kind:
                return objective_kind
        return None

    objective_definition = OBJECTIVE_TYPES.get(objective_data)
    if objective_definition is None:
        return None
    return objective_definition.get("type")

def get_objective_definition(objective_data):
    objective_kind = resolve_objective_kind(objective_data)
    if objective_kind is None:
        return None

    for objective_definition in OBJECTIVE_TYPES.values():
        if objective_definition.get("type") == objective_kind:
            return objective_definition

    return None

def create_objective(objective_data, position, size, duration=None):
    if objective_data == "flyby":
        return Flyby(position, size)
    elif objective_data == "stay":
        if duration is None or duration is False:
            return NoneObjective(position, size)
        return Stay(position, size, duration)
    else:
        return NoneObjective(position, size)
print("Work in progress, objectives system is being implemented...")