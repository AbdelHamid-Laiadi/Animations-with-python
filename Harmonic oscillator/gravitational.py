# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 00:29:55 2023

This script simulates and animates the vertical motion of a free-falling object under gravity.

1. It calculates the time of flight for an object dropped from a given height using basic physics formulas.
2. It generates position data over time using the equation h(t) = h0 - 0.5 * g * t².
3. It visualizes the falling motion with a matplotlib animation showing height vs. time.


@author: HAMID
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants for gravitational motion
initial_height = 100.0  # Initial height (meters)
gravity = 1.81  # Acceleration due to gravity (m/s^2)

# Calculate time of flight
time_of_flight = np.sqrt((2 * initial_height) / gravity)

# Create time array
t = np.linspace(0, time_of_flight, 1000)

# Function to calculate the position of the falling object at each time step
def calculate_position(t):
    return initial_height - 0.5 * gravity * t**2

# Set up the figure and axis
fig, ax = plt.subplots()
point, = ax.plot([], [], 'bo', markersize=10)
ax.set_xlim(0, time_of_flight)
ax.set_ylim(0, initial_height)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Height (m)')

# Function to update the animation frame
def update(frame):
    y = calculate_position(0.1 * frame)
    point.set_data(0.1 * frame, y)
    return point,

# Create the animation
ani = FuncAnimation(fig, update, frames=int(10 * time_of_flight), blit=True, repeat=False)

plt.title("Gravitational Motion Animation")
plt.show()
