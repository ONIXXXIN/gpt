perm = ["au", "fr", "hg"]
try:
    perm.remove("au")
    print(perm[3])
except IndexError as error :
    print(error)
except ValueError as error :
    print(error)