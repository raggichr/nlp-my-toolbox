import re  # (1)

r = "(hi|hello|hey)[ ]*([a-z]*)"  # (2)
print(re.match(pattern=r, string='Hello Rosa', flags=re.IGNORECASE))  # (3)

print(re.match(pattern=r, string="hi ho, hi ho, it's off to work ...", flags=re.IGNORECASE))

print(re.match(pattern=r, string="hey hey, what's up", flags=re.IGNORECASE))

# (1) There are two "official" regular expression packages in Python. We use the re package here just because it's
# installed with all versions of Python. The regex package comes with later versions of Python and is much more
# powerful, as you'll see later.

# (2) '|' means "OR," and '\*' means the preceding character can occur 0 or more times and still match. So our regex
# will match greetings that start with "hi" or "hello" or "hey" followed by any number of '' characters and then
# any number of letters.

# (3) Ignoring the case of text characters is common, to keep the regular expressions simpler.

r = r"[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])?(morn[gin']{0,3}|afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})"
re_greeting = re.compile(pattern=r, flags=re.IGNORECASE)
print(re_greeting.match(string='Hello Rosa'))  # (4)

print(re_greeting.match(string='Hello Rosa').groups())

print(re_greeting.match(string='Good morning Rosa'))

print(re_greeting.match(string='Good manning Rosa'))  # (5)

print(re_greeting.match(string='Good evening Rosa Parks').groups())  # (6)

print(re_greeting.match(string="Good Morn'n Rosa"))

print(re_greeting.match(string='yo Rosa'))

# (4) You can compile regular expression so you don't have to specify the options (flags) each time you use them.

# (5) Notice that this regular expression cannot recognize (match) words with typos.

# (6) Our regular expression can separate different parts of the greeting into groups, but it will be unaware of
# Rosa's famous last name, because we don't have a pattern to match any characters after the first name.
