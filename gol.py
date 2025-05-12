import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

def update(_, N):
    global grid
    global auxiliaryGrid
    global ageGrid

    for i in range(N):
        for j in range(N):
            total = (
                auxiliaryGrid[(i - 1) % N, (j - 1) % N]
                + auxiliaryGrid[(i - 1) % N, j]
                + auxiliaryGrid[(i - 1) % N, (j + 1) % N]
                + auxiliaryGrid[i, (j - 1) % N]
                + auxiliaryGrid[i, (j + 1) % N]
                + auxiliaryGrid[(i + 1) % N, (j - 1) % N]
                + auxiliaryGrid[(i + 1) % N, j]
                + auxiliaryGrid[(i + 1) % N, (j + 1) % N]
            )

            if auxiliaryGrid[i, j] >= 1:
                if total in (2, 3):
                    grid[i, j] = min(10, auxiliaryGrid[i, j] + 1)  # Increase age
                else:
                    grid[i, j] = 0
            else:
                if total == 3:
                    grid[i, j] = 1  # Cell is reborn
                else:
                    grid[i, j] = 0

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
