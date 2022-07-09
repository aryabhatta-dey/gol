import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


def update(_, N):
    global grid
    global auxiliaryGrid

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
            if auxiliaryGrid[i, j] == 1:
                if (total < 2) or (total > 3):
                    grid[i, j] = 0
            else:
                if total == 3:
                    grid[i, j] = 1

    img.set_data(grid)
    auxiliaryGrid = grid
    return [img]


N = 100
P = 0.27
# create a 1 d array of length N * N filled with 0's with probability p and 1's with probability (1 - p) and then reshape it into a 2d array of N rows and N columns
grid = np.random.choice([0, 1], N * N, p=[P, 1 - P]).reshape(N, N)
auxiliaryGrid = grid.copy()

plt.style.use("dark_background")
fig, ax = plt.subplots()
img = ax.matshow(grid, cmap="Accent")
ani = animation.FuncAnimation(fig, update, fargs=(N,), interval=500, save_count=500)
ani.save("gol.mp4", dpi = 500)
