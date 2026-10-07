import numpy as np

# 1. Physical Spatial Graph Topology (Fixed)
B = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
])

# 2. Observed Spatially Segregated Gene Expression
x_obs = np.array([10, 10, 100, 100])
d = np.sum(B,axis=1)
D = np.diag(d)
L = D - B
Lx_obs = L @ x_obs
d_energy_obs = x_obs.T @ Lx_obs 

num_shuffles = 1000
null_energies = np.zeros(num_shuffles)
rng = np.random.default_rng(100)

for i in range(num_shuffles):
    x_perm = np.random.permutation(x_obs)
    Lx_perm = L @ x_perm
    d_energy_perm = x_perm @ Lx_perm
    null_energies[i] = d_energy_perm

p_value = np.sum(null_energies <= d_energy_obs) / num_shuffles
print(p_value)



    