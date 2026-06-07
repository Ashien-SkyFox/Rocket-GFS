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
#  {[**File**]}        main_menu.py
#  {[**Author**]}      Cutie Ashien
#  {[**Version**]}     6.0.0
#  {[**Date**]}        2026-06-04
#  {[**Python**]}      3.11.x
#  {[**License**]}     MIT
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Description**]}
#
#                  This module contains the main menu functionality of Rocket.
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
#     - v4.1.0: Fluid map selection update.
#       - rewrote the functions that show the map selection to support dynamic map count.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v4.0.2: Structure overhaul(main menu).
#       - Moved the main menu functionality to a separate file (main_menu.py).
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
import config as conf
import levels

# ------------------------------------------------------------------------------ #

### Library Imports ###
import pygame

# ------------------------------------------------------------------------------ #


### Config Imports ###
screensize_x = conf.screensize_x
screensize_y = conf.screensize_y

# Define color constants
HOVER_COLOR = (255, 255, 0)

class MainMenu:
        def __init__(self, map_data, map_selected = 0, highscore = 0, level_scores = None): # Initializing the main menu with map selection and highscore
            self.map_data = map_data
            self.map_selected = map_selected
            self.highscore = highscore
            self.level_scores = level_scores if isinstance(level_scores, dict) else {}
            self.window = "main_menu" # Setting the initial window to main menu
            self.font = pygame.font.Font(None, 36) # Creating a font object for rendering text
            self.map_info = self.map_data[0]  # Get level names for menu display
            self.objective_info = self.map_data[1]  # Get objective levels for level loading
            self.duration_info = self.map_data[2]  # Get objective durations for level loading
            self.center_x = screensize_x // 2
            self.center_y = screensize_y // 2
            self.level_count = len(self.map_info)  # Get the number of available levels
            self.level_names = self.map_info.values()  # Get level names
            self.explanation_lines = [
                "How to play:",
                "Use G, H, J, K, L to control thrusters.",
                "Land safely on cyan start/finish pads.",
                "Avoid red zones or you will crash.",
                "Follow the top arrow to objective, then finish.",
            ]

        def update_screen_size(self, screen):
            self.center_x = screen.get_width() // 2
            self.center_y = screen.get_height() // 2

        def button_check_colision(self, mouse_pos, mouse_clicked, button_rect):
            if mouse_clicked and button_rect.collidepoint(mouse_pos):
                return True
            return False

        def main_menu(self, screen):
            self.update_screen_size(screen)
            self.highscore_front = self.font.render(f"Highscore: {self.highscore}", True, (255, 255, 255), None) # Rendering the highscore text
            screen.blit(self.highscore_front, (10, 10)) # Blitting the highscore text to the screen
            
            # Render buttons
            levels_button_text = self.font.render("Levels", True, (255, 255, 255), None)
            levels_rect = pygame.Rect(self.center_x - levels_button_text.get_width() // 2, self.center_y - 50, levels_button_text.get_width(), levels_button_text.get_height())
            explanation_button_text = self.font.render("Explanation", True, (255, 255, 255), None)
            explanation_rect = pygame.Rect(self.center_x - explanation_button_text.get_width() // 2, self.center_y + 10, explanation_button_text.get_width(), explanation_button_text.get_height())
            quit_button_text = self.font.render("Quit", True, (255, 255, 255), None)
            quit_rect = pygame.Rect(self.center_x - quit_button_text.get_width() // 2, self.center_y + 70, quit_button_text.get_width(), quit_button_text.get_height())

            # Get mouse position and click status
            mouse_pos = pygame.mouse.get_pos()
            mouse_clicked = pygame.mouse.get_pressed()[0]

            # Check button collisions
            if self.button_check_colision(mouse_pos, mouse_clicked, levels_rect):
                self.window = "map_selection"
            elif self.button_check_colision(mouse_pos, mouse_clicked, explanation_rect):
                self.window = "explanation"
            elif self.button_check_colision(mouse_pos, mouse_clicked, quit_rect):
                pygame.quit()
                sys.exit(0)

            # Blit buttons to screen
            screen.blit(levels_button_text, (levels_rect.x, levels_rect.y))
            screen.blit(explanation_button_text, (explanation_rect.x, explanation_rect.y))
            screen.blit(quit_button_text, (quit_rect.x, quit_rect.y))

        def main_menu_loop(self, screen):

            if self.window == "main_menu": # Displaying the main menu
                self.main_menu(screen)
            elif self.window == "map_selection": # Displaying the map selection menu
                self.open_map_selection(screen)
                return self.map_selected
            elif self.window == "explanation":
                self.explanation_menu(screen)

        def explanation_menu(self, screen):
            self.update_screen_size(screen)
            mouse_pos = pygame.mouse.get_pos()
            mouse_clicked = pygame.mouse.get_pressed()[0]

            title_text = self.font.render("Explanation", True, (255, 255, 255), None)
            screen.blit(title_text, (self.center_x - title_text.get_width() // 2, 40))

            line_spacing = 40
            start_y = 100
            for index, text_line in enumerate(self.explanation_lines):
                line_surface = self.font.render(text_line, True, (220, 220, 220), None)
                screen.blit(line_surface, (self.center_x - line_surface.get_width() // 2, start_y + (index * line_spacing)))

            back_text = self.font.render("Back", True, (255, 255, 255), None)
            back_rect = pygame.Rect(self.center_x - back_text.get_width() // 2, self.center_y + 180, back_text.get_width(), back_text.get_height())

            if back_rect.collidepoint(mouse_pos):
                back_text = self.font.render("Back", True, HOVER_COLOR, None)

            if self.button_check_colision(mouse_pos, mouse_clicked, back_rect):
                self.window = "main_menu"

            screen.blit(back_text, (back_rect.x, back_rect.y))

        def open_map_selection(self, screen):
            vertical_spacing = 30  # Consistent vertical spacing between elements
            start_y = 10

            self.title_text = self.font.render("Select a level:", True, (255, 255, 255), None) # Rendering the title text
            self.info_text = self.font.render("Click at the level you want to choose", True, (255, 255, 255), None) # Rendering the info text

            # Get mouse position and click status
            mouse_pos = pygame.mouse.get_pos()
            mouse_clicked = pygame.mouse.get_pressed()[0]

            screen.blit(self.title_text, (10, start_y)) # Blitting the title text to the screen
            screen.blit(self.info_text, (10, start_y + vertical_spacing)) # Blitting the info text to the screen

            # Dynamically create buttons for all available levels
            for level_num in range(1, self.level_count + 1):
                level_name = list(self.level_names)[level_num - 1]  # Get level name from levels.py
                level_points = int(self.level_scores.get(str(level_num), 0))
                level_label = f"{level_num}. {level_name} [{level_points}]"
                button_y = start_y + (level_num + 1) * vertical_spacing
                        
                # Create button text and rectangle
                button_text = self.font.render(level_label, True, (255, 255, 255), None)
                button_rect = pygame.Rect(10, button_y, button_text.get_width(), button_text.get_height())
                        
                # Check for hover effect
                if button_rect.collidepoint(mouse_pos):
                    button_text = self.font.render(level_label, True, HOVER_COLOR, None)
                        
                # Check for collision using button_check_colision method
                if self.button_check_colision(mouse_pos, mouse_clicked, button_rect):
                    self.map_selected = level_num
                    return level_num
                        
                # Blit button to screen
                screen.blit(button_text, (10, button_y))
                
        def map_loading_animation(self, screen):
            self.update_screen_size(screen)
            loading_text = self.font.render("Loading...", True, (255, 255, 255), None)
            screen.fill((0, 0, 0)) # Filling the screen with black color to clear previous frame
            screen.blit(loading_text, (self.center_x - loading_text.get_width() // 2, self.center_y))  # Blit the loading text to the screen
            pygame.display.flip()  # Update the display
            pygame.time.delay(500)  # Delay for half a second

        def main_menu_reset(self):
            self.map_selected = 0
            self.window = "main_menu"