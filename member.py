# Is something a member of a sequence? Poor man's in keyword.
# x is a value, a is a sequence.

def is_member(x, a):
    for element in a:
        if element == x:
            return True
    return False
    
