# Return True if a vowel is given, otherwise, return False

def vowel(character):
    if len(character) == 1 and character in 'aeiou':
        return True
    else:
        return False

if __name__ == "__main__":
    character = input('Type a character: ')
    print(vowel(character))