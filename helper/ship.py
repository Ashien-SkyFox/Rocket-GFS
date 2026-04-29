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
#  {[**File**]}        ship.py
#  {[**Author**]}      Cutie Ashien
#  {[**Version**]}     5.1.0
#  {[**Date**]}        2025-11-22
#  {[**Python**]}      3.11.x
#  {[**License**]}     MIT
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  {[**Description**]}
#
#                  This module contains the ship-related functionalities of Rocket, like ship rotation, ship movement and controls.
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
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   -v5.0.1: Collision End check and start of refactoring.
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
#   -v5.0.0 Collision End check and start of refactoring.
#       - Checks if player is at the endpoint and ending the game.
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   -v4.2.1: Collision Color chek update.
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
#     - v4.0.3: Structure overhaul(ship).
#       - Moved the ship class to a separate file (ship.py).
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
import sys
from turtle import color # Import sys to modify the Python path


# Move to main directory and ensure parent directory is in sys.path
main_dir = os.path.join(os.path.dirname(__file__), '..')
os.chdir(main_dir)
if main_dir not in sys.path:
    sys.path.insert(0, main_dir)
"""
Problem: when importing files from subfolders, python couldn't find the files
Solution: I used os.path.join to create the correct path to the main directory and added it to sys.path

Explaination:
    Basically, this moves the path to the main directory of the project, so python can find all files

Step by step:
    1. I got the path of this file using os.path.dirname(__file__), then I moved one level up using os.path.join with '..'
    1.1. os.path.join needs two arguments, the first is the base path, the second is the path to join
    1.2. '..' means move one level up in the directory structure (so basicly back, or in other words we remove the last part of the path)

    2. Then I changed the current working directory to the main directory using os.chdir(main_dir)
    2.1. os.chdir changes the current working directory to the specified path

    3. Finally, I checked if the main directory is already in sys.path, if not, I added it to the start of sys.path using sys.path.insert(0, main_dir)
    3.1. sys.path.insert needs two arguments, the first is the index to insert at, the second is the value to insert
    3.2. By inserting at index 0, we say that the path should be imported at the very start of the path list, so python will look there first when importing files

Note to myself:
    I don't want do this anymore it took me way to long to figure this out... (ಥ﹏ಥ) It was round about 4 hours of trial and error and googling to find a solution.
    But well now I know how to do it :3
"""

# ------------------------------------------------------------------------------ #

### File Imports ###
import levels as levels # Importing levels module
import config as conf # Importing config module
import helper.main_menu as mm # Importing map helper module

# ------------------------------------------------------------------------------ #

### Library Imports ###
from unittest import case # For match case statements
import pygame # Importing the pygame library for game development
import math # Importing the math library for mathematical functions

# ------------------------------------------------------------------------------ #

### Config Imports ###
vector = conf.vector # Importing vector from config module
screensize_x = conf.screensize_x # Importing screen size x from config module   
screensize_y = conf.screensize_y # Importing screen size y from config module

### Ship Class ###
class Ship:
        def __init__(self):
            ##########################################################
            ##########################################################
            self.create_ship_image() # Create the ship image and mask for collision detection
            
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
            self.locktime = conf.ship_collision_locktime

            ##########################################################
            ##########################################################

            ### Game State ###
            self.game_state = "running" # Initial game state

            ### Physics Factors ###
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

            # Variables for movement update
            self.movement_speed = 0
            self.position = vector(0, 0) # Ship position
            self.velocity = vector(0, 0) # Ship velocity
            self.acceleration_vector = vector(0, 0) # Ship acceleration
            self.acceleration_vector = vector(0, 0) # Ship acceleration
            self.forward_direction = vector(0, 0)

            # Collision Varibals
            self.collision_move_upward = conf.ship_collision_move_upward
            self.collision_angle_limit = conf.ship_rotate_angle_collision
            self.rotate_to_ground_speed = conf.ship_rotate_to_ground_speed
            self.speedx_fade_fast_rate = conf.ship_speedx_fade_fast_rate
            self.overlap_pixel_color = None
            self.prev_collision_count = 0
            self.speedx_fade_fast = False
            self.movement_lock = False
            self.gravity_lock = False
            self.rotation_lock = False
            self.unsave_color = conf.unsafe_color
            self.start_point_color = conf.start_point_color
            self.end_point_color = conf.end_point_color
            self.debug_enabled = getattr(conf, 'debug_mode', False)
            self.ship_mask = None
            self.total_collision_count = 0
            self.collision_start_side_count = 0
            self.collision_unsafe_side_count = 0
            self.collision_end_side_count = 0
            self.collision_side = None
            
            # Other
            self.won_countdown_start = True

        def create_ship_image(self):
            self.ship_orginal = pygame.image.load('pictures/Rocket.png').convert_alpha()
            """
            Problems: I couldent load the image from a subfolder
            Fixed: I used os.path.join to create the correct path to the image
            """
            ships_size = ((0.1 * screensize_x) + (0.1 * screensize_y)) / 2 # Calculating the ship size based on screen size
            self.ship_orginal = pygame.transform.scale(self.ship_orginal, (ships_size, ships_size)) # Scaling the ship image based on screen size
            self.ship = self.ship_orginal # Initializing the ship image
            self.ship_mask = pygame.mask.from_surface(self.ship)
        
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
            if self.rotation_lock == False: # Only update rotation if not locked by collision
                speedup_rotate = (((self.input_thruster_outer_right * self.turn_outer_factor) + self.input_thruster_inner_right * self.turn_inner_factor) - (self.input_thruster_inner_left * self.turn_inner_factor + (self.input_thruster_outer_left * self.turn_outer_factor))) # Turning speed based on thruster input
                self.rotate_angle %= 360  # Keep the angle within [0, 360) to prevent overflow
                self.rotate_velocity += speedup_rotate * self.acceleration # Adding the speedup input multiplied by the acceleration to the rotate velocity

                self.rotate_velocity *= self.rotate_friction # Applying friction to the rotate velocity to slowly decrease it over time

                self.rotate_angle += self.rotate_velocity # Updating the rotate angle based on the rotate velocity

                self.ship = pygame.transform.rotate(self.ship_orginal, self.rotate_angle) # Rotating the ship image based on the rotate angle
                self.ship_mask = pygame.mask.from_surface(self.ship)
            else:
                if self.collision_side in ("on Start", "on End"): # Only update rotation if collision is on top and ship is upright
                    self.rotate_angle %= 360  # Keep the angle within (0, 360) to prevent overflow
                    if self.rotate_angle < 1 or self.rotate_angle > 359:
                        self.rotate_velocity = 0
                        self.rotate_angle = 0
                    else:
                        if self.rotate_angle < 90:
                            self.rotate_velocity = -(self.rotate_to_ground_speed * 0.3)
                        if self.rotate_angle > 270:
                            self.rotate_velocity = (self.rotate_to_ground_speed * 0.3)

                    self.rotate_angle += self.rotate_velocity # Updating the rotate angle based on the rotate velocity
                    self.ship = pygame.transform.rotate(self.ship_orginal, self.rotate_angle) # Rotating the ship image based on the rotate angle
                    self.ship_mask = pygame.mask.from_surface(self.ship)

        def move_ship(self, sprite_group):
            # Calculate forward direction based on current rotation
            self.temp_position = self.position.copy() # Temporary position for calculations
            self.temp_movement = vector(0, 0) # Temporary movement vector
            rad_angle = math.radians(self.rotate_angle-90) # Convert angle to radians (remove inversion if not needed)
            self.forward_direction = vector(math.cos(rad_angle), -math.sin(rad_angle)) # Calculate forward direction vector

            # Calculate total thrust from all thrusters
            self.total_thrust = 0
            self.total_thrust = -(self.input_thruster_outer_left + self.input_thruster_inner_left +
                    self.input_thruster_middle +
                    self.input_thruster_inner_right + self.input_thruster_outer_right)
            """
            Problem: the acceleration was fliped
            Solution: I was lazy and just added a negative sign in front of the total thrust calculation
            """

            # Update acceleration based on total thrust and forward direction
            max_acceleration = 2.0  # Limits ship acceleration for smoother control; adjust for desired responsiveness
            raw_acceleration = self.forward_direction * self.total_thrust * self.acceleration # Calculate raw acceleration vector
            if raw_acceleration.length() > max_acceleration: # Limit acceleration to max value
                raw_acceleration = raw_acceleration.normalize() * max_acceleration # Limit acceleration to max value
            self.acceleration_vector = raw_acceleration # Set the ship's acceleration vector

            # Update velocity and position
            self.velocity += self.acceleration_vector # Update velocity based on acceleration
            self.velocity *= 0.98  # Apply velocity damping for realism
            text_to_show, reason = self.check_collisions(sprite_group) # Check for collisions with the map
            if self.gravity_lock == False: # Only apply gravity if not locked by collision
                self.temp_movement += self.gravity # Apply gravity to temporary movement
                if self.speedx_fade_fast == True: # Apply fast horizontal speed fade on collision
                    self.velocity.x *= self.speedx_fade_fast_rate  # Faster horizontal speed fade on collision
                    if abs(self.velocity.x) < 0.1: # Threshold to stop horizontal movement
                        self.velocity.x = 0 # Stop horizontal movement
                        self.speedx_fade_fast = False # Disable fast fade once horizontal speed is negligible
            self.temp_position += self.velocity + self.temp_movement # Temporary position calculation
            self.position = self.temp_position # Update position based on velocity
            if self.debug_enabled:
                print(text_to_show, reason)
            return text_to_show, reason
            
            
        def get_ship_position(self):
            return self.position

        def get_rect(self):
            self.ship_rect = self.ship.get_rect(center = ((0.5 * screensize_x), (0.5 * screensize_y))) # Getting the rect of the ship image to center it on the screen
            return self.ship, self.ship_rect # Returning the ship image and rect for rendering
        
        def import_surface(self, surface):
            self.surface = None # clear the surface variable
            self.surface = surface # Importing the surface to get pixel color from

        def won_countdown(self):
            if self.won_countdown_start:
                start_time = pygame.time.get_ticks() # Get the current time in milliseconds
                countdown_duration = 3000 # Duration of the countdown in milliseconds (e.g., 3000ms = 3 seconds)
                self.countdown_active = True # Flag to indicate that the countdown is active
                self.end_countdown_tick = start_time + countdown_duration # Calculate the time when the countdown should end
                self.won_countdown_start = False

            while self.countdown_active:
                if pygame.time.get_ticks() >= self.end_countdown_tick:
                    self.countdown_active = False
                    print("Trigger Win")
                    self.game_state = "Win"
                    return "You Win!", "win"
                elif pygame.time.get_ticks() <= self.end_countdown_tick:
                    self.sec_till_win_remaining = (self.end_countdown_tick - pygame.time.get_ticks()) // 1000 # Calculate the remaining seconds until win
                    return f"Win in {self.sec_till_win_remaining} s", "Countdown Win"

        def reset_won_countdown(self):
            self.won_countdown_start = True
            self.countdown_active = False

        def count_collision_colors(self, ship_rect, ship_mask, sprite, sprite_mask):
            overlap_rect = ship_rect.clip(sprite.rect)
            start_count = 0
            unsafe_count = 0
            end_count = 0

            for x in range(overlap_rect.left, overlap_rect.right):
                for y in range(overlap_rect.top, overlap_rect.bottom):
                    ship_local = (x - ship_rect.left, y - ship_rect.top)
                    sprite_local = (x - sprite.rect.left, y - sprite.rect.top)
                    if not ship_mask.get_at(ship_local) or not sprite_mask.get_at(sprite_local):
                        continue

                    overlap_pixel_color = sprite.image.get_at(sprite_local)
                    if overlap_pixel_color == self.start_point_color:
                        start_count += 1
                    elif overlap_pixel_color == self.end_point_color:
                        end_count += 1
                    elif overlap_pixel_color == self.unsave_color:
                        unsafe_count += 1

            return start_count, unsafe_count, end_count

        def check_collisions(self, sprite_group):
            ship_mask = self.ship_mask or pygame.mask.from_surface(self.ship) # Create a mask for the ship
            ship_rect = self.ship.get_rect(center = ((0.5 * screensize_x), (0.5 * screensize_y))) # Getting the rect of the ship image to center it on the screen
            
            self.collision_start_side_count = 0 # Counter for collisions on the start side
            self.collision_unsafe_side_count = 0 # Counter for collisions on the unsafe side
            self.collision_end_side_count = 0 # Counter for collisions on the end side
            self.collision_side = None # Variable to store the determined collision side based on the count of each side
            touched_tiles = 0

            for sprite in sprite_group:
                if not ship_rect.colliderect(sprite.rect):
                    continue

                offset = (int(sprite.rect.x - ship_rect.x), int(sprite.rect.y - ship_rect.y)) # Calculate offset between ship and sprite
                sprite_mask = sprite.mask # Reuse the cached mask for the sprite
                collision_point = ship_mask.overlap(sprite_mask, offset) # Check for overlap point
                overlap_area = ship_mask.overlap_area(sprite_mask, offset) # Get the area of overlap
                if collision_point is None or overlap_area <= 0:
                    continue

                touched_tiles += overlap_area
                # Start/end only count as safe when the ship is landing from above and is nearly upright.
                landing_on_top = collision_point[1] > ship_mask.get_size()[1] * 0.7
                upright_enough = (abs(self.rotate_angle) <= self.collision_angle_limit or abs(360 - self.rotate_angle) <= self.collision_angle_limit)
                match sprite.tile_type:
                    case 1:
                        self.collision_unsafe_side_count += overlap_area
                    case 2:
                        if landing_on_top and upright_enough:
                            # Start tiles contain both safe and unsafe colors, so keep the cheap mask test
                            # and only do per-pixel color counting inside the real overlap area.
                            start_count, unsafe_count, _ = self.count_collision_colors(ship_rect, ship_mask, sprite, sprite_mask)
                            self.collision_start_side_count += start_count
                            self.collision_unsafe_side_count += unsafe_count
                        else:
                            self.collision_unsafe_side_count += overlap_area
                    case 3:
                        if landing_on_top and upright_enough:
                            # Finish tiles use the same split safe/unsafe layout as the start tile.
                            _, unsafe_count, end_count = self.count_collision_colors(ship_rect, ship_mask, sprite, sprite_mask)
                            self.collision_end_side_count += end_count
                            self.collision_unsafe_side_count += unsafe_count
                        else:
                            self.collision_unsafe_side_count += overlap_area

            # Unsafe overlap always wins over safe overlap on start and finish tiles.
            self.total_collision_count = self.collision_start_side_count + self.collision_unsafe_side_count + self.collision_end_side_count # Total collision count is the sum of all collision counts
            if self.total_collision_count != 0: # Only determine the collision side if there is at least one collision to prevent division by zero
                if self.collision_unsafe_side_count > 0:
                    self.collision_side = "You where not suposed to do that"
                elif self.collision_end_side_count > 0:
                    self.collision_side = "on End"
                elif self.collision_start_side_count > 0:
                    self.collision_side = "on Start"

                # Collision response
            if self.debug_enabled:
                print(f"Collision detected on {self.collision_side} side with {touched_tiles} touched tiles.")
            match self.collision_side:
                case "You where not suposed to do that":
                    if self.debug_enabled:
                        print("Collided with unsafe area")
                    return self.game_over() # Trigger game over no collision not top

                case "on Start":
                    if self.debug_enabled:
                        print("Collided with start point")
                    self.reset_won_countdown()
                    if self.velocity.y < 0 and self.total_thrust == 0:
                        self.velocity.y = 0 # Stopping downward velocity on top collision
                        self.position.y -= self.collision_move_upward # Move ship upward on top collision
                    self.gravity_lock = True # Setting the gravity lock to true on top collision
                    self.rotation_lock = True # Setting the rotation lock to true on top collision
                    if self.prev_collision_count == 0:
                        self.position.y -= self.collision_move_upward # Move ship upward on top collision
                    self.prev_collision_count = 1 # Incrementing the previous collision count to determine if the ship is already colliding in the next frame
                    self.speedx_fade_fast = True # Enabling fast horizontal speed fade on collision
                    return None, "start"

                case "on End":
                    if self.debug_enabled:
                        print("Collided with end point")
                    if self.velocity.y < 0 and self.total_thrust == 0:
                        self.velocity.y = 0 # Stopping downward velocity on top collision
                        self.position.y -= self.collision_move_upward # Move ship upward on top collision
                    self.gravity_lock = True # Setting the gravity lock to true on top collision
                    self.rotation_lock = True # Setting the rotation lock to true on top collision
                    if self.prev_collision_count == 0:
                        self.position.y -= self.collision_move_upward # Move ship upward on top collision
                    self.prev_collision_count = 1 # Incrementing the previous collision count to determine if the ship is already colliding in the next frame
                    self.speedx_fade_fast = True # Enabling fast horizontal speed fade on collision
                    return self.won_countdown() # Trigger win countdown on end collision
                    
                case None:
                    if self.debug_enabled:
                        print("No collision detected.")
                    self.reset_won_countdown()
                    self.gravity_lock = False # Releasing gravity lock if there is no collision
                    self.rotation_lock = False # Releasing rotation lock if there is no collision
                    self.prev_collision_count = 0 # Resetting the previous collision count if there is no collision
                    self.speedx_fade_fast = False # Disabling fast horizontal speed fade if there is no collision
                    return None, None

        def game_over(self):
            if self.debug_enabled:
                print("Game Over triggered")
            self.game_state = "game over" # Setting the game state to game over
            return "Game Over", "fail"

        def check_game_state(self):
            return self.game_state

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
                "acceleration_vector": self.acceleration_vector,
                "forward_direction": self.forward_direction,
                "temp_position": self.temp_position,
                "total_thrust": self.total_thrust,
                "collision_side": self.collision_side if hasattr(self, 'collision_side') else "N/A",
                "game_state": self.game_state,
                "prev_collision_count": self.prev_collision_count, 
                "gravity_lock": self.gravity_lock,
                "rotation_lock": self.rotation_lock,
                "movement_lock": self.movement_lock,
                "speedx_fade_fast": self.speedx_fade_fast,
                "collision_total_count": self.total_collision_count if hasattr(self, 'total_collision_count') else "N/A",
                "collision_start_side_count": self.collision_start_side_count if hasattr(self, 'collision_start_side_count') else "N/A",
                "collision_end_side_count": self.collision_end_side_count if hasattr(self, 'collision_end_side_count') else "N/A",
                "collision_unsafe_side_count": self.collision_unsafe_side_count if hasattr(self, 'collision_unsafe_side_count') else "N/A"
                }
            for argument, value in debug_values.items():
                print(f"{argument}: {value}")

            print("--------------------")
            print()