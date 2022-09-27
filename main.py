import numpy as np
import scipy
from scipy.stats import norm

def get_gaussian_sample(mu, sigma, N):
    rv1 = norm(loc=mu, scale=sigma)
    sample = rv1.rvs(N)
    return sample

def compute_sample_average(sample):
    return sample.mean()

def compute_sample_std(sample):
    return np.sqrt(np.var(sample))

sample = get_gaussian_sample(mu=1,sigma=1,N=1000)
print(compute_sample_average(sample))
print(compute_sample_std(sample))