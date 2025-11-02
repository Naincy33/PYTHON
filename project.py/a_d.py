d = {"f":10, "a":15, "c":20, "e":25, "b":30, "d":35}
a_d = dict(sorted(d.items()))
print(a_d)

def check_values(d):
    if 15 in d.values() and 20 in d.values():
        return True
    else:
        return False

result = check_values(a_d)
print("Contains 15 and 20?", result)