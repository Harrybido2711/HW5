import numpy as np


def euclidean_distances(X, Y):
    """Compute pairwise Euclidean distance between the rows of two matrices X (shape MxK)
    and Y (shape NxK). The output of this function is a matrix of shape MxN containing
    the Euclidean distance between two rows.

    (Hint: You're free to implement this with numpy.linalg.norm)

    Arguments:
        X {np.ndarray} -- First matrix, containing M examples with K features each.
        Y {np.ndarray} -- Second matrix, containing N examples with K features each.

    Returns:
        D {np.ndarray}: MxN matrix with Euclidean distances between rows of X and rows of Y.
    """
    # initialize matrix D with all zeros
    M, N = X.shape[0], Y.shape[0]
    D = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            D[i, j] = np.linalg.norm(X[i] - Y[j]) # direct calculation of L2
    return D


def manhattan_distances(X, Y):
    """Compute pairwise Manhattan distance between the rows of two matrices X (shape MxK)
    and Y (shape NxK). The output of this function is a matrix of shape MxN containing
    the Manhattan distance between two rows.

    (Hint: You're free to implement this with numpy.linalg.norm)

    Arguments:
        X {np.ndarray} -- First matrix, containing M examples with K features each.
        Y {np.ndarray} -- Second matrix, containing N examples with K features each.

    Returns:
        D {np.ndarray}: MxN matrix with Manhattan distances between rows of X and rows of Y.
    """
    # similar to euclidean distances
    M, N = X.shape[0], Y.shape[0]
    D = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            D[i, j] = np.linalg.norm(X[i] - Y[j], ord = 1) # direct calculation of L1
    return D


def cosine_distances(X, Y):
    """Compute pairwise Cosine distance between the rows of two matrices X (shape MxK)
    and Y (shape NxK). The output of this function is a matrix of shape MxN containing
    the Cosine distance between two rows.

    (Hint: You're free to implement this with numpy.linalg.norm)
    (Hint: this is cosine *distance*, not cosine similarity)

    Arguments:
        X {np.ndarray} -- First matrix, containing M examples with K features each.
        Y {np.ndarray} -- Second matrix, containing N examples with K features each.

    Returns:
        D {np.ndarray}: MxN matrix with Cosine distances between rows of X and rows of Y.
    """
    M, N = X.shape[0], Y.shape[0]
    D = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            dot_product = np.dot(X[i], Y[j])
            norms_multiple = np.linalg.norm(X[i]) * np.linalg.norm(Y[j]) 
            D[i, j] = 1 - np.clip(dot_product / norms_multiple, -1, 1) # revise because of floating point
    return D
