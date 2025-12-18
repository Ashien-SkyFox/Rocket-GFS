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
#  {[**Version**]}     3.0.0
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
# Written by Ashien the Skyfox (https://github.com/Ashien-SkyFox)
##################################################################################################################################################################################################################

from unittest import case
import pygame
import os
import time
import math

def game_loop():
    pygame.init()

    ##########################################################
    ##########################################################
    # Ajustable Favtors #

    # screen size
    screensize_x = 1900
    screensize_y = 800
    """
    Problems: If you would want to change the screen size you would have to change it in multiple places or else the pictures would not be in the ritght place
    Fixed: I created variables for the screen size and used them in the code with multiplaycations.
    """

    ##########################################################
    ##########################################################
    
    map_selected = 0
    vector = pygame.math.Vector2



    screen = pygame.display.set_mode((screensize_x, screensize_y)) # set the screen size

    clock = pygame.time.Clock() # Creating a clock object to manage the frame rate

    class Ship:
        def __init__(self):
            ##########################################################
            ##########################################################

            ##### Ajustable Favtors #####
            # Trustor key bindings
            self.thruster_key_outer_left = pygame.K_g
            self.thruster_key_inner_left = pygame.K_h
            self.thruster_key_middle = pygame.K_j
            self.thruster_key_inner_right = pygame.K_k
            self.thruster_key_outer_right = pygame.K_l

            # Thruster ratios
            self.inner_truster_ratue = 0.6
            self.outer_truster_ratue = 1.0
            self.middle_truster_ratue = 1.0

            ##########################################################
            ##########################################################

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

            self.movement_speed = 0
            self.position = vector(0, 0) # Ship position
            self.velocity = vector(0, 0) # Ship velocity
            self.acceleration_vector = vector(0, 0) # Ship acceleration
            self.acceleration_vector = vector(0, 0) # Ship acceleration

        def create_ship_image(self):
            self.ship_orginal = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Pictures','Rocket.png')).convert_alpha()
            """
            Problems: I couldent load the image from a subfolder
            Fixed: I used os.path.join to create the correct path to the image
            """
            ships_size = ((0.1 * screensize_x) + (0.1 * screensize_y)) / 2 # Calculating the ship size based on screen size
            self.ship_orginal = pygame.transform.scale(self.ship_orginal, (ships_size, ships_size)) # Scaling the ship image based on screen size
        
        def render_ship_maps(self):
            self.ship_rect = self.ship.get_rect(center = ((0.5 * screensize_x), (0.5 * screensize_y))) # Getting the rect of the ship image to center it on the screen
            return self.ship, self.ship_rect # Returning the ship image and rect for rendering

        def update_thruster_inputs(self):
            # Read key inputs
            keys = pygame.key.get_pressed()
            # Reset thruster inputs
            self.input_thruster_outer_left = 0
            self.input_thruster_inner_left = 0
            self.input_thruster_middle = 0
            self.input_thruster_inner_right = 0
            self.input_thruster_outer_right = 0

            if keys[self.thruster_key_outer_left]: #Update thruster Outer Left
                self.input_thruster_outer_left = self.outer_truster_ratue

            if keys[self.thruster_key_inner_left]: #Update thruster Inner Left
                self.input_thruster_inner_left = self.inner_truster_ratue

            if keys[self.thruster_key_middle]: #Update thruster Middle
                self.input_thruster_middle = self.middle_truster_ratue

            if keys[self.thruster_key_inner_right]: #Update thruster Inner Right
                self.input_thruster_inner_right = self.inner_truster_ratue

            if keys[self.thruster_key_outer_right]: #Update thruster Outer Right
                self.input_thruster_outer_right = self.outer_truster_ratue

        def ship_rotate(self):
            speedup_rotate = ((self.input_thruster_outer_right + self.input_thruster_inner_right) - (self.input_thruster_inner_left + self.input_thruster_outer_left)) # Turning speed based on thruster input
            self.rotate_angle %= 360  # Keep the angle within [0, 360) to prevent overflow
            self.rotate_velocity += speedup_rotate * self.acceleration # Adding the speedup input multiplied by the acceleration to the rotate velocity

            self.rotate_velocity *= self.rotate_friction # Applying friction to the rotate velocity to slowly decrease it over time

            self.rotate_angle += self.rotate_velocity # Updating the rotate angle based on the rotate velocity

            self.ship = pygame.transform.rotate(self.ship_orginal, self.rotate_angle) # Rotating the ship image based on the rotate angle  

        def move_ship(self):
            # Calculate forward direction based on current rotation
            rad_angle = math.radians(self.rotate_angle-90) # Convert angle to radians (remove inversion if not needed)
            forward_direction = vector(math.cos(rad_angle), -math.sin(rad_angle)) # Calculate forward direction vector

            # Calculate total thrust from all thrusters
            total_thrust = -(self.input_thruster_outer_left + self.input_thruster_inner_left +
                    self.input_thruster_middle +
                    self.input_thruster_inner_right + self.input_thruster_outer_right)
            """
            Problem: the acceleration was fliped
            Solution: I was lazy and just added a negative sign in front of the total thrust calculation
            """

            # Update acceleration based on total thrust and forward direction
            max_acceleration = 2.0  # Limits ship acceleration for smoother control; adjust for desired responsiveness
            raw_acceleration = forward_direction * total_thrust * self.acceleration
            if raw_acceleration.length() > max_acceleration:
                raw_acceleration = raw_acceleration.normalize() * max_acceleration
            self.acceleration_vector = raw_acceleration

            # Update velocity and position
            self.velocity += self.acceleration_vector
            self.velocity *= 0.98  # Apply velocity damping for realism
            self.position += self.velocity
            
        def get_ship_position(self):
            return self.position

        def get_rect(self):
            self.ship_rect = self.ship.get_rect(center = ((0.5 * screensize_x), (0.5 * screensize_y))) # Getting the rect of the ship image to center it on the screen
            return self.ship, self.ship_rect # Returning the ship image and rect for rendering
        
        
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
                "position": self.position,
                "velocity": self.velocity,
                "acceleration_vector": self.acceleration_vector                
                }
            for argument, value in debug_values.items():
                print(f"{argument}: {value}")

            print("--------------------")
            print()
    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #  

    class TileMap:
        def __init__(self, map_data):
            # Load tile images
            self.tile_size = (int((0.05 * screensize_x) + (0.05 * screensize_y)) / 2, int((0.05 * screensize_x) + (0.05 * screensize_y)) / 2) # Calculating the tile size based on screen size
            self.wall_tile = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Pictures', 'Tiles', 'Basic_wall.png')).convert_alpha() # Loading tile images
            self.start_point_tile = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Pictures', 'Tiles', 'Start_point.png')).convert_alpha() # Loading tile images
            self.finish_point_tile = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Pictures', 'Tiles', 'Finisch_point.png')).convert_alpha() # Loading tile images

            # Store map data
            self.map_data = map_data # Storing the map data
            self.width = len(map_data[0]) * self.tile_size[0] # Calculating the width of the map based on the number of columns and tile size
            self.height = len(map_data) * self.tile_size[1] # Calculating the height of the map based on the number of rows and tile size
            self.tile_group = pygame.sprite.Group() # Group to hold all tile sprites
            self.create_tiles() # Creating the tile sprites

            #scaling the map based on screen size
            tile_size = ((0.2 * screensize_x) + (0.2 * screensize_y)) / 2 # New tile size based on screen size
            new_tile_size = int(tile_size)
            self.tile_size = (new_tile_size, new_tile_size)

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
            for row_index, row in enumerate(self.scaled_tile_images):
                for col_index, tile_image in enumerate(row):
                    if tile_image:
                        x = col_index * self.tile_size[0] + self.location.x
                        y = row_index * self.tile_size[1] + self.location.y
                        screen.blit(tile_image, (x, y))


    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #


    # Ceate tilemap for easy level design
    # List: 0 = empty, 1 = Basic_wall, 2 = Start_point, 3 = Finisch_point

    levels = {
       "tilemap_level_1": "Level 1",
       "tilemap_level_2": "Level 2"
    }

    # ----------------------------------------------------------------------------- #
    
    # Map1
    tilemap_level_1 = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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

    tilemap_level_2 = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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

    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #

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
        
        if map_selected == 0:
            print("Select a level:")
            for index, level_name in enumerate(levels.values(), start=1): # Displaying the available levels
                print(f"{index}. {level_name}")
            user_input = input("Enter the level number: ") # Getting user input for level selection
            try: # Attempting to convert user input to integer
                map_selected = int(user_input)
            except ValueError: # Handling invalid input
                print("Invalid input. Please enter a number corresponding to the level.")
                continue

            if map_selected not in range(1, len(levels) + 1): # Checking if the selected level is valid
                print("Invalid level number. Please try again.")
                map_selected = 0
                continue

            else: # Loading the selected level
                print(f"Loading {levels[f'tilemap_level_{map_selected}']}...") # Confirming the selected level
                match map_selected:
                    case 1:
                        map_data = tilemap_level_1 # Selecting the map data for level 1
                        map_selected = -1 # Setting the value to -1 to indicate that a map has been selected
                    case 2:
                        map_data = tilemap_level_2
                        map_selected = -1 # Setting the value to -1 to indicate that a map has been selected

                map_instance = TileMap(map_data) # Creating a tilemap instance based on the selected map
                map_instance.tile_group.draw(screen) # Drawing the tilemap on the screen
            
        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #

        if map_selected == -1:
            ship_instance.update_thruster_inputs() # Update thruster inputs based on key presses
            ship_instance.ship_rotate() # Update ship movement based on thruster inputs
            ship_instance.move_ship() # Move the ship based on current velocity and acceleration
            position = ship_instance.get_ship_position() # Getting the ship position for map movement
            map_instance.draw_map(screen, position) # Drawing the map on the screen
            ship_instance.render_ship_maps() # Render the ship with updated rotation
            ship, ship_rect = ship_instance.get_rect() # Getting the ship image and rect for rendering
            ship_instance.debug() # Starting the debug
            screen.blit(ship, ship_rect) # Drawing the ship on the screen at the center position

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