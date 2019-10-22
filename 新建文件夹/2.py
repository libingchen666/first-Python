import string
def kaisa(s,k):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    before = string.ascii_letters
    after = lower[k:]+lower[:k]+upper[k:]+upper[:k]
    table = ''.maketrans(before,after)
    return s.translate(table)
    s = "If the implementation is easy to explain,it may be a good idea."
kaisa(s,3)