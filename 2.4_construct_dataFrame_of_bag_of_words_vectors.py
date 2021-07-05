import pandas as pd

sentence = """Thomas Jefferson began building Monticello at the age of 26."""
df = pd.DataFrame(pd.Series(dict([(token, 1) for token in sentence.split()])), columns=['sent']).T
print(df)

sentences = """Thomas Jefferson began building Monticello at the age of 26.\n"""
sentences += """Construction was done mostly by local masons and carpenters.\n"""
sentences += """He moved into the South Pavilion in 1770.\n"""
sentences += """Turning Monticello into a neoclassical masterpiece was Jefferson's obsession."""

corpus = {}
for i, sent in enumerate(sentences.split('\n')):  # (1)
    corpus['sent{}'.format(i)] = dict((tok, 1) for tok in sent.split())

df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T  # (2)
print(df.head())

# (1) Normally you should use .splitlines() but here you explicitly add a single '\n' character to the end of each
# line/sentence, so you need to explicitly split on this character.
# (2) Construct a DataFrame of bag-of-words vectors
