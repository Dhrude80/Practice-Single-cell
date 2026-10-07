import numpy as np
from scipy.spatial import KDTree
stars = np.array([
    [0.0,  0.0,  50.0],  # Row 0
    [1.0,  1.0,  30.0],  # Row 1
    [1.5,  0.5,  20.0],  # Row 2
    [10.0, 12.0, 90.0]   # Row 3
], dtype=float)
coordinates = stars[:,[0,1]]
space_tree = KDTree(coordinates)
close_stars = space_tree.query_ball_point(x=[0,0], r = 2)
print(close_stars)
