import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants for SHM
amplitude = 10.0  # Amplitude of motion
frequency = 1.0  # Frequency of oscillation (in Hz)
angular_frequency = 2 * np.pi * frequency

# Create a time array
t = np.linspace(0, 10, 1000)

# Function to calculate the x-position of the point at each time step
def calculate_position(t):
    return amplitude * np.cos(angular_frequency * t)

# Set up the figure and axis
fig, ax = plt.subplots()
point, = ax.plot([], [], 'bo', markersize=10)
ax.set_xlim(0, 10)
ax.set_ylim(-amplitude - 0.2, amplitude + 0.2)
ax.set_xlabel('Time')
ax.set_ylabel('Position')

# Function to update the animation frame
def update(frame):
    x = calculate_position(0.1 * frame)
    point.set_data(x, 0)
    return point,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), blit=True, repeat=True)

plt.title("Simple Harmonic Motion (SHM) Animation")
plt.show()
