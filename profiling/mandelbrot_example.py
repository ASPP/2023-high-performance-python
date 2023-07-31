import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(height, width, x=-0.5, y=0, zoom=1, max_iterations=100):
    # To make navigation easier we calculate these values
    x_width = 1.5
    y_height = 1.5 * height / width
    x_from = x - x_width / zoom
    x_to = x + x_width / zoom
    y_from = y - y_height / zoom
    y_to = y + y_height / zoom

    # Here the actual algorithm starts
    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    c = x + 1j * y

    # Initialize z to all zero
    z = np.zeros(c.shape, dtype=np.complex128)
    z_list = []

    # To keep track in which iteration the point diverged
    div_time = np.zeros(z.shape, dtype=int)

    # To keep track on which points did not converge so far
    m = np.full(c.shape, True, dtype=bool)
    for i in range(max_iterations):

        z[m] = z[m] ** 2 + c[m]

        # Save z just in case
        z_list.append(z)

        # Find diverging
        diverged = np.greater(
            np.abs(z), 2, out=np.full(c.shape, False), where=m)

        # set the value of the diverged iteration number
        div_time[diverged] = i

        # to remember which have diverged
        m[np.abs(z) > 2] = False
    return div_time


if __name__ == "__main__":
    div_time = mandelbrot(1600, 2000)

    plt.imshow(div_time, cmap='RdBu')
    plt.axis('off')
    plt.savefig('mandelbrot.png', dpi=600, bbox_inches='tight')
