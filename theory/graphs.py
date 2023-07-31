import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 1000)  # Input size range
o_n_log_n = n * np.log2(n)  # Time complexity O(nlogn)
o_n = n


def plot_graph(time_complexity, label):
    plt.plot(n, time_complexity, label=label)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time Complexity')
    plt.title(f'Time Complexity:{label}')
    plt.legend()
    plt.show()
    plt.figure()


plot_graph(o_n, "O(n)")
plot_graph(o_n_log_n, "O(nlogn)")
