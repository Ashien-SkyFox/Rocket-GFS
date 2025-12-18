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
#  {[**Author**]}      Ashien the Skyfox
#  {[**Version**]}     4.0.1
#  {[**Date**]}        2025-11-07
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
# Written by Ashien the Skyfox (https://github.com/Ashien-SkyFox)
##################################################################################################################################################################################################################

### File Imports ###
import levels as levels # Importing levels module
import config as conf # Importing config module

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


def game_loop():
    pygame.display.set_caption("Rocket - v4.0.1") # Setting the window title
    pygame.init()

    map_selected = 0
    vector = pygame.math.Vector2

    screen = pygame.display.set_mode((screensize_x, screensize_y)) # set the screen size

    clock = pygame.time.Clock() # Creating a clock object to manage the frame rate

    class Ship:
        def __init__(self):
            ##########################################################
            ##########################################################

            ##### Ajustable Favtors #####
            # Importing Thruster key bindings from config.py
            self.thruster_key_outer_left = conf.ship_thruster_key_outer_left
            self.thruster_key_inner_left = conf.ship_thruster_key_inner_left
            self.thruster_key_middle = conf.ship_thruster_key_middle
            self.thruster_key_inner_right = conf.ship_thruster_key_inner_right
            self.thruster_key_outer_right = conf.ship_thruster_key_outer_right

            # Importing Thruster ratios from config.py
            self.inner_thruster_ratio = conf.ship_inner_thruster_ratio
            self.outer_thruster_ratio = conf.ship_outer_thruster_ratio
            self.middle_thruster_ratio = conf.ship_middle_thruster_ratio
            self.turn_outer_factor = conf.ship_turn_outer_factor
            self.turn_inner_factor = conf.ship_turn_inner_factor

            # Importing Gravity settings from config.py
            self.gravity = conf.ship_gravity

            ##########################################################
            ##########################################################

            # Importing Rotation and movement factors from config.py
            self.acceleration = conf.ship_acceleration
            self.rotate_friction = conf.ship_rotate_friction

            ### Game Variables ###
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
            self.ship_orginal = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pictures','Rocket.png')).convert_alpha()
            """
            Problems: I couldent load the image from a subfolder
            Fixed: I used os.path.join to create the correct path to the image
            """
            ships_size = ((0.1 * screensize_x) + (0.1 * screensize_y)) / 2 # Calculating the ship size based on screen size
            self.ship_orginal = pygame.transform.scale(self.ship_orginal, (ships_size, ships_size)) # Scaling the ship image based on screen size
            self.ship = self.ship_orginal # Initializing the ship image
        
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
                self.input_thruster_outer_left = self.outer_thruster_ratio

            if keys[self.thruster_key_inner_left]: #Update thruster Inner Left
                self.input_thruster_inner_left = self.inner_thruster_ratio

            if keys[self.thruster_key_middle]: #Update thruster Middle
                self.input_thruster_middle = self.middle_thruster_ratio

            if keys[self.thruster_key_inner_right]: #Update thruster Inner Right
                self.input_thruster_inner_right = self.inner_thruster_ratio

            if keys[self.thruster_key_outer_right]: #Update thruster Outer Right
                self.input_thruster_outer_right = self.outer_thruster_ratio

        def ship_rotate(self):
            speedup_rotate = (((self.input_thruster_outer_right * self.turn_outer_factor) + self.input_thruster_inner_right * self.turn_inner_factor) - (self.input_thruster_inner_left * self.turn_inner_factor + (self.input_thruster_outer_left * self.turn_outer_factor))) # Turning speed based on thruster input
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
            self.position += self.velocity + self.gravity
            
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
            # Tile size and spacing
            self.sizing_factor = 0.3 # Used for tile size calculation
            self.tile_spacing = int(((self.sizing_factor * screensize_x) / 2) + ((self.sizing_factor * screensize_y) / 2))  # Calculating tile spacing based on screen size
            self.tile_size = (int((self.sizing_factor * screensize_x) + (self.sizing_factor * screensize_y)) / 2, int((self.sizing_factor * screensize_x) + (self.sizing_factor * screensize_y)) / 2) # Calculating the tile size based on screen size

            # Load tile images
            self.wall_tile = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pictures', 'tiles', 'Basic_wall.png')).convert_alpha() # Loading tile images
            self.start_point_tile = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pictures', 'tiles', 'Start_point.png')).convert_alpha() # Loading tile images
            self.finish_point_tile = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pictures', 'tiles', 'Finisch_point.png')).convert_alpha() # Loading tile images

            # Store map data
            self.map_data = map_data # Storing the map data
            self.width = len(map_data[0]) * self.tile_size[0] # Calculating the width of the map based on the number of columns and tile size
            self.height = len(map_data) * self.tile_size[1] # Calculating the height of the map based on the number of rows and tile size
            self.tile_group = pygame.sprite.Group() # Group to hold all tile sprites
            self.create_tiles() # Creating the tile sprites

            

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
            offset_x = self.location.x
            offset_y = self.location.y
            for row_index, row in enumerate(self.scaled_tile_images):
                for col_index, tile_image in enumerate(row):
                    if tile_image:
                        x = col_index * self.tile_spacing + offset_x
                        y = row_index * self.tile_spacing + offset_y
                        screen.blit(tile_image, (x, y))

        def get_location_of_spawn_point(self, ship_rect):
            for row_index, row in enumerate(self.map_data):
                for col_index, tile_type in enumerate(row):
                    if tile_type == 2: # Start point tile
                        x = col_index * self.tile_size[0] + (50 / (0.2 / self.sizing_factor)) + (ship_rect.width / (0.3 / self.sizing_factor))
                        y = row_index * self.tile_size[1]
                        return vector(x, y)
            return vector(0, 0) # Default to (0, 0) if no start point found
        


    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #

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
    

    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #

    main_menu_instance = main_menu(map_selected, highscore)
    ship_instance = Ship()
    ship_orginal = ship_instance.create_ship_image()
    running = True
    def start_game_loop(running=running, map_selected=map_selected):
        while running:
            for event in pygame.event.get(): # Quiting the game loop if the window is closed
                if event.type == pygame.QUIT: 
                    running = False 

            # -------------------------------------------------------------------------------- #

            screen.fill((0, 0, 0)) # Filling the screen with black color to clear previous frame

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #
            if map_selected == 0:
                map = main_menu_instance.main_menu_loop(screen) # Displaying the main menu
                if map in [1, 2]: # If a map is selected

                    main_menu_instance.map_loading_animation(screen) # Displaying the map loading animation
                    map_instance = TileMap(levels.grapp_level(map)) # Creating a tilemap instance based on the selected map
                    ship, ship_rect = ship_instance.get_rect()
                    spawn_position = map_instance.get_location_of_spawn_point(ship_rect) # Getting the spawn position from the tilemap
                    ship_instance.position = spawn_position # Setting the ship position to the spawn position
                    map_instance.tile_group.draw(screen) # Drawing the tilemap on the screen
                    map_selected = -1 # Setting the value to -1 to indicate that a map has been selected

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

    start_game_loop()
    pygame.quit()

game_loop()
"""
Starting the game loop
"""