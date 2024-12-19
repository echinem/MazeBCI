# Maze Game - Brain-Computer Interface (BCI)

## Overview

This is a **BCI-controlled maze game** implemented using **Pygame** and a dataset of simulated brainwave activity. The game allows the player to navigate through a maze by interpreting brainwave data for directional movement. The project demonstrates the integration of machine learning datasets with a real-time game engine to simulate BCI-based controls.

## Features

- **BCI Simulation**: Utilizes brainwave dataset (`emotions.csv`) to control player movement in real-time.
- **Maze Navigation**: The player collects a key and reaches the exit to win.
- **Collision Detection**: Walls block the player’s movement, simulating a realistic maze experience.
- **Threshold-Based Control**: Movement is triggered based on deviations from neutral brainwave thresholds.
- **Pygame Interface**: Built entirely with Pygame for rendering and handling game mechanics.

## Dataset

The dataset (`emotions.csv`) contains simulated brainwave activity in two dimensions. The values represent brain signal deviations that trigger movement:
- **Column 1**: Horizontal movement (X-axis).
- **Column 2**: Vertical movement (Y-axis).

## Game Mechanics

1. **Objective**:
   - Collect the key and reach the exit to win.
2. **Player Movement**:
   - Movement is controlled based on brainwave dataset values:
     - X-axis brainwave deviation triggers left/right movement.
     - Y-axis brainwave deviation triggers up/down movement.
   - Movement occurs only if deviations exceed a defined threshold.
3. **Collision Handling**:
   - The player stops on collision with maze walls, updating movement restrictions dynamically.
4. **Winning Conditions**:
   - Collect the key and reach the exit zone.

## Technologies Used

- **Python**
- **Pygame**: For game rendering and event handling.
- **CSV Data Handling**: Reads and interprets `emotions.csv` for controlling the player.

## How to Run

1. Install Python (3.x) and Pygame:
   ```bash
   pip install pygame
