import argparse

import matplotlib.pyplot as plt


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Measure numerical intergration error."
    )
    parser.add_argument(
        "n_max", type=int, help="number of bins to use for integration",
    )
    parser.add_argument(
        "a", type=float, help="lower bound for integration",
    )
    parser.add_argument(
        "b", type=float, help="upper bound for integration",
    )

    return parser.parse_args()


def integrate_f(f, a, b, n):
    s = []
    for i in range(n):
        dx = (b - a) / n
        x = a + (i + 0.5) * dx
        y = f(x)
        s = s + [y * dx]
    return sum(s)


def measure_integration_errors(f, F, n_max, a, b):
    errors = []
    for n in range(1, n_max, 10):
        F_analytical = F(b) - F(a)
        F_numerical = integrate_f(f, a, b, n)
        error = abs(F_analytical - F_numerical)
        errors = errors + [error]
    return errors


def plot_results(n_max, errors):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(1, n_max)
    ax.set_ylim(1e-7, max(errors))
    ax.set_xlabel("Number of bins")
    ax.set_ylabel("Absolute error")
    ax.set_yscale("log")
    ax.plot(range(1, n_max, 10), errors)
    fig.savefig("numerical_integration_error.pdf")


def main():
    args = parse_arguments()

    def f(x):
        return x ** 4 - 3 * x

    def F(x):
        return 1 / 5 * x ** 5 - 3 / 2 * x ** 2

    errors = measure_integration_errors(f, F, args.n_max, args.a, args.b)
    plot_results(args.n_max, errors)


if __name__ == "__main__":
    main()
