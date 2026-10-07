import numpy as np

# Adjacency Matrix B for 5 cells (Star graph centered at Cell 0)
B = np.array([
    [0, 1, 1, 1, 1],  # Cell 0 touches 1, 2, 3, 4
    [1, 0, 0, 0, 0],  # Cell 1 touches 0
    [1, 0, 0, 0, 0],  # Cell 2 touches 0
    [1, 0, 0, 0, 0],  # Cell 3 touches 0
    [1, 0, 0, 0, 0]   # Cell 4 touches 0
])

# Expression level of a target gene across cells 0 to 4
x = np.array([100, 20, 20, 20, 20])
d = np.sum(B, axis=1)
D = np.diag(d)
L = D - B
Lx = L@x
print(d)
print(D)
print(L)
print(Lx)


# 1. Adjacency matrix for 0 -- 1 -- 2
B2 = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
])

# 2. Gene expression vector
x2 = np.array([5, 15, 25])
d2 = np.sum(B2, axis=1)
D2 = np.diag(d2)
L2 = D2 - B2
L2x = L2@x2
energy = x2.T@L2x
print(L2x)
print(energy)