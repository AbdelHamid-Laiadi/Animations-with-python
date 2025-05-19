# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 23:56:17 2023

@author: HAMID
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants for SHM
amplitude = 1.0  # Amplitude of motion
frequency = 1.0  # Frequency of oscillation (in Hz)
angular_frequency = 2 * np.pi * frequency
phase = 0.0  # Phase angle (in radians)

# Create a time array
t = np.linspace(0, 10, 1000)

# Function to calculate the position of the mass at each time step
def calculate_position(t):
    return amplitude * np.sin(angular_frequency * t + phase)

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot(t, calculate_position(t), lw=2)
ax.set_xlim(0, 10)
ax.set_ylim(-amplitude, amplitude)
ax.set_xlabel('Time')
ax.set_ylabel('Position')

# Function to update the animation frame
def update(frame):
    phase_shift = 0.05 * frame
    line.set_ydata(calculate_position(t + phase_shift))
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(200), blit=True, repeat=True)

plt.title("Simple Harmonic Motion (SHM) Animation")
plt.show()
