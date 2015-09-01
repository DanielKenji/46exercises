# Words must be a list. Returns the lenght of the longest word in a list

import sys

def find_longest_word(words):
    long = 0
    for word in words:
        if len(word) > long:
            long = len(word)
    return long
    
if __name__ == "__main__":
    words = list(sys.argv[1:])
    print(find_longest_word(words))
    