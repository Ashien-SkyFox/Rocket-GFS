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
#  {[**Version**]}     7.0.0
#  {[**Date**]}        2026-07-15
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
#  -v7.0.0: Mini map
#       - Added a mini map to the game that shows the ship's position and orientation relative to the level.
#       - The mini map is displayed in the top-right corner of the screen and updates in
#
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#  -v6.1.1: Runtime dependency bootstrap.
#      - Added startup dependency check that installs missing runtime requirements automatically.
#      - Ignored build-only dependency `pyinstaller` during runtime checks.
#      - Kept game startup path unchanged after dependency verification.
#
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#  -v6.1.0: Thruster effects raw.
#      - Integrated ship thruster effect rendering into the main gameplay draw loop.
#      - Synced in-file documentation with the new five-thruster visual behavior.
#
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#  -v6.0.0: Full release of the game with all features and levels.
#      - Added multiple levels with increasing difficulty and unique objectives.
#      - Implemented a highscore system to track player performance across levels.
#      - Added a main menu with level selection and highscore display.
#      - Improved graphics and visual effects for a more immersive experience.
#
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#  -v5.1.4: Winn condition fix.
#      - Added a fix to the win condition check in the ship class to handle cases where there is no objective instance, allowing for levels without specific objectives to be completed successfully.
#
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#  - v5.1.3: Objective system update.
#      - Half rework of objective system
#
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

### Library Imports ###
from unittest import case # For match case statements
import datetime
from importlib import metadata as importlib_metadata
import json
import math # Importing the math library for mathematical functions
import os # Importing the os library for file path operations
import random
import re
import subprocess
import sys
import time # Importing the time library for time-related functions
import traceback


def get_runtime_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))


def read_runtime_requirements(requirements_path):
    if not os.path.exists(requirements_path):
        return []

    requirements = []
    with open(requirements_path, "r", encoding="utf-8") as req_file:
        for raw_line in req_file:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            requirements.append(line)
    return requirements


def extract_distribution_name(requirement_line):
    base = requirement_line.split(";", 1)[0].strip()
    base = re.split(r"[<>=!~]", base, maxsplit=1)[0].strip()
    base = base.split("[", 1)[0].strip()
    return base


def find_missing_requirements(requirements):
    missing = []
    # pyinstaller is a build-time dependency and not required to run the game.
    runtime_ignore = {"pyinstaller"}

    for requirement in requirements:
        package_name = extract_distribution_name(requirement)
        if not package_name:
            continue
        if package_name.lower() in runtime_ignore:
            continue
        try:
            importlib_metadata.version(package_name)
        except importlib_metadata.PackageNotFoundError:
            missing.append(requirement)
    return missing


def ensure_runtime_requirements_installed():
    if getattr(sys, "frozen", False):
        return

    base_dir = get_runtime_base_dir()
    requirements_path = os.path.join(base_dir, "requirements.txt")
    requirements = read_runtime_requirements(requirements_path)
    missing_requirements = find_missing_requirements(requirements)

    if not missing_requirements:
        return

    print("Missing dependencies detected. Installing requirements...")
    install_command = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "--only-binary=:all:",
        "-r",
        requirements_path,
    ]
    result = subprocess.run(install_command, check=False)
    if result.returncode != 0:
        raise RuntimeError("Failed to install missing requirements.")


ensure_runtime_requirements_installed()


### File Imports ###
import levels as levels # Importing levels module
import config as conf # Importing config module
import helper.main_menu as mm # Importing map helper module
import helper.ship as sh # Importing ship helper module
import helper.map as mp # Importing map helper module
import helper.objectives as obj # Importing objectives module

import pygame # Importing the pygame library for game development

# ------------------------------------------------------------------------------ #

### json Imports ###
HIGHSCORE_FILE = "highscore.json"


def get_default_highscore_data():
    return {
        "total_points": 0,
        "wins": 0,
        "level_points": {}
    }


def load_highscore_data():
    if not os.path.exists(HIGHSCORE_FILE):
        return get_default_highscore_data()

    try:
        with open(HIGHSCORE_FILE, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        return get_default_highscore_data()

    if not isinstance(data, dict):
        return get_default_highscore_data()

    normalized = get_default_highscore_data()
    normalized["total_points"] = int(data.get("total_points", 0)) if isinstance(data.get("total_points", 0), (int, float)) else 0
    normalized["wins"] = int(data.get("wins", 0)) if isinstance(data.get("wins", 0), (int, float)) else 0
    level_points = data.get("level_points", {})
    if not isinstance(level_points, dict):
        level_points = {}

    normalized["level_points"] = {str(k): int(v) for k, v in level_points.items() if isinstance(v, (int, float))}
    return normalized


def save_highscore_data(highscore_data):
    try:
        with open(HIGHSCORE_FILE, "w", encoding="utf-8") as json_file:
            json.dump(highscore_data, json_file, indent=4)
    except OSError:
        print("Failed to save highscore data.")


def get_highscore_text(highscore_data):
    total_points = int(highscore_data.get("total_points", 0))
    return f"Total Points: {total_points}"


def calculate_points_for_run(completion_time_seconds):
    # Faster completion gives more points; minimum is 0 points.
    return max(0, int(10000 - (completion_time_seconds * 100)))


def update_highscore_for_win(highscore_data, level_number, completion_time_seconds):
    if completion_time_seconds <= 0:
        return False

    points = calculate_points_for_run(completion_time_seconds)
    changed = False
    levels = highscore_data.setdefault("level_points", {})
    level_key = str(level_number)
    old_level_best = int(levels.get(level_key, 0))
    if points > old_level_best:
        levels[level_key] = points
        changed = True

    highscore_data["total_points"] = int(sum(int(v) for v in levels.values()))

    highscore_data["wins"] = int(highscore_data.get("wins", 0)) + 1
    return changed

# ------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------ #

highscore = "Total Points: 0"

## ------------------------------------------------------------------------------ #

screensize_x = conf.screensize_x
screensize_y = conf.screensize_y
vector = conf.vector


def apply_runtime_screen_size(new_width, new_height):
    global screensize_x, screensize_y
    screensize_x = int(new_width)
    screensize_y = int(new_height)
    conf.screensize_x = screensize_x
    conf.screensize_y = screensize_y
    conf.map_tile_size = (
        int((conf.map_sizing_factor * screensize_x) + (conf.map_sizing_factor * screensize_y)) / 2,
        int((conf.map_sizing_factor * screensize_x) + (conf.map_sizing_factor * screensize_y)) / 2
    )
    sh.screensize_x = screensize_x
    sh.screensize_y = screensize_y
    mp.screensize_x = screensize_x
    mp.screensize_y = screensize_y


def create_window(window_size):
    return pygame.display.set_mode(window_size, pygame.RESIZABLE)


def get_window_position_safe():
    if hasattr(pygame.display, "get_window_position"):
        try:
            return pygame.display.get_window_position()
        except Exception:
            return None
    return None


def set_window_position_safe(x, y):
    if hasattr(pygame.display, "set_window_position"):
        try:
            pygame.display.set_window_position(int(x), int(y))
        except Exception:
            pass


def preserve_ship_world_on_resize(ship_instance, old_tile_spacing, new_tile_spacing):
    if old_tile_spacing <= 0 or new_tile_spacing <= 0:
        return

    tile_position = vector(ship_instance.position.x / old_tile_spacing, ship_instance.position.y / old_tile_spacing)
    tile_velocity = vector(ship_instance.velocity.x / old_tile_spacing, ship_instance.velocity.y / old_tile_spacing)

    ship_instance.position = vector(tile_position.x * new_tile_spacing, tile_position.y * new_tile_spacing)
    ship_instance.velocity = vector(tile_velocity.x * new_tile_spacing, tile_velocity.y * new_tile_spacing)
    ship_instance.acceleration_vector = vector(0, 0)
    if hasattr(ship_instance, "temp_position"):
        ship_instance.temp_position = ship_instance.position.copy()


def apply_window_resize(screen, new_size, ship_instance, map_selected, map_instance, resize_grace_frames):
    screen = create_window(new_size)
    apply_runtime_screen_size(*new_size)
    ship_instance.update_screen_size(*new_size)
    if map_selected == -1 and map_instance is not None:
        old_tile_spacing = map_instance.tile_spacing
        map_instance.update_screen_size(*new_size)
        preserve_ship_world_on_resize(ship_instance, old_tile_spacing, map_instance.tile_spacing)
        resize_grace_frames = 4
    return screen, resize_grace_frames


def draw_navigation_arrow(screen, ship_position, target_position):
    if target_position is None:
        return

    direction = vector(target_position) - vector(ship_position)
    if direction.length_squared() <= 0.0001:
        return

    angle = math.atan2(direction.y, direction.x)
    arrow_origin = vector(screensize_x * 0.5, 40)
    base_points = [vector(18, 0), vector(-10, -8), vector(-10, 8)]
    rotated_points = []
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    for point in base_points:
        rotated_x = point.x * cos_a - point.y * sin_a
        rotated_y = point.x * sin_a + point.y * cos_a
        rotated_points.append((arrow_origin.x + rotated_x, arrow_origin.y + rotated_y))

    pygame.draw.circle(screen, (25, 25, 25), (int(arrow_origin.x), int(arrow_origin.y)), 16)
    pygame.draw.polygon(screen, (255, 230, 0), rotated_points)
    pygame.draw.circle(screen, (20, 20, 20), (int(arrow_origin.x), int(arrow_origin.y)), 16, 2)


def load_star_background_surface():
    try:
        star_surface = pygame.image.load(conf.star_glitter_background).convert_alpha()
        star_scale = float(getattr(conf, "background_star_scale", 1.0))
        star_scale = max(0.05, min(2.0, star_scale))
        scaled_size = (
            max(1, int(star_surface.get_width() * star_scale)),
            max(1, int(star_surface.get_height() * star_scale))
        )
        return pygame.transform.smoothscale(star_surface, scaled_size)
    except (FileNotFoundError, pygame.error):
        return None


def build_random_starfield(star_surface, width, height):
    if star_surface is None:
        return None

    world_width = max(width * 3, 1)
    world_height = max(height * 3, 1)
    base_count = max(80, int((width * height) / 12000))
    stars = []
    for _ in range(base_count):
        stars.append((
            random.uniform(0, world_width),
            random.uniform(0, world_height),
            random.uniform(0.45, 1.0)
        ))

    return {
        "world_width": world_width,
        "world_height": world_height,
        "stars": stars
    }


def draw_moving_background(screen, star_surface, starfield_data, offset_x, offset_y):
    if star_surface is None or starfield_data is None:
        screen.fill((0, 0, 0))
        return

    world_width = starfield_data["world_width"]
    world_height = starfield_data["world_height"]
    stars = starfield_data["stars"]
    if world_width <= 0 or world_height <= 0 or not stars:
        screen.fill((0, 0, 0))
        return

    screen.fill((0, 0, 0))

    for star_x, star_y, star_brightness in stars:
        screen_x = (star_x - offset_x) % world_width
        screen_y = (star_y - offset_y) % world_height

        if screen_x > screensize_x or screen_y > screensize_y:
            continue

        alpha_min = int(getattr(conf, "background_star_alpha_min", 25))
        alpha_max = int(getattr(conf, "background_star_alpha_max", 110))
        alpha_min = max(0, min(255, alpha_min))
        alpha_max = max(alpha_min, min(255, alpha_max))
        star_alpha = alpha_min + int((alpha_max - alpha_min) * star_brightness)
        star_surface.set_alpha(star_alpha)
        screen.blit(star_surface, (screen_x, screen_y))

### Game Loop ###

def game_loop():
    pygame.display.set_caption("Rocket - v7 (Minimap)") # Setting the window title
    pygame.init()

    highscore_data = load_highscore_data()

    map_selected = 0 # 0 = main menu, -1 = map loaded
    display_info = pygame.display.Info()
    default_window_size = (max(800, int(display_info.current_w * 0.75)), max(450, int(display_info.current_h * 0.75)))
    windowed_size = default_window_size
    bordered_fullscreen = False
    previous_window_position = None
    screen = create_window(default_window_size) # set the screen size
    apply_runtime_screen_size(*screen.get_size())
    clock = pygame.time.Clock() # Creating a clock object to manage the frame rate
    star_background_surface = load_star_background_surface()
    starfield_data = build_random_starfield(star_background_surface, screensize_x, screensize_y)

    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #

    map_data = levels.get_level_info() # Loading the level data from the levels module
    main_menu_instance = mm.MainMenu(
        map_data,
        map_selected,
        get_highscore_text(highscore_data),
        highscore_data.get("level_points", {})
    )
    ship_instance = sh.Ship()
    running = True
    reset_ship = False
    delta_time = 0.
    resize_grace_frames = 0
    ignore_resize_events = 0
    current_level = None
    level_start_ticks = None

    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #

    def start_game_loop(running=running, map_selected=map_selected, reset_ship=reset_ship, ship_instance=ship_instance, main_menu_instance=main_menu_instance, delta_time=delta_time, map_data=map_data):
        nonlocal screen, windowed_size, bordered_fullscreen, resize_grace_frames, ignore_resize_events, previous_window_position, current_level, level_start_ticks, starfield_data
        map_instance = None
        while running:
            for event in pygame.event.get(): # Quiting the game loop if the window is closed
                if event.type == pygame.QUIT: 
                    running = False 
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    if not bordered_fullscreen:
                        previous_window_position = get_window_position_safe()
                        windowed_size = screen.get_size()
                        desktop_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
                        screen, resize_grace_frames = apply_window_resize(
                            screen,
                            desktop_size,
                            ship_instance,
                            map_selected,
                            map_instance,
                            resize_grace_frames
                        )
                        starfield_data = build_random_starfield(star_background_surface, screensize_x, screensize_y)
                        set_window_position_safe(0, 0)
                        bordered_fullscreen = True
                    else:
                        screen, resize_grace_frames = apply_window_resize(
                            screen,
                            windowed_size,
                            ship_instance,
                            map_selected,
                            map_instance,
                            resize_grace_frames
                        )
                        starfield_data = build_random_starfield(star_background_surface, screensize_x, screensize_y)
                        if previous_window_position is not None:
                            set_window_position_safe(previous_window_position[0], previous_window_position[1])
                        bordered_fullscreen = False
                    ignore_resize_events = 2
                elif event.type == pygame.VIDEORESIZE and not bordered_fullscreen:
                    if ignore_resize_events > 0:
                        ignore_resize_events -= 1
                        continue
                    resized_width = max(800, event.w)
                    resized_height = max(450, event.h)
                    windowed_size = (resized_width, resized_height)
                    screen, resize_grace_frames = apply_window_resize(
                        screen,
                        windowed_size,
                        ship_instance,
                        map_selected,
                        map_instance,
                        resize_grace_frames
                    )
                    starfield_data = build_random_starfield(star_background_surface, screensize_x, screensize_y)

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #

            parallax_reference_position = vector(0, 0)
            if map_selected == -1:
                parallax_reference_position = ship_instance.get_ship_position()

            parallax_factor = float(getattr(conf, "background_parallax_factor", 0.2))
            # Positive parallax offsets make the tiled background move opposite to ship motion.
            parallax_offset_x = parallax_reference_position.x * parallax_factor
            parallax_offset_y = parallax_reference_position.y * parallax_factor
            draw_moving_background(screen, star_background_surface, starfield_data, parallax_offset_x, parallax_offset_y)

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #

            if reset_ship == True: # deliting and recreating the ship instance to reset all values
                ship_instance = sh.Ship()
                reset_ship = False

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #

            if map_selected == 0:
                map = main_menu_instance.main_menu_loop(screen) # Displaying the main menu
                if map in map_data[0]: # Checking if the selected map is valid
                    main_menu_instance.map_loading_animation(screen) # Displaying the map loading animation
                    map_instance = mp.TileMap(map_data, map) # Creating a tilemap instance based on the selected map
                    ship_instance = sh.Ship(map_instance)
                    ship, ship_rect = ship_instance.get_rect()
                    spawn_position = map_instance.get_location_of_spawn_point(ship_rect) # Getting the spawn position from the tilemap
                    ship_instance.position = spawn_position # Setting the ship position to the spawn position
                    map_instance.tile_group.draw(screen) # Drawing the tilemap on the screen
                    map_selected = -1 # Setting the value to -1 to indicate that a map has been selected
                    current_level = map
                    level_start_ticks = pygame.time.get_ticks()
                    start_select = 1 # Resetting the start select variable for the next time the main menu is shown
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
                    if resize_grace_frames > 0:
                        resize_grace_frames -= 1
                        ship_instance.velocity = vector(0, 0)
                        ship_instance.acceleration_vector = vector(0, 0)
                        text_to_show, reason = None, None
                    else:
                        text_to_show, reason = ship_instance.move_ship(spirit_collision_group) # Move the ship based on current velocity and acceleration
                    ship_instance.render_ship_maps() # Render the ship with updated rotation
                    game_state = ship_instance.check_game_state() # Check for game over or level completion
                    ship, ship_rect = ship_instance.get_rect() # Getting the ship image and rect for rendering
                    if conf.debug_mode:
                        ship_instance.debug() # Starting the debug
                    ship_instance.draw_thruster_effects(screen, ship_rect) # Draw thruster flames before blitting ship
                    screen.blit(ship, ship_rect) # Drawing the ship on the screen at the center position
                    navigation_target = map_instance.get_navigation_target_position()
                    draw_navigation_arrow(screen, position, navigation_target)
                    if text_to_show is not None:
                        font = pygame.font.SysFont(None, 74) # Creating a font object for rendering text
                        if reason is not None and reason == "not relevant":
                            text_to_show_font = font.render(text_to_show, True, (255, 0, 255))
                            screen.blit(text_to_show_font, (screensize_x // 2 - text_to_show_font.get_width() // 2, screensize_y // 2 - text_to_show_font.get_height() // 2)) # Blits the needed text
                        elif reason is not None and reason == "Countdown Win":
                            text_to_show_font = font.render(text_to_show, True, (255, 0, 255))
                            screen.blit(text_to_show_font, (screensize_x // 2 - text_to_show_font.get_width() // 2, screensize_y // 2 - text_to_show_font.get_height() // 2)) # Blits the needed text
                        elif reason is not None:
                            text_to_show_font = font.render(text_to_show, True, (255, 0, 255))
                            screen.blit(text_to_show_font, (screensize_x // 2 - text_to_show_font.get_width() // 2, screensize_y // 2 - text_to_show_font.get_height() // 2)) # Blits the needed text
                            pygame.display.flip() # Updating the display to show the new frame
                            pygame.time.delay(1000) # Delay for a second before resetting
                            if game_state == "game over" or game_state == "Win":
                                if game_state == "Win" and level_start_ticks is not None and current_level is not None:
                                    completion_time_seconds = (pygame.time.get_ticks() - level_start_ticks) / 1000.0
                                    update_highscore_for_win(highscore_data, current_level, completion_time_seconds)
                                    save_highscore_data(highscore_data)
                                    main_menu_instance.highscore = get_highscore_text(highscore_data)
                                    main_menu_instance.level_scores = highscore_data.get("level_points", {})
                                screen.fill((0, 0, 0)) # Filling the screen with black color to clear previous frame
                                map_selected = 0 # Returning to main menu
                                map = 0 # Resetting map variable
                                current_level = None
                                level_start_ticks = None
                                reset_ship = True # Resetting the ship
                                main_menu_instance.main_menu_reset() # Resetting the main menu instance
                        else:
                            print("===============================")
                            print("===============================")
                            print("ERROR")
                            print("===============================")
                            print("===============================")
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
                    Well refactored some parts and now know how its working again
                    -v5.1.2
                    """

            # -------------------------------------------------------------------------------- #
            # -------------------------------------------------------------------------------- #
            
            pygame.display.flip() # Updating the display to show the new frame
            delta_time = clock.tick(60) / 1000.0 # Limiting the frame rate to 30 FPS and calculating delta time for movement calculations

    # -------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------- #

    start_game_loop()
    pygame.quit()

def write_crash_log(exc: BaseException):
    """Write a timestamped crash log to the crashes/ folder."""
    try:
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        crash_dir = os.path.join(base_dir, "crashes")
        os.makedirs(crash_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        crash_file = os.path.join(crash_dir, f"crash_{timestamp}.txt")
        with open(crash_file, "w", encoding="utf-8") as f:
            f.write(f"Rocket Crash Log\n")
            f.write(f"Time: {timestamp}\n")
            f.write(f"Python: {sys.version}\n")
            f.write(f"Platform: {sys.platform}\n")
            f.write("-" * 60 + "\n")
            f.write(traceback.format_exc())
        print(f"Crash log saved to: {crash_file}")
    except Exception:
        pass


try:
    game_loop()
except (SystemExit, KeyboardInterrupt):
    pass
except Exception as _crash_exc:
    write_crash_log(_crash_exc)
    raise
"""
Starting the game loop
"""