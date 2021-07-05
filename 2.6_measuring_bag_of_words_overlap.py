import pandas as pd

sentences = """Thomas Jefferson began building Monticello at the age of 26.\n"""
sentences += """Construction was done mostly by local masons and carpenters.\n"""
sentences += """He moved into the South Pavilion in 1770.\n"""
sentences += """Turning Monticello into a neoclassical masterpiece was Jefferson's obsession."""

corpus = {}
for i, sent in enumerate(sentences.split('\n')):
    corpus['sent{}'.format(i)] = dict((tok, 1) for tok in sent.split())

df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T  # (1)
print(df.head(20))

df = df.T
print(df.sent0.dot(df.sent1))
print(df.sent0.dot(df.sent2))
print(df.sent0.dot(df.sent3))  # (2)

print([(k, v) for (k, v) in (df.sent0 & df.sent3).items() if v])  # (3)

# (1) This is your first vector space model (VSM) of natural language documents (sentences).
# (2) Overlap of word counts for two bag-of-words vectors.
# (3) Find the words which are shared in sentence 0 and 3.
