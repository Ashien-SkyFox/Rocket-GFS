import pygame
import os
import time

        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #

def game_loop():
    pygame.init()

    clock = pygame.time.Clock()
    """
    Initializing pygame and creating a clock object to manage the frame rate
    """
    rotate_angle = 0
    inner_truster_ratue = 1.2
    outer_truster_ratue = 1.64
    middle_truster_ratue = 1.0
    rotate_velocity_fade = 0
    rotate_velocity_speedup = 0
    """
    Overall Varibals
    """
    screensize_x = 1800
    screensize_y = 900
    """
    Problems: If you would want to change the screen size you would have to change it in multiple places or else the pictures would not be in the ritght place
    Fixed: I created variables for the screen size and used them in the code with multiplaycations.
    """
    screen = pygame.display.set_mode((screensize_x, screensize_y))
    ship_orginal = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Pictures','Rocket.png')).convert_alpha()
    """
    Problems: I couldent load the image from a subfolder
    Fixed: I used os.path.join to create the correct path to the image
    """

    running = True
    while running:
        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #
        def ship_movement(rotate_angle,input_thruster_outer_left, input_thruster_inner_left, input_thruster_middle, input_thruster_inner_right, input_thruster_outer_right, prev_rotate_velocity_fade, prev_rotate_velocity_speedup):
            speedup_rotate = (input_thruster_outer_left + input_thruster_inner_left + input_thruster_inner_right + input_thruster_outer_right) # Turning speed based on thruster input
            if rotate_angle > 360 or rotate_angle < -360: # Resetting the rotate angle to prevent overflow
                rotate_angle = 0
            if prev_rotate_velocity_fade == 0 or speedup_rotate != 0: # If there is no fade velocity or if there is a speedup input set the fade velocity to the speedup velocity multiplied by 0.98
                rotate_velocity_fade = speedup_rotate * 0.98
            else:  # Else multiply the previous fade velocity by 0.98 to slowly decrease it over time
                rotate_velocity_fade = prev_rotate_velocity_fade * 0.98
            if rotate_velocity_fade < 0.1 and rotate_velocity_fade > -0.1: # If the fade velocity is very small set it to 0 to prevent jittering
                rotate_velocity_fade = 0


            if prev_rotate_velocity_speedup == 0 and speedup_rotate != 0: # If there is no speedup velocity and there is a speedup input set the speedup velocity to the speedup input multiplied by 0.1
                rotate_velocity_speedup = speedup_rotate * 0.1
            else: # Else add the previous speedup velocity to the speedup input multiplied by 0.1 to slowly increase it over time
                rotate_velocity_speedup = prev_rotate_velocity_speedup + speedup_rotate * 0.1
            if rotate_velocity_speedup < 0.1 and rotate_velocity_speedup > -0.1: # If the speedup velocity is very small set it to 0 to prevent jittering
                rotate_velocity_speedup = 0

            rotate_angle = rotate_angle + rotate_velocity_speedup + rotate_velocity_fade # Updating the rotate angle based on the speedup and fade velocities and previous angle
            ship = pygame.transform.rotate(ship_orginal, rotate_angle) # Rotating the ship image based on the rotate angle
            """
            Rotation of the ship image
            """
            return ship, rotate_angle, rotate_velocity_fade, rotate_velocity_speedup # Returning the updated ship image, rotate angle, fade velocity and speedup velocity
        
        def ship_controls(rotate_angle, rotate_velocity_fade, rotate_velocity_speedup):
            keys = pygame.key.get_pressed()
            input_thruster_outer_left = 0
            input_thruster_inner_left = 0
            input_thruster_middle = 0
            input_thruster_inner_right = 0
            input_thruster_outer_right = 0
            """
            These variables are used to store the input from the thrusters
            """

            if keys[pygame.K_g]:
                input_thruster_outer_left = -outer_truster_ratue
                """
                Farest left thruster
                """

            if keys[pygame.K_h]:
                input_thruster_inner_left = -inner_truster_ratue
                """
                Left thruster
                """

            if keys[pygame.K_j]:
                input_thruster_middle = middle_truster_ratue
                """
                Middle thruster
                """

            if keys[pygame.K_k]:
                input_thruster_inner_right = inner_truster_ratue
                """
                Right thruster
                """

            if keys[pygame.K_l]:
                input_thruster_outer_right = outer_truster_ratue
                """
                Farest right thruster
                """

            ship, rotate_angle, rotate_velocity_fade, rotate_velocity_speedup = ship_movement(rotate_angle, input_thruster_outer_left, input_thruster_inner_left, input_thruster_middle, input_thruster_inner_right, input_thruster_outer_right, rotate_velocity_fade, rotate_velocity_speedup)
            
            return ship, rotate_angle, input_thruster_outer_left, input_thruster_inner_left, input_thruster_middle, input_thruster_inner_right, input_thruster_outer_right, rotate_velocity_fade, rotate_velocity_speedup # Returning all the variables for the debug data
            """
            Rotating the ship based on the input angle from the thrusters
            """
        
        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            """
            For smooth closing of the window
            """
        
        
        screen.fill((0, 0, 0))
        """
        Filling the screen with black color
        """

        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #
    

        ship, rotate_angle, input_thruster_outer_left, input_thruster_inner_left, input_thruster_middle, input_thruster_inner_right, input_thruster_outer_right, rotate_velocity_fade, rotate_velocity_speedup = ship_controls(rotate_angle, rotate_velocity_fade, rotate_velocity_speedup)
        ship_rect = ship.get_rect(center = ((0.5 * screensize_x), (0.5 * screensize_y)))
        """
        Getting the rectangle of the ship and centering it on the screen for any screen size and so when it is rotated it stays in the center
        """
        screen.blit(ship, ship_rect)
        """
        Blitting the ship on the screen at the correct position (rendering a frame)
        """
        
        pygame.display.flip()
        clock.tick(60)
        """
        Updating the display and setting the frame rate to 60 FPS
        """
        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #
        
        debug = {"rotate_angle": rotate_angle,
                 "input_thruster_outer_left": input_thruster_outer_left,
                 "input_thruster_inner_left": input_thruster_inner_left,
                 "input_thruster_middle": input_thruster_middle,
                 "input_thruster_inner_right": input_thruster_inner_right,
                 "input_thruster_outer_right": input_thruster_outer_right,
                 "rotate_velocity_fade": rotate_velocity_fade,
                 "rotate_velocity_speedup": rotate_velocity_speedup,
                 }
        for argument, value in debug.items():
            print(f"{argument}: {value}")
        
        # """
        # Updating the debug data dictionary with the current values
        # """
        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #

    pygame.quit()

        # -------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------- #

game_loop()
"""
Starting the game loop
"""