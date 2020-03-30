import numpy as np
from ballistico.helpers.tools import generate_unitary_grid, generate_index_grid

replica_grid = np.array([[0, 0, 0],
                         [ 0,  0,  1],
                         [ 0,  0,  2],
                         [ 0,  0, -2],
                         [ 0,  0, -1],
                         [ 0,  1,  0],
                         [ 0,  1,  1],
                         [ 0,  1,  2],
                         [ 0,  1, -2],
                         [ 0,  1, -1],
                         [ 0,  2,  0],
                         [ 0,  2,  1],
                         [ 0,  2,  2],
                         [ 0,  2, -2],
                         [ 0,  2, -1],
                         [ 0, -2,  0],
                         [ 0, -2,  1],
                         [ 0, -2,  2],
                         [ 0, -2, -2],
                         [ 0, -2, -1],
                         [ 0, -1,  0],
                         [ 0, -1,  1],
                         [ 0, -1,  2],
                         [ 0, -1, -2],
                         [ 0, -1, -1],
                         [ 1,  0,  0],
                         [ 1,  0,  1],
                         [ 1,  0,  2],
                         [ 1,  0, -2],
                         [ 1,  0, -1],
                         [ 1,  1,  0],
                         [ 1,  1,  1],
                         [ 1,  1,  2],
                         [ 1,  1, -2],
                         [ 1,  1, -1],
                         [ 1,  2,  0],
                         [ 1,  2,  1],
                         [ 1,  2,  2],
                         [ 1,  2, -2],
                         [ 1,  2, -1],
                         [ 1, -2,  0],
                         [ 1, -2,  1],
                         [ 1, -2,  2],
                         [ 1, -2, -2],
                         [ 1, -2, -1],
                         [ 1, -1,  0],
                         [ 1, -1,  1],
                         [ 1, -1,  2],
                         [ 1, -1, -2],
                         [ 1, -1, -1],
                         [ 2,  0,  0],
                         [ 2,  0,  1],
                         [ 2,  0,  2],
                         [ 2,  0, -2],
                         [ 2,  0, -1],
                         [ 2,  1,  0],
                         [ 2,  1,  1],
                         [ 2,  1,  2],
                         [ 2,  1, -2],
                         [ 2,  1, -1],
                         [ 2,  2,  0],
                         [ 2,  2,  1],
                         [ 2,  2,  2],
                         [ 2,  2, -2],
                         [ 2,  2, -1],
                         [ 2, -2,  0],
                         [ 2, -2,  1],
                         [ 2, -2,  2],
                         [ 2, -2, -2],
                         [ 2, -2, -1],
                         [ 2, -1,  0],
                         [ 2, -1,  1],
                         [ 2, -1,  2],
                         [ 2, -1, -2],
                         [ 2, -1, -1],
                         [-2,  0,  0],
                         [-2,  0,  1],
                         [-2,  0,  2],
                         [-2,  0, -2],
                         [-2,  0, -1],
                         [-2,  1,  0],
                         [-2,  1,  1],
                         [-2,  1,  2],
                         [-2,  1, -2],
                         [-2,  1, -1],
                         [-2,  2,  0],
                         [-2,  2,  1],
                         [-2,  2,  2],
                         [-2,  2, -2],
                         [-2,  2, -1],
                         [-2, -2,  0],
                         [-2, -2,  1],
                         [-2, -2,  2],
                         [-2, -2, -2],
                         [-2, -2, -1],
                         [-2, -1,  0],
                         [-2, -1,  1],
                         [-2, -1,  2],
                         [-2, -1, -2],
                         [-2, -1, -1],
                         [-1,  0,  0],
                         [-1,  0,  1],
                         [-1,  0,  2],
                         [-1,  0, -2],
                         [-1,  0, -1],
                         [-1,  1,  0],
                         [-1,  1,  1],
                         [-1,  1,  2],
                         [-1,  1, -2],
                         [-1,  1, -1],
                         [-1,  2,  0],
                         [-1,  2,  1],
                         [-1,  2,  2],
                         [-1,  2, -2],
                         [-1,  2, -1],
                         [-1, -2,  0],
                         [-1, -2,  1],
                         [-1, -2,  2],
                         [-1, -2, -2],
                         [-1, -2, -1],
                         [-1, -1,  0],
                         [-1, -1,  1],
                         [-1, -1,  2],
                         [-1, -1, -2],
                         [-1, -1, -1]])

k_grid = np.array([[-0.4, -0.4, -0.4],
       [-0.4, -0.4, -0.2],
       [-0.4, -0.4,  0. ],
       [-0.4, -0.4,  0.2],
       [-0.4, -0.4,  0.4],
       [-0.4, -0.2, -0.4],
       [-0.4, -0.2, -0.2],
       [-0.4, -0.2,  0. ],
       [-0.4, -0.2,  0.2],
       [-0.4, -0.2,  0.4],
       [-0.4,  0. , -0.4],
       [-0.4,  0. , -0.2],
       [-0.4,  0. ,  0. ],
       [-0.4,  0. ,  0.2],
       [-0.4,  0. ,  0.4],
       [-0.4,  0.2, -0.4],
       [-0.4,  0.2, -0.2],
       [-0.4,  0.2,  0. ],
       [-0.4,  0.2,  0.2],
       [-0.4,  0.2,  0.4],
       [-0.4,  0.4, -0.4],
       [-0.4,  0.4, -0.2],
       [-0.4,  0.4,  0. ],
       [-0.4,  0.4,  0.2],
       [-0.4,  0.4,  0.4],
       [-0.2, -0.4, -0.4],
       [-0.2, -0.4, -0.2],
       [-0.2, -0.4,  0. ],
       [-0.2, -0.4,  0.2],
       [-0.2, -0.4,  0.4],
       [-0.2, -0.2, -0.4],
       [-0.2, -0.2, -0.2],
       [-0.2, -0.2,  0. ],
       [-0.2, -0.2,  0.2],
       [-0.2, -0.2,  0.4],
       [-0.2,  0. , -0.4],
       [-0.2,  0. , -0.2],
       [-0.2,  0. ,  0. ],
       [-0.2,  0. ,  0.2],
       [-0.2,  0. ,  0.4],
       [-0.2,  0.2, -0.4],
       [-0.2,  0.2, -0.2],
       [-0.2,  0.2,  0. ],
       [-0.2,  0.2,  0.2],
       [-0.2,  0.2,  0.4],
       [-0.2,  0.4, -0.4],
       [-0.2,  0.4, -0.2],
       [-0.2,  0.4,  0. ],
       [-0.2,  0.4,  0.2],
       [-0.2,  0.4,  0.4],
       [ 0. , -0.4, -0.4],
       [ 0. , -0.4, -0.2],
       [ 0. , -0.4,  0. ],
       [ 0. , -0.4,  0.2],
       [ 0. , -0.4,  0.4],
       [ 0. , -0.2, -0.4],
       [ 0. , -0.2, -0.2],
       [ 0. , -0.2,  0. ],
       [ 0. , -0.2,  0.2],
       [ 0. , -0.2,  0.4],
       [ 0. ,  0. , -0.4],
       [ 0. ,  0. , -0.2],
       [ 0. ,  0. ,  0. ],
       [ 0. ,  0. ,  0.2],
       [ 0. ,  0. ,  0.4],
       [ 0. ,  0.2, -0.4],
       [ 0. ,  0.2, -0.2],
       [ 0. ,  0.2,  0. ],
       [ 0. ,  0.2,  0.2],
       [ 0. ,  0.2,  0.4],
       [ 0. ,  0.4, -0.4],
       [ 0. ,  0.4, -0.2],
       [ 0. ,  0.4,  0. ],
       [ 0. ,  0.4,  0.2],
       [ 0. ,  0.4,  0.4],
       [ 0.2, -0.4, -0.4],
       [ 0.2, -0.4, -0.2],
       [ 0.2, -0.4,  0. ],
       [ 0.2, -0.4,  0.2],
       [ 0.2, -0.4,  0.4],
       [ 0.2, -0.2, -0.4],
       [ 0.2, -0.2, -0.2],
       [ 0.2, -0.2,  0. ],
       [ 0.2, -0.2,  0.2],
       [ 0.2, -0.2,  0.4],
       [ 0.2,  0. , -0.4],
       [ 0.2,  0. , -0.2],
       [ 0.2,  0. ,  0. ],
       [ 0.2,  0. ,  0.2],
       [ 0.2,  0. ,  0.4],
       [ 0.2,  0.2, -0.4],
       [ 0.2,  0.2, -0.2],
       [ 0.2,  0.2,  0. ],
       [ 0.2,  0.2,  0.2],
       [ 0.2,  0.2,  0.4],
       [ 0.2,  0.4, -0.4],
       [ 0.2,  0.4, -0.2],
       [ 0.2,  0.4,  0. ],
       [ 0.2,  0.4,  0.2],
       [ 0.2,  0.4,  0.4],
       [ 0.4, -0.4, -0.4],
       [ 0.4, -0.4, -0.2],
       [ 0.4, -0.4,  0. ],
       [ 0.4, -0.4,  0.2],
       [ 0.4, -0.4,  0.4],
       [ 0.4, -0.2, -0.4],
       [ 0.4, -0.2, -0.2],
       [ 0.4, -0.2,  0. ],
       [ 0.4, -0.2,  0.2],
       [ 0.4, -0.2,  0.4],
       [ 0.4,  0. , -0.4],
       [ 0.4,  0. , -0.2],
       [ 0.4,  0. ,  0. ],
       [ 0.4,  0. ,  0.2],
       [ 0.4,  0. ,  0.4],
       [ 0.4,  0.2, -0.4],
       [ 0.4,  0.2, -0.2],
       [ 0.4,  0.2,  0. ],
       [ 0.4,  0.2,  0.2],
       [ 0.4,  0.2,  0.4],
       [ 0.4,  0.4, -0.4],
       [ 0.4,  0.4, -0.2],
       [ 0.4,  0.4,  0. ],
       [ 0.4,  0.4,  0.2],
       [ 0.4,  0.4,  0.4]])


def test_k_mesh():
    grid_shape = (5, 5, 5)
    generated_grid = generate_index_grid(grid=grid_shape,
                                         order='F',
                                         is_wrapping=True,
                                         is_centering=False)
    np.testing.assert_equal(replica_grid, generated_grid)


def test_q_mesh():
    grid_shape = (5, 5, 5)
    generated_k_grid = generate_unitary_grid(grid_shape, order='F', is_wrapping=False, is_centering=True)
    np.testing.assert_equal(k_grid, generated_k_grid)