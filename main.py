import matplotlib.pyplot as plt
import random
import numpy as np


def f(a, b, c, x):
    return a*x*x + b*x + c


def check_intersect(a, b, c, x1, x2, y):
    if ((f(a, b, c, x1) - y) * (f(a, b, c, x2) - y)) <= 0:
        return True
    return False


def draw_new_graph(a, b, c, x, y, upper_left, lower_right):
    plt.clf()
    plt.axis([x[0], x[1], y[0], y[1]])
    plt.xlabel('X')
    plt.ylabel('Y')
    points = 10 * (x[1] - x[0])
    graph_x = np.linspace(x[0], x[1], points)
    plt.plot([0, 0], [y[0], y[1]], color='black')
    plt.plot([x[0], x[1]], [0, 0], color='black')
    plt.plot([upper_left[0], lower_right[0], lower_right[0], upper_left[0], upper_left[0]],
             [upper_left[1], upper_left[1], lower_right[1], lower_right[1], upper_left[1]], color='red')
    if a is not None:
        graph_y = a * graph_x * graph_x + b * graph_x + c
        plt.plot(graph_x, graph_y, 'blue')


def play_game(x_range, y_range):
    width = random.randint(1, x_range / 2)
    height = random.randint(1, y_range / 2)
    upper_left_x = random.randint(-x_range / 2, x_range / 2)
    upper_left_y = random.randint(-y_range / 2, y_range / 2)
    lower_right_x = upper_left_x - width
    lower_right_y = upper_left_y - height
    a, b, c = None, None, None
    plt.ion()
    plt.show()
    draw_new_graph(a, b, c, [-x_range, x_range], [-y_range, y_range],
                   [upper_left_x, upper_left_y], [lower_right_x, lower_right_y])
    plt.draw()
    plt.pause(0.1)
    while True:
        print("Please input the variables for a quadratic function (q to exit)")
        a = input("a = ")
        if a == "q":
            break
        b = input("b = ")
        if b == "q":
            break
        c = input("c = ")
        if c == "q":
            break
        a = int(a)
        b = int(b)
        c = int(c)
        draw_new_graph(a, b, c, [-x_range, x_range], [-y_range, y_range],
                       [upper_left_x, upper_left_y], [lower_right_x, lower_right_y])
        plt.draw()
        plt.pause(0.1)
        critical_points = [upper_left_x]
        if a != 0:
            critical_points.append(-b / 2*a)
        critical_points.append(lower_right_x)
        flag = False
        for i in range(len(critical_points)-1):
            flag = flag or check_intersect(a, b, c, critical_points[i], critical_points[i+1], upper_left_y)
            flag = flag or check_intersect(a, b, c, critical_points[i], critical_points[i+1], lower_right_y)
        if not flag:
            print("Congratulations! You won!")
            plt.pause(2)
            return


choice = int(input("Type 1 to start playing: "))
if choice == 1:
    play_game(10, 10)
