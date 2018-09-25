import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


class Distribution:
    def __init__(self, distribution, estimate_function):
        self.distribution = distribution
        self.estimate_function = estimate_function

    def process_distribution(self):
        standard_deviations = []
        for k in range(1, max_k):
            squared_deviations = []
            for i in range(iterations):
                observations = self.distribution(theta, n)
                values = [x ** k for x in observations]
                m = mean(values)
                estimation = self.estimate_function(m, k)
                squared_deviations.append((theta - estimation) ** 2)
            standard_deviations.append(mean(squared_deviations))
        return standard_deviations


n = 200
theta = 1.0
iterations = 200
max_k = 100
figures_number = 1


def mean(values):
    return sum(values) / len(values)


def plot_graph(distribution_name, results):
    global figures_number
    figure = plt.figure(figures_number)
    figures_number += 1
    plt.subplot(111)
    plt.plot([i for i in range(1, len(results) + 1)], results, label=distribution_name)
    plt.xlabel('k')
    plt.ylabel('standard deviation')
    plt.legend()
    return figure


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def represents_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def main():
    global n, theta, iterations, max_k

    a = input("Input number of values in distribution or X to use the default value\n")
    if represents_int(a):
        n = int(a)
    a = input("Input distribution parameter or X to use the default value\n")
    if represents_float(a):
        theta = float(a)
    a = input("Input maximal k or X to use the default value\n")
    if represents_int(a):
        max_k = int(a)

    figure_uniform = plot_graph("uniform", Distribution(lambda h, s: np.random.uniform(0.0, h, s),
                                                        lambda x, k: ((k + 1) * x) ** (1 / float(k)))
                                .process_distribution())
    figure_exponential = plot_graph("exponential", Distribution(np.random.exponential,
                                                                lambda x, k: (x / math.factorial(k)) ** (1 / float(k)))
                                    .process_distribution())

    pp = PdfPages('standard-deviation.pdf')
    pp.savefig(figure_uniform)
    pp.savefig(figure_exponential)
    pp.close()

    print("Results written to standard-deviation.pdf.")


if __name__ == '__main__':
    main()
