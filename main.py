perm = ["au", "fr", "hg"]
try:
    print(perm[3])
except IndexError:
    print("xyz")