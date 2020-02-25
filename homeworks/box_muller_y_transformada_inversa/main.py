"""main class for homework assignment, formulas are contained within the components
folder"""

import matplotlib.pyplot as plt
import components

def main():
    """main method for the homework assignment"""

    i = 10000
    x_min = 0
    x_max = 500000

    muller_values = components.box_muller(i, x_min, x_max)
    inverse_values = components.inverse_transform(i, x_min, x_max)

    n_bins = 100
    v_rwidth = 0.90

    plt.hist(muller_values, bins=n_bins, rwidth=v_rwidth, color="blue")
    plt.hist(inverse_values, bins=n_bins, rwidth=v_rwidth, color="yellow")

    plt.show()

if __name__ == "__main__":
    main()
