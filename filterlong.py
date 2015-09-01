# Receives a list of words and an integer n. 
# Then return a list of the words longer than n.

def filter_long_words(words, n):
    longlist = []
    for element in words:
        if len(element) > n:
            longlist.append(element)
    return longlist
    

    