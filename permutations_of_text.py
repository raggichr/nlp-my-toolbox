from itertools import permutations

print([" ".join(combo) for combo in permutations(iterable="Good morning Rosa!".split(), r=3)])

s = """Find textbooks with titles containing 'NLP', or 'natural' and 'language', or 'computational' and 'linguistics.'"""
print(len(set(s.split())))

import numpy as np

print(np.arange(1, 12 + 1).prod())  # factorial(12) = arange(1, 13).prod()

# The number of permutations explodes from factorial(3) == 6 in our simple greeting to factorial(12) == 479001600 in
# out longer statement!