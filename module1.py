import numpy as np
import matplotlib.pyplot as plt


def infected():
    # prevalence = np.arange(0.00001, 0.5)
    global specificity
    prevalence = np.arange(0.01, 0.5, 0.01)

    sens = .99
    spec = [.99, .9999, .999999]
    # p(pos | pt) * p(prevalence) /
    # p(pos | pt) * p(pt) + p(pos | nt) * p(nt)
    upper = np.zeros(len(prevalence))
    bottom = np.zeros(len(prevalence))
    result = np.zeros(len(prevalence))
    mat = np.zeros((3, len(prevalence)))
    idx = 0
    for specificity in spec:
        for i in range(len(prevalence)):
            upper[i] = sens * prevalence[i]

        for j in range(len(prevalence)):
            bottom[j] = (sens * prevalence[j]) + (1 - specificity) * (1 - prevalence[j])

        for i in range(len(prevalence)):
            result[i] = (upper[i] / bottom[i]) * 100

        mat[idx, :] = result
        idx += 1

        plt.plot(prevalence, result, c='red')
        plt.title("Change of infection with %f specificity" % specificity)
        plt.ylabel("Probability of Infection (%)")
        plt.xlabel("Prevalence rate")
        plt.show()

    plt.plot(prevalence, mat[0], c='red')
    plt.plot(prevalence, mat[1], c='blue')
    # plt.plot(prevalence, mat[2], c='green')
    plt.title("Change of infection with %f specificity" % specificity)
    plt.ylabel("Probability of Infection (%)")
    plt.xlabel("Prevalence rate")
    plt.show()


if __name__ == "__main__":
    infected()

'''
With such a high sensitivity rate, the true positive rate is bound to be quite high. 
Even though the prevalence rate isn't very high, 
it also isn't extremely low, so I would expect quite a high true positive rate. 
Probably higher than 80-85%. If the prevalence rate was higher, it would be even higher.
'''
