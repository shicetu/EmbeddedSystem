import numpy as np
import matplotlib.pyplot as plt
import random


def gen_sample_data():
    w = random.randint(0, 10) + random.random()
    b = random.randint(0, 5) + random.random()

    num_sample = 100
    x_list = []
    y_list = []
    for i in range(num_sample):
        x = random.randint(0, 100) * random.random()
        y = w * x + b + random.random() * random.randint(-1, 100) + random.randint(-1, 20)

        x_list.append(x)
        y_list.append(y)

    return x_list, y_list


# define cost function
def cost_function(theta, x_array, y_array):
    diff = np.dot(x_array, theta) - y_array
    return (1 / (2 * len(y_array))) * np.dot(diff.transpose(), diff)


# get gradient value of the cost function
def gradient_function(theta, x_array, y_array):
    m = len(x_array)
    diff = np.dot(x_array, theta) - y_array  # sum of all predict value - true value
    return (1 / m) * np.dot(x_array.transpose(), diff)


def train_func(x_array, y_array, lr):
    # init figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # change to interactive mode
    plt.ion()
    ax.scatter(x_list_init, y_list_init, s=30, c="red", marker="s")
    plt.xlabel("X")
    plt.ylabel("Y")
    x = np.arange(0, len(x_list_init), 0.2)

    theta = np.array([1, 1]).reshape(2, 1)
    gradient = gradient_function(theta, x_array, y_array)

    # if direction gradient of cost func <= 0.1, then stop
    while not all(abs(gradient) <= 0.2):
        # calculate new coefficient of cost function
        theta = theta - lr * gradient
        gradient = gradient_function(theta, x_array, y_array)

        # theta and cost log
        print("final_theta:", theta[0][0], theta[1][0])
        print('cost function:', cost_function(theta, x_array, y_array)[0][0])

        # update plot
        y = theta[0][0] + theta[1][0] * x
        ax.plot(x, y)
        plt.pause(0.001)

    plt.ioff()
    plt.show()
    return theta


# generate train data
x_list_init, y_list_init = gen_sample_data()


def main():
    x_list = np.array(x_list_init).reshape(len(x_list_init), 1)
    y_list = np.array(y_list_init).reshape(len(y_list_init), 1)

    # Generate a vector of m rows and 1 column, which is x0, which is all 1
    add_column_with_1 = np.ones((len(x_list), 1))
    x_list = np.hstack((add_column_with_1, x_list))

    # set init learn rate
    learn_rate = 0.001382
    trained_theta = train_func(x_list, y_list, learn_rate)


if __name__ == "__main__":
    main()
