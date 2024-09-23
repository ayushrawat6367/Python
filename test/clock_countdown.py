import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
from matplotlib.patches import Circle, FancyBboxPatch

# Function to draw the clock hands and update them based on remaining time
def update_clock(num, ax, countdown_time):
    ax.clear()

    # Calculate remaining time
    time_left = countdown_time - datetime.datetime.now()
    if time_left.total_seconds() <= 0:
        time_left = datetime.timedelta(0)

    hours = time_left.seconds // 3600
    minutes = (time_left.seconds % 3600) // 60
    seconds = time_left.seconds % 60
    milliseconds = time_left.microseconds // 1000

    # Draw gradient background
    ax.set_facecolor('black')
    ax.imshow([[1, 0], [0, 1]], extent=(-1.5, 1.5, -1.5, 1.5), aspect='auto', cmap='coolwarm', alpha=0.8)

    # Draw the outer bezel
    ax.add_patch(Circle((0, 0), 1.05, transform=ax.transData._b, color='darkblue', fill=True, lw=12, zorder=2))
    ax.add_patch(Circle((0, 0), 1, transform=ax.transData._b, color='darkslategray', fill=False, lw=5, zorder=3))

    # Draw hour markers with shadow
    for i in range(12):
        angle = 2 * np.pi * i / 12
        x = np.cos(angle)
        y = np.sin(angle)
        ax.plot([0.75 * x, 0.85 * x], [0.75 * y, 0.85 * y], color='lightgray', lw=6, zorder=4)
        ax.text(0.65 * x, 0.65 * y, f'{12 if i == 0 else i}', ha='center', va='center', fontsize=16, fontweight='bold', color='white', zorder=5)

    # Draw minute markers
    for i in range(60):
        angle = 2 * np.pi * i / 60
        x = np.cos(angle)
        y = np.sin(angle)
        ax.plot([0.85 * x, 0.9 * x], [0.85 * y, 0.9 * y], color='lightblue', lw=2, zorder=4)

    # Draw second markers
    for i in range(300):  # 300 for finer ticks (5 per second)
        angle = 2 * np.pi * i / 300
        x = np.cos(angle)
        y = np.sin(angle)
        ax.plot([0.9 * x, 0.95 * x], [0.9 * y, 0.95 * y], color='lightgreen', lw=1, zorder=3)

    # Draw hour hand
    hour_angle = 2 * np.pi * (hours % 12 + minutes / 60) / 12
    ax.plot([0, 0.5 * np.cos(hour_angle)], [0, 0.5 * np.sin(hour_angle)], color='white', lw=10, zorder=6)

    # Draw minute hand
    minute_angle = 2 * np.pi * (minutes + seconds / 60) / 60
    ax.plot([0, 0.7 * np.cos(minute_angle)], [0, 0.7 * np.sin(minute_angle)], color='white', lw=8, zorder=6)

    # Draw second hand
    second_angle = 2 * np.pi * (seconds + milliseconds / 1000) / 60
    ax.plot([0, 0.85 * np.cos(second_angle)], [0, 0.85 * np.sin(second_angle)], color='red', lw=4, zorder=7)

    # Draw millisecond hand
    millisecond_angle = 2 * np.pi * milliseconds / 1000
    ax.plot([0, 0.9 * np.cos(millisecond_angle)], [0, 0.9 * np.sin(millisecond_angle)], color='yellow', lw=2, zorder=8)

    # Draw the center circle
    ax.add_patch(Circle((0, 0), 0.03, transform=ax.transData._b, color='white', fill=True, zorder=8))
    ax.add_patch(Circle((0, 0), 0.06, transform=ax.transData._b, color='lightgray', fill=True, zorder=7, alpha=0.7))

    # Draw rotating bezel with ticks
    ax.add_patch(Circle((0, 0), 1.1, transform=ax.transData._b, color='silver', fill=False, lw=15, zorder=1))
    ax.add_patch(Circle((0, 0), 1.12, transform=ax.transData._b, color='darkblue', fill=False, lw=15, zorder=0, linestyle=(0, (1, 10))))

    # Draw countdown time in the center with shadow effect
    time_str = f'{int(time_left.total_seconds())//3600:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}'
    ax.text(0, -1.25, time_str, ha='center', va='center', fontsize=24, color='white', fontweight='bold', zorder=9, bbox=dict(facecolor='black', edgecolor='black', boxstyle='round,pad=0.5'))

    # Simulate glass reflection
    ax.add_patch(FancyBboxPatch((-1.2, 1), width=2.4, height=0.3, boxstyle="round,pad=0.1", edgecolor='none', facecolor='white', transform=ax.transData._b, alpha=0.2, zorder=10))
    ax.add_patch(FancyBboxPatch((-0.7, -1), width=1.4, height=0.15, boxstyle="round,pad=0.1", edgecolor='none', facecolor='white', transform=ax.transData._b, alpha=0.2, zorder=10))

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xticks([])
ax.set_yticks([])

# Set the countdown duration (e.g., 10 minutes)
countdown_minutes = 10
countdown_seconds = countdown_minutes * 60

# Set the end time
countdown_time = datetime.datetime.now() + datetime.timedelta(seconds=countdown_seconds)

# Animate the clock
ani = animation.FuncAnimation(fig, update_clock, fargs=(ax, countdown_time), interval=50)

plt.show()
