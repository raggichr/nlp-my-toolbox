import numpy as np
import pandas as pd

# Simple sentence split ----
sentence = """Thomas Jefferson began building Monticello at the age of 26."""

print(sentence.split())  # sentence split into tokens by whitespace

# Turning words into numbers
token_sequence = str.split(sentence)  # (1)
vocab = sorted(set(token_sequence))  # (2)
print(', '.join(vocab))  # (3)

num_tokens = len(token_sequence)
vocab_size = len(vocab)

onehot_vectors = np.zeros(shape=(num_tokens, vocab_size), dtype=int)  # (4)
print(onehot_vectors)

for i, word in enumerate(token_sequence):
    onehot_vectors[i, vocab.index(word)] = 1  # (5)

print(' '.join(vocab))
print(onehot_vectors)

# (1) str.split is your quick-and-dirty tokenizer.
# (2) Your vocabulary lists all the unique tokens (words) that you want to keep track of.
# (3) Sorted lexographically (lexically) so numbers come before letters, and capital letters come
# before lowercase letters.
# (4) The empty table is a wide as your count of unique vocabulary terms and as high as the length of your document,
# 10 rows by 10 columns.
# (5) For each word in the sentence, mark the column for that word in your vocabulary with a 1.

df = pd.DataFrame(onehot_vectors, columns=vocab)
print(df)

df[df == 0] = ''  # create non-numerical object within your numpy array
print(df)
