import numpy as np

def norm_1(ary):
    """Computes the 1-norm of vectors or matrices *ary* passed in as numpy arrays."""
    
    if len(ary.shape) == 1:
        return np.sum(np.abs(ary))
    elif len(ary.shape) == 2:
        return np.max(np.sum(np.abs(ary), axis=1))
    else:
        raise ValueError("ary must be vector or matrix")