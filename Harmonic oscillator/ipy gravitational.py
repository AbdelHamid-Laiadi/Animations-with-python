import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import ipywidgets as widgets
from ipywidgets import interact

# Create a time array
t = np.linspace(0, 10, 1000)

# Function to generate a sine wave
def generate_sine_wave(t, frequency):
    return np.sin(2 * np.pi * frequency * t)

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot(t, generate_sine_wave(t, frequency=1.0), lw=2)
ax.set_xlim(0, 10)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')

# Function to update the animation frame
def update(frequency):
    line.set_ydata(generate_sine_wave(t, frequency))
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(1, 10, 100), blit=True, repeat=False)

# Function to interactively adjust the frequency
@interact(frequency=widgets.FloatSlider(min=0.1, max=5.0, step=0.1, value=1.0, description='Frequency'))
def update_frequency(frequency):
    ani.event_source.stop()  # Stop the animation
    update(frequency)  # Update the frequency
    ani.event_source.start()  # Restart the animation

plt.title("Interactive Sine Wave Animation")
plt.show()
