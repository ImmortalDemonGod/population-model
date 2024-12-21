def plot_population_growth(time, population_size):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.plot(time, population_size, label='Population Size', color='blue')
    plt.title('Population Growth Over Time')
    plt.xlabel('Time')
    plt.ylabel('Population Size')
    plt.legend()
    plt.grid()
    plt.show()