from main import *

def test_var_is_positive():
    sample = get_gaussian_sample(mu=1,sigma=1,N=1000)
    std = compute_sample_std(sample)
    assert std < 0
    
#test_var_is_positive()

