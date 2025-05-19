import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import numpy as np

# Create a Tkinter window
root = tk.Tk()
root.title("Matplotlib Animation with Sliders")

# Create a Matplotlib figure
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)

# Create a time array
t = np.linspace(0, 10, 1000)

# Function to generate a sine wave
def generate_sine_wave(t, frequency, amplitude):
    return amplitude * np.sin(2 * np.pi * frequency * t)

# Set up the Matplotlib plot
line, = ax.plot(t, generate_sine_wave(t, frequency=1.0, amplitude=1.0), lw=2)
ax.set_xlim(0, 10)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')

# Function to update the animation frame
def update(frame, frequency, amplitude):
    line.set_ydata(generate_sine_wave(t, frequency, amplitude))
    return line,

# Create the Matplotlib animation
ani = FuncAnimation(fig, update, frames=range(1, 11), fargs=(1.0, 1.0), blit=True, repeat=False)

# Create a Tkinter canvas for Matplotlib to draw on
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Create sliders to control frequency and amplitude
frequency_scale = tk.Scale(root, label="Frequency", from_=0.1, to=5.0, resolution=0.1, orient="horizontal", command=lambda x: update_parameters())
amplitude_scale = tk.Scale(root, label="Amplitude", from_=0.1, to=2.0, resolution=0.1, orient="horizontal", command=lambda x: update_parameters())

frequency_scale.pack()
amplitude_scale.pack()

# Function to update the animation parameters
def update_parameters():
    frequency = float(frequency_scale.get())
    amplitude = float(amplitude_scale.get())
    ani.event_source.stop()
    ani.event_source.start()
    ani.event_source.interval = 1000 / frequency

# Function to start the animation
def start_animation():
    ani.event_source.start()

# Run the Tkinter main loop
root.mainloop()
