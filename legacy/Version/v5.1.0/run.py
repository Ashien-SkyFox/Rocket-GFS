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
#  {[**Author**]}      Cutie Ashien
#  {[**Version**]}     5.1.0
#  {[**Date**]}        2026-04-22
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
#   - v5.0.0 Collision End check and start of refactoring.
#       - Checks if player is at the endpoint and ending the game.
#       - Started refactoring the code for better readability and maintainability.
#       - Refactored the game loop into a separate function for better organization.
#       - Refactored the collision handling logic for better clarity and separation of concerns.
#       - Added comments and documentation for better understanding of the code.
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
#     - v4.1.1: Minor bug fixes and improvements.
#       - Fixed minor bugs related to level selection functions.
#       - Improved code readability and maintainability.
#       - Fixed bug that the Ship wouldn't spawn at the center start point in certain situations.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v4.1.0: Fluid map selection update.
#       - Improved map selection logic for changinging map count dynamically.
#       - rewrote the functions that show the map selection to support dynamic map count.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#     - v4.0.4: Structure overhaul(map).
#       - Moved the map class to a separate file (map.py).
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
# Written by Cutie Ashien (https://github.com/Ashien-SkyFox)
##################################################################################################################################################################################################################

### File Imports ###
import levels as levels # Importing levels module
import config as conf # Importing config module
import helper.main_menu as mm # Importing map helper module
import helper.ship as sh # Importing ship helper module
import helper.map as mp # Importing map helper module
import helper.objectives as obj # Importing objectives module

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

### Game Loop ###

def game_loop():
    pygame.display.set_caption("Rocket - v5.1.0") # Setting the window title
    pygame.init()

    map_selected = 0 # 0 = main menu, -1 = map loaded
    screen = pygame.display.set_mode((screensize_x, screensize_y)) # set the screen size
    clock = pygame.time.Clock() # Creating a clock object to manage the frame rate

    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #

    main_menu_instance = mm.MainMenu(map_selected, highscore)
    ship_instance = sh.Ship()
    ship_orginal = ship_instance.create_ship_image()
    running = True
    reset_ship = False
    delta_time = 0.0

    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #

    def start_game_loop(running=running, map_selected=map_selected, reset_ship=reset_ship, ship_instance=ship_instance, ship_orginal=ship_orginal, main_menu_instance=main_menu_instance, delta_time=delta_time):
        while running:
            for event in pygame.event.get(): # Quiting the game loop if the window is closed
                if event.type == pygame.QUIT: 
                    running = False 

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #

            screen.fill((0, 0, 0)) # Filling the screen with black color to clear previous frame

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #

            if reset_ship == True: # deliting and recreating the ship instance to reset all values
                ship_instance = sh.Ship()
                ship_orginal = ship_instance.create_ship_image()
                reset_ship = False

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #

            if map_selected == 0:
                map = main_menu_instance.main_menu_loop(screen) # Displaying the main menu
                level_info, objective = levels.get_level_info()
                if map in level_info: # Checking if the selected map is valid
                    main_menu_instance.map_loading_animation(screen) # Displaying the map loading animation
                    map_instance = mp.TileMap(levels.grapp_level(map), objective[map]) # Creating a tilemap instance based on the selected map
                    ship, ship_rect = ship_instance.get_rect()
                    spawn_position = map_instance.get_location_of_spawn_point(ship_rect) # Getting the spawn position from the tilemap
                    ship_instance.position = spawn_position # Setting the ship position to the spawn position
                    map_instance.tile_group.draw(screen) # Drawing the tilemap on the screen
                    map_selected = -1 # Setting the value to -1 to indicate that a map has been selected
                    game_state = "running" # Setting the game state to running

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #

            if map_selected == -1:
                if game_state == "running":
                    position = ship_instance.get_ship_position() # Getting the ship position for map movement
                    spirit_collision_group = map_instance.draw_map(screen, position) # Drawing the map on the screen and getting the collision group
                    ship_instance.import_surface(screen) # Importing the collision surface to the ship instance for pixel color detection
                    ship_instance.update_thruster_inputs() # Update thruster inputs based on key presses
                    ship_instance.ship_rotate() # Update ship movement based on thruster inputs
                    text_to_show, reason = ship_instance.move_ship(spirit_collision_group) # Move the ship based on current velocity and acceleration
                    ship_instance.render_ship_maps() # Render the ship with updated rotation
                    game_state = ship_instance.check_game_state() # Check for game over or level completion
                    ship, ship_rect = ship_instance.get_rect() # Getting the ship image and rect for rendering
                    objective_completed = map_instance.update_objective(ship_rect, delta_time)
                    if objective_completed and conf.debug_mode:
                        print("Objective complete")
                    if conf.debug_mode:
                        ship_instance.debug() # Starting the debug
                    screen.blit(ship, ship_rect) # Drawing the ship on the screen at the center position
                    if text_to_show is not None:
                        font = pygame.font.SysFont(None, 74) # Creating a font object for rendering text
                        if reason is not None and reason == "Countdown Win":
                            text_to_show_font = font.render(text_to_show, True, (255, 0, 255))
                            screen.blit(text_to_show_font, (screensize_x // 2 - text_to_show_font.get_width() // 2, screensize_y // 2 - text_to_show_font.get_height() // 2)) # Blits the needed text
                        else:
                            text_to_show_font = font.render(text_to_show, True, (255, 0, 255))
                            screen.blit(text_to_show_font, (screensize_x // 2 - text_to_show_font.get_width() // 2, screensize_y // 2 - text_to_show_font.get_height() // 2)) # Blits the needed text
                            pygame.display.flip() # Updating the display to show the new frame
                            pygame.time.delay(1000) # Delay for a second before resetting
                            if game_state == "game over" or "Win":
                                screen.fill((0, 0, 0)) # Filling the screen with black color to clear previous frame
                                map_selected = 0 # Returning to main menu
                                map = 0 # Resetting map variable
                                reset_ship = True # Resetting the ship
                                main_menu_instance.main_menu_reset() # Resetting the main menu instance
                            else:
                                print("ERROR")
                    """
                    Do i remember how the heck that even worked :/
                        Probably not :D
                    Do i need to redo the logic?
                        absolutely, becaus it looks messy af
                    But do i want to rn?
                        Not really :/
                    Maybe later :3
                    -v4.0.4
                    Kinda work on it in like v4.2.0. but still do't remember how it works anyway
                    -v4.2.2
                    Well I started Refactoring
                    -v4.2.5
                    """

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #
            
            pygame.display.flip() # Updating the display to show the new frame
            delta_time = clock.tick(60) / 1000.0 # Limiting the frame rate to 60 FPS and storing frame time

    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #

    start_game_loop()
    pygame.quit()

game_loop()
"""
Starting the game loop
"""