# Arguments are lists. Function is true if lists have at least
# a single element in common

def overlapping(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False