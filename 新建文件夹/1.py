import string
table = ''.maketrans('abcdef123','uvwxyz@#$')
s = "python is a great language.I like it!"
s.translate(table)