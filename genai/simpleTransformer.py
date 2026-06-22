import numpy as np

# Example word vectors (pretend embeddings)
X = np.array([
    [1, 0],   # "I"
    [0, 1],   # "love"
    [1, 1]    # "cats"
])

# Random weight matrices
Wq = np.random.rand(2, 2)
Wk = np.random.rand(2, 2)
Wv = np.random.rand(2, 2)

# Compute Query, Key, Value
Q = X @ Wq
K = X @ Wk
V = X @ Wv

# Attention scores
scores = Q @ K.T

# Softmax
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

weights = softmax(scores)

# Final output
output = weights @ V

print(output)