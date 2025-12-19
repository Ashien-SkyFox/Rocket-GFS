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
#  {[**Author**]}      Ashien the Skyfox
#  {[**Version**]}     4.0.3
#  {[**Date**]}        2025-11-07
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
# Written by Ashien the Skyfox (https://github.com/Ashien-SkyFox)
##################################################################################################################################################################################################################

### File Imports ###
import config

### Library Imports ###
import pygame

### Config Imports ###
screensize_x = config.screensize_x
screensize_y = config.screensize_y

class main_menu:
        def __init__(self, map_selected = 0, highscore = 0): # Initializing the main menu with map selection and highscore
            self.map_selected = map_selected
            self.highscore = highscore
            self.window = "main_menu" # Setting the initial window to main menu
            self.font = pygame.font.Font(None, 36) # Creating a font object for rendering text
            self.maps = {
                1: "Level 1",
                2: "Level 2"
            }
            self.center_x = screensize_x // 2
            self.center_y = screensize_y // 2

        def main_menu(self, screen):
            self.highscore_front = self.font.render(f"Highscore: {self.highscore}", True, (255, 255, 255), None) # Rendering the highscore text
            screen.blit(self.highscore_front, (10, 10)) # Blitting the highscore text to the screen
            
            # Create buttons in the middle of the screen
            
            # Create button texts
            levels_button_text = self.font.render("Levels", True, (255, 255, 255), None)
            quit_button_text = self.font.render("Quit", True, (255, 255, 255), None)
            
            # Create button rectangles
            levels_rect = pygame.Rect(self.center_x - levels_button_text.get_width() // 2, self.center_y - 50, levels_button_text.get_width(), levels_button_text.get_height())
            quit_rect = pygame.Rect(self.center_x - quit_button_text.get_width() // 2, self.center_y + 10, quit_button_text.get_width(), quit_button_text.get_height())

            # Check for mouse clicks and hover
            mouse_pos = pygame.mouse.get_pos()
            mouse_clicked = pygame.mouse.get_pressed()[0]
            
            # Change colors on hover
            levels_color = (255, 255, 0) if levels_rect.collidepoint(mouse_pos) else (255, 255, 255)
            quit_color = (255, 255, 0) if quit_rect.collidepoint(mouse_pos) else (255, 255, 255)
            
            # Re-render texts with hover colors
            levels_button_text = self.font.render("Levels", True, levels_color, None)
            quit_button_text = self.font.render("Quit", True, quit_color, None)
            
            # Draw buttons
            screen.blit(levels_button_text, (self.center_x - levels_button_text.get_width() // 2, self.center_y - 50))
            screen.blit(quit_button_text, (self.center_x - quit_button_text.get_width() // 2, self.center_y + 10))

            # Handle button clicks
            if mouse_clicked:
                if levels_rect.collidepoint(mouse_pos):
                    self.window = "map_selection"
                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()

        def main_menu_loop(self, screen):

            if self.window == "main_menu": # Displaying the main menu
                self.main_menu(screen)
            elif self.window == "map_selection": # Displaying the map selection menu
                self.open_map_selection(screen)
                return self.map_selected

        def open_map_selection(self, screen):
            vertical_spacing = 30  # Consistent vertical spacing between elements
            start_y = 10

            self.title_text = self.font.render("Select a level:", True, (255, 255, 255), None) # Rendering the title text
            self.info_text = self.font.render("Click at the level you want to choose", True, (255, 255, 255), None) # Rendering the info text
            self.level1_button_text = self.font.render("1. Level 1", True, (255, 255, 255), None) # Rendering the level 1 button text
            self.level2_button_text = self.font.render("2. Level 2", True, (255, 255, 255), None) # Rendering the level 2 button text

            # Create button rectangles
            level1_rect = pygame.Rect(10, start_y + 2 * vertical_spacing, self.level1_button_text.get_width(), self.level1_button_text.get_height()) # Rectangle for level 1 button
            level2_rect = pygame.Rect(10, start_y + 3 * vertical_spacing, self.level2_button_text.get_width(), self.level2_button_text.get_height()) # Rectangle for level 2 button

            # Check for mouse clicks
            mouse_pos = pygame.mouse.get_pos() # Getting the mouse position
            mouse_clicked = pygame.mouse.get_pressed()[0] # Checking if the left mouse button is clicked

            # Highlight buttons on hover
            level1_color = (255, 255, 0) if level1_rect.collidepoint(mouse_pos) else (255, 255, 255) # Changing color on hover level 1
            level2_color = (255, 255, 0) if level2_rect.collidepoint(mouse_pos) else (255, 255, 255) # Changing color on hover

            # Re-render text with appropriate colors
            self.level1_button_text = self.font.render("1. Level 1", True, level1_color, None) # Rendering the level 1 button text with hover color
            self.level2_button_text = self.font.render("2. Level 2", True, level2_color, None) # Rendering the level 2 button text with hover color

            screen.blit(self.title_text, (10, start_y)) # Blitting the title text to the screen
            screen.blit(self.info_text, (10, start_y + vertical_spacing)) # Blitting the info text to the screen
            screen.blit(self.level1_button_text, (10, start_y + 2 * vertical_spacing)) # Blitting the level 1 button text to the screen
            screen.blit(self.level2_button_text, (10, start_y + 3 * vertical_spacing))

            # Handle button clicks
            if mouse_clicked: # If the mouse is clicked
                if level1_rect.collidepoint(mouse_pos): # If the mouse is over the level 1 button
                    self.map_selected = 1
                    return 1
                elif level2_rect.collidepoint(mouse_pos):
                    self.map_selected = 2
                    return 2
                
        def map_loading_animation(self, screen):
            loading_text = self.font.render("Loading...", True, (255, 255, 255), None)
            screen.fill((0, 0, 0)) # Filling the screen with black color to clear previous frame
            screen.blit(loading_text, (self.center_x - loading_text.get_width() // 2, self.center_y))  # Blit the loading text to the screen
            pygame.display.flip()  # Update the display
            pygame.time.delay(500)  # Delay for half a second