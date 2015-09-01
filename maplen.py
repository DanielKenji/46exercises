# maps a list of words into a list of integers
# of the lenghts of the words.

def maplen(listwords):
    listsize = []
    for word in listwords:
        listsize.append(len(word))
    return listsize

