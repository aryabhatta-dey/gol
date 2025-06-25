import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

def update(_, N):
    img.set_data(grid)
    auxiliaryGrid = grid.copy()
    return [img]

N = 60
P = 0.15

# Cells initialized with either 0 (dead) or 1 (alive)
grid = np.random.choice([0, 1], N * N, p=[1 - P, P]).reshape(N, N)
auxiliaryGrid = grid.copy()

plt.style.use("dark_background")
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap="plasma", interpolation='nearest')
plt.axis('off')  # Hide axes for cleaner output

ani = animation.FuncAnimation(fig, update, fargs=(N,), interval=200, save_count=200)
ani.save("custom_life.mp4", dpi=300)
