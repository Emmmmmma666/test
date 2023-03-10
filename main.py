# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
#
# # Press the green button in the gutter to run the script.
import random

import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':


#
#     # problem 1: monte carlo method to estimate pi.
#     # uniformly generate two random numbers x, y between [-1, 1].
#     # if x**2 + y**2 <= 1, then the point (x, y) is the circle with area = pi.
#     # what is the probability that the random (x, y) is in the circle?
#     # the probability is pi/4.
#     # what we will do is generate n sample points of (x, y) and say m samples are with in the circle.
#     # then what is our estimate of pi?
#     # m/n = pi/4 => pi 4m/n.
    def gen_samples(n):
        x_samples = np.random.uniform(low=-1, high=1, size=n)
        y_samples = np.random.uniform(low=-1, high=1, size=n)
        return x_samples, y_samples

#
#     # This function estimates pi based on the 1000000 samples.
    def estimate_pi():
        num_samples = 1000000
        xs, ys = gen_samples(n=num_samples)
        cnt = 0
        # for the ith iteration, we look at the ith sample and see if its within the unit circle.
        # if the ith sample is within the unit circle, we incremenet cnt.
        for i in range(num_samples):
            if xs[i] ** 2 + ys[i] ** 2 <= 1:
                cnt = cnt + 1

        g = 4*cnt/num_samples
        print(g)

    gg = estimate_pi()




    # def draw_samples(x_samples, y_samples):
    #     fig = plt.figure()
    #     ax = fig.gca()
    #     ax.set_xlim([-1.5, 1.5])
    #     ax.set_ylim([-1.5, 1.5])
    #
    #     for i in range(len(x_samples)):
    #         ax.plot(x_samples[i], y_samples[i], 'ro')
    #     circ = plt.Circle((0, 0), radius=1, edgecolor='b', facecolor='None')
    #     ax.add_patch(circ)
    #     plt.grid()
    #     plt.show()
    # #
    # #
    # # # Press the green button in the gutter to run the script.
    # if __name__ == '__main__':
    #     # estimate_pi()
    #     num_samples = 500
    #     xs, ys = gen_samples(n=num_samples)
    #     draw_samples(xs, ys)

# if __name__ == '__main__':



