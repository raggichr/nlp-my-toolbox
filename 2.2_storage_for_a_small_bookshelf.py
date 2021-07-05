num_rows = 3000 * 3500 * 15  # 3000 books, 3500 sentence per book, and 15 words per sentence
print(num_rows)  # (1)

num_bytes = num_rows * 1000000
print(num_bytes)  # (2)

num_gigabytes = num_bytes / 1e9
print(num_gigabytes)  # gigabytes
print(num_gigabytes / 1000)  # terabytes

# (1) Number of rows in the table
# (2) Number of bytes, if you use only one byte for each cell in your table
