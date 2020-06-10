import numpy as np

def test_norm_1():
    from norms import norm_1

    for i in range(10):
        A = np.random.randn(20, 20)
        x = np.random.randn(20)
        
        assert norm_1(A@x) <= norm_1(A) * norm_1(x)