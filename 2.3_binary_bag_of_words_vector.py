sentence = """Thomas Jefferson began building Monticello at the age of 26."""
sentence_bow = {}  # bag-of-words (BOW)
for token in sentence.split():
    sentence_bow[token] = 1

print(sorted(sentence_bow.items()))
