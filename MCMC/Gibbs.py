from tqdm import tqdm
import math
import copy
from numpy.random import normal


class Gibbs:
    def __init__(
        self, iter: int = 10000, burn_ratio: float = 0.5, random_walk: float = 0.1
    ):
        self.iter = iter
        self.burn_ratio = burn_ratio
        self.sample = []
        self.random_walk = random_walk

    def sampling(self, u: list, log_prior, log_likelihood):
        self.sample.append(u)
        dim = len(u)
        last_sample = copy.deepcopy(u)
        sample = copy.deepcopy(u)
        bar = tqdm(range(1, self.iter), desc="Gibbs")
        for i in bar:
            for j in range(dim):
                pass
            # log_prior +log_likelihood 中使用MCMC从每个边缘概率密度p(u1|u2)中采样
            self.sample.append(sample)


def test():
    from matplotlib import pyplot as plt
    from scipy.stats import multivariate_normal

    def log_prior(x: list):
        return 0

    def log_likelihood(x: list):
        mean = [0.5, -0.2]
        cov = [[2.0, 0.3], [0.3, 0.5]]
        return math.log(multivariate_normal.pdf(x, mean=mean, cov=cov))

    MH = Gibbs()
    MH.sampling([0, 0], log_prior, log_likelihood)

    plt.scatter(MH.sample[:][0], MH.sample[:][1], alpha=0.8)
    plt.show()
    MH.sample[:][0]
