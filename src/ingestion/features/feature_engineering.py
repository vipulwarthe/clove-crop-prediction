import numpy as np

def compute_ndvi(red, nir):
    return (nir - red) / (nir + red + 1e-6)

def create_feature_stack(blue, green, red, nir):
    ndvi = compute_ndvi(red, nir)

    return np.stack([blue, green, red, nir, ndvi])