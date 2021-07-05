import pandas as pd
import numpy as np
# One way to check for the similarities between sentences is to count the number of overlapping tokens
# using a dot product.
v1 = np.array([1, 2, 3])
v2 = np.array([2, 3, 4])
print(v1.dot(v2))

print((v1 * v2).sum())  # (1)

print(zip(v1, v2))
print([x1 * x2 for x1, x2 in zip(v1, v2)])  # (2)

print(v1.reshape(-1, 1).T @ v2.reshape(-1, 1))  # (3)

# (1) Multiplication of numpy arrays is a "vectorized" operation that is very efficient.
# (2) You shouldn't iterate through vectors this way unless you want to slow down your pipeline.
# (3) The dot product is equivalent to the matrix product, which can be accomplished in numpy with the np.matmul()
# function or the @ operator.
