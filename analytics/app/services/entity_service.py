import matplotlib as plt



def plot_entity(locations):
    x = [row[0] for row in locations]
    y = [row[1] for row in locations]

    plt.figure()
    plt.plot(x, y, marker="o")
    plt.scatter(x[0], y[0], color="green", label="start")
    plt.scatter(x[0], y[0], color="red", label="end")

    plt.show()


