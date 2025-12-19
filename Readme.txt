#################################################################################################################################################################################################################
================================================================================================================================================================================================================
  ██████╗ ██╗   ██╗      █████╗ ███████╗██╗  ██╗██╗███████╗███╗   ██╗
  ██╔══██╗╚██╗ ██╔╝     ██╔══██╗██╔════╝██║  ██║██║██╔════╝████╗  ██║
  ██████╔╝ ╚████╔╝      ███████║███████╗███████║██║█████╗  ██╔██╗ ██║
  ██╔══██╗  ╚██╔╝       ██╔══██║╚════██║██╔══██║██║██╔══╝  ██║╚██╗██║
  ██████╔╝   ██║        ██║  ██║███████║██║  ██║██║███████╗██║ ╚████║
  ╚═════╝    ╚═╝        ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝
================================================================================================================================================================================================================
 {[**Project**]}     Rocket
 {[**File**]}        ////
 {[**Author**]}      Ashien the Skyfox
 {[**Version**]}     4.2.4
 {[**Date**]}        2025-11-20
 {[**Python**]}      3.11.x
 {[**License**]}     MIT
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 {[**Description**]}

     The code is a pygame-based simulation of a rocket coup ship.
     You have five thrusters that you can control using the G, H, J, K, and L keys to rotate the ship and move it forward.
     The ship's rotation is influenced by thruster inputs, with fade and speedup factors to simulate somwhat realistic movement.
     The ship is rendered at the center of the screen, and the game runs at 60 frames per second.
     The code is structured to allow easy adjustments of thruster ratios and movement factors.
     Debugging information can be printed to the console to monitor the ship's state.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 {[**Purpose**]}

     The Project is an educational project to learn more about programming and game development.
     The purpose of this code is to create a simple simulation of a rocket ship that can be controlled using keyboard inputs.
     The code is designed to be modular and easy to understand, allowing for future enhancements and modifications or also for educational purposes.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 {[**Changelog**]}

  -v4.2.1: Collision Color chek update.
      - Added ability to chek the overlapping pixel for collor

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  - v4.2.0: Collision update.
      - Implemented collision detection and handling in the ship movement logic.
      - Added game state management for running and game over states.
      - Added funtionality to reset the ship and main menu after game over.
      - Added logic to set the game stat to game over if the collison is not on the top of a block.
      - Added an reset funktion to the main menu instance to reset it after game over.
      - Added config valibals for collision locktime, collision fall off and upward movement on collision.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v4.1.1: Minor bug fixes and improvements.
      - Fixed minor bugs related to level selection functions.
      - Improved code readability and maintainability.
      - Fixed bug that the Ship wouldn't spawn at the center start point in certain situations.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v4.1.0: Fluid map selection update.
      - Improved map selection logic for changinging map count dynamically.
      - rewrote the functions that show the map selection to support dynamic map count.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v4.0.4: Structure overhaul(map).
      - Moved the map class to a separate file (map.py).

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v4.0.3: Structure overhaul(ship).
      - Moved the ship class to a separate file (ship.py).

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v4.0.2: Structure overhaul(main menu).
      - Moved the main menu class to a separate file (main_menu.py).

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v4.0.1: Structure overhaul(config).
      - Moved the config values to a separate config file (config.py).

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v4.0.0: Structure overhaul and level management update.
      - Added Files: config.py, levels.py, helper/map.py, helper/ship.py, helper/main_menu.py
      - Moved the tilemap to a separate level file (level.py).

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v3.1.0: Main menu and level selection update.
      - Added a main menu with level selection functionality.
      - Implemented a loading animation when switching levels.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v3.0.2: Center ship start adjustment.
      - Adjusted the calculation of center_ship_start for better alignment-
      - Added contability with different tile sizes.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v3.0.1: Tilemap spacing and sizing & Gravity update.
      - Adjusted tile spacing and sizing based on screen size for better visual consistency.
      - Added gravity variable to the Ship class for easier adjustment.
      - Added gravity effect to the ship's movement for more realistic physics.
      - Improved overall code structure and readability.
      - Fixed minor bugs related to ship movement and rendering.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v3.0.0: Map and movment update.
      - Added a tilemap system for level design.
      - Implemented map movement based on ship position.
      - Adjusted tile size based on screen size.
      - Improved overall code structure and readability.
      - Fixed minor bugs related to ship movement and rendering.
      - Added levle selection functionality.
      - Updated debug function to include new variables.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v2.1.0: Minor overhaul to ship rotation logic.
      - Simplified rotation velocity calculation.
      - Removed unnecessary variables related to rotation fade and speedup.
      - Improved code readability by removing redundant comments.
      - Updated debug function to include new variables.
      - Fixed minor rotation buggs.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v2.0.0: Major overhaul of the code structure and functionality.
      - Improved thruster input handling and ship rotation logic.
      - Added adjustable factors for thruster ratios and movement dynamics.
      - Enhanced code readability and maintainability.
      - Fixed image loading path issue.
      - Added comments and documentation for clarity.
      - Added class structure for better organization.
      - Major overhaul of the debug functionality.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    - v1.0.0: Initial release of the rocket ship simulation.
      - Basic thruster controls and ship rotation implemented.
      - Simple rendering of the ship at the center of the screen.
      - Basic game loop with event handling and frame rate control.
      - Initial debugging functionality added.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 ⚙️  Notes:

     - required assets in the 'Pictures' folder.
     - Requires pygame >= 2.5.0
     - Run `main.py` to start the game

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 ⚙️  Side notes:

     - This code was created as part of an educational project at the GWS Bühl.
     - The code originally was written in 2025 and has been updated and improved over time.
     - The code is open-source and available on GitHub for educational purposes.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The code is clearly labeled using comments so you can
easily navigate through it and understand its structure and functionality.
Enjoy coding! :3
================================================================================================================================================================================================================
Written by Ashien the Skyfox (https://github.com/Ashien-SkyFox)
#################################################################################################################################################################################################################
