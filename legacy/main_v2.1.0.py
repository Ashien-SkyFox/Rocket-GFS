##################################################################################################################################################################################################################
# ================================================================================================================================================================================================================
#   ██████╗ ██╗   ██╗      █████╗ ███████╗██╗  ██╗██╗███████╗███╗   ██╗
#   ██╔══██╗╚██╗ ██╔╝     ██╔══██╗██╔════╝██║  ██║██║██╔════╝████╗  ██║
#   ██████╔╝ ╚████╔╝      ███████║███████╗███████║██║█████╗  ██╔██╗ ██║
#   ██╔══██╗  ╚██╔╝       ██╔══██║╚════██║██╔══██║██║██╔══╝  ██║╚██╗██║
#   ██████╔╝   ██║        ██║  ██║███████║██║  ██║██║███████╗██║ ╚████║
#   ╚═════╝    ╚═╝        ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝
# ================================================================================================================================================================================================================
#  {[**Project**]}     Rocket Reprogramation of ZKM
#  {[**File**]}        main.py
#  {[**Author**]}      Ashien the Skyfox
#  {[**Version**]}     2.1.0
#  {[**Date**]}        2025-11-06
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

import pygame
import os
import time

def game_loop():
    pygame.init()

    screensize_x = 800
    screensize_y = 600
    """
    Problems: If you would want to change the screen size you would have to change it in multiple places or else the pictures would not be in the ritght place
    Fixed: I created variables for the screen size and used them in the code with multiplaycations.
    """

    screen = pygame.display.set_mode((screensize_x, screensize_y)) # set the screen size

    clock = pygame.time.Clock() # Creating a clock object to manage the frame rate

    class Ship:
        def __init__(self):
            ##### Ajustable Favtors #####

            # Thruster ratios
            self.inner_truster_ratue = 1.15
            self.outer_truster_ratue = 1.4
            self.middle_truster_ratue = 1.0

            # Rotation and movement factors
            self.acceleration = 0.2
            self.rotate_friction = 0.95

            ### Game Varibals ###
            # Thruster Inputs
            self.input_thruster_outer_left = 0 
            self.input_thruster_inner_left = 0
            self.input_thruster_middle = 0
            self.input_thruster_inner_right = 0
            self.input_thruster_outer_right = 0
            
            # Variables for rotation update
            self.rotate_angle = 0
            self.rotate_velocity = 0

        def create_ship_image(self):
            self.ship_orginal = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Pictures','Rocket.png')).convert_alpha()
            """
            Problems: I couldent load the image from a subfolder
            Fixed: I used os.path.join to create the correct path to the image
            """
        
        def render_ship(self, screensize_x, screensize_y):
            self.ship_rect = self.ship.get_rect(center = ((0.5 * screensize_x), (0.5 * screensize_y)))
            return self.ship, self.ship_rect
        
        def update_thruster_inputs(self):
            # Read key inputs
            keys = pygame.key.get_pressed()
            # Reset thruster inputs
            self.input_thruster_outer_left = 0
            self.input_thruster_inner_left = 0
            self.input_thruster_middle = 0
            self.input_thruster_inner_right = 0
            self.input_thruster_outer_right = 0

            if keys[pygame.K_g]: #Update thruster Outer Left
                self.input_thruster_outer_left = self.outer_truster_ratue

            if keys[pygame.K_h]: #Update thruster Inner Left
                self.input_thruster_inner_left = self.inner_truster_ratue

            if keys[pygame.K_j]: #Update thruster Middle
                self.input_thruster_middle = self.middle_truster_ratue

            if keys[pygame.K_k]: #Update thruster Inner Right
                self.input_thruster_inner_right = self.inner_truster_ratue

            if keys[pygame.K_l]: #Update thruster Outer Right
                self.input_thruster_outer_right = self.outer_truster_ratue

        def ship_rotate(self):
            speedup_rotate = ((self.input_thruster_outer_right + self.input_thruster_inner_right) - (self.input_thruster_inner_left + self.input_thruster_outer_left)) # Turning speed based on thruster input
            if self.rotate_angle > 360 or self.rotate_angle < -360: # Resetting the rotate angle to prevent overflow
                self.rotate_angle = 0
            self.rotate_velocity += speedup_rotate * self.acceleration # Adding the speedup input multiplied by the acceleration to the rotate velocity

            self.rotate_velocity *= self.rotate_friction # Applying friction to the rotate velocity to slowly decrease it over time

            self.rotate_angle += self.rotate_velocity # Updating the rotate angle based on the rotate velocity

            self.ship = pygame.transform.rotate(self.ship_orginal, self.rotate_angle) # Rotating the ship image based on the rotate angle  

        def get_info_for_render(self):
            self.ship_rect = self.ship.get_rect(center = ((0.5 * screensize_x), (0.5 * screensize_y)))
            return self.ship, self.ship_rect
        
        
        def debug(self): # For debugging the Game Varibals
            debug_values = {
                "rotate_angle" : self.rotate_angle,
                "input_thruster_outer_left": self.input_thruster_outer_left,
                "input_thruster_inner_left": self.input_thruster_inner_left,
                "input_thruster_middle": self.input_thruster_middle,
                "input_thruster_inner_right": self.input_thruster_inner_right,
                "input_thruster_outer_right": self.input_thruster_outer_right,
                "rotate_velocity": self.rotate_velocity,
                "acceleration": self.acceleration,
                "rotate_friction": self.rotate_friction,
                }
            for argument, value in debug_values.items():
                print(f"{argument}: {value}")


    ship_instance = Ship()
    ship_orginal = ship_instance.create_ship_image()
    running = True
    while running:
        for event in pygame.event.get(): # Quiting the game loop if the window is closed
            if event.type == pygame.QUIT: 
                running = False 

        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #
        
        screen.fill((0, 0, 0)) # Filling the screen with black color to clear previous frame

        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #

        ship_instance.update_thruster_inputs() # Update thruster inputs based on key presses
        ship_instance.ship_rotate() # Update ship movement based on thruster inputs
        ship_instance.render_ship(screensize_x, screensize_y) # Render the ship with updated rotation
        ship, ship_rect = ship_instance.get_info_for_render()
        screen.blit(ship, ship_rect) # Drawing the ship on the screen at the center position
        ship_instance.debug() # Starting the debug

        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #

        pygame.display.flip() # Updating the display to show the new frame
        clock.tick(60) # Limiting the frame rate to 60 FPS

        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #

    pygame.quit()


game_loop()
"""
Starting the game loop
"""