import numpy as np

L = np.array([
    [ 2., -1., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.,  0.],
    [-1., -1.,  3., -1.,  0.,  0.],
    [ 0.,  0., -1.,  3., -1., -1.],
    [ 0.,  0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1., -1.,  2.]
])

node_indices = np.arange(6)
eigen_values,eigen_vectors = np.linalg.eigh(L)
i = np.argsort(eigen_values)
eigen_vectors = eigen_vectors[:,i]
eigen_values = eigen_values[i]
fiedler_vector = eigen_vectors[:,1]
fiedler_value = eigen_values[1]
fiedler_vector_shape = fiedler_vector.shape
segregation_1_mask = fiedler_vector < 0
segregation_2_mask = fiedler_vector > 0
segregation_1 = fiedler_vector[segregation_1_mask]
segregation_2 = fiedler_vector[segregation_2_mask]
print(segregation_1)
print(segregation_2)