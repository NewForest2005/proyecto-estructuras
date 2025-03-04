import numpy as np

def generate_adjacency_matrix(n=10):
    # Create an adjacency matrix of size (n^2, n^2)
    adjacency_matrix = np.zeros((n**2, n**2), dtype=int)
    
    # Generate vertex indices
    vertices = [(i, j) for i in range(n) for j in range(n)]
    
    # Compute adjacency matrix
    for idx1, (i, j) in enumerate(vertices):
        for idx2, (k, l) in enumerate(vertices):
            probability = abs((i - k) * (j - l)) / 500
            adjacency_matrix[idx1, idx2] = np.random.choice([1, 0], p=[probability, 1 - probability])
    
    return adjacency_matrix

# Example usage
adj_matrix = generate_adjacency_matrix()
print(adj_matrix)
