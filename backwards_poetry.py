poem1 = ["hello", "whatsup", "go"]

def lines_printed_backwards(poem):
    ''' returns text words in backwards order. takes a list of strings. '''
    #  get the poem , be able to access each element. access the last one. append it to new list. 

    backwards = []
    length = len(poem) - 1
    enum_poem = [(word) for word in enumerate(poem)]
    print(enum_poem)
    print(length)
    
    for word in poem:
        backwards.append(poem[length])
        length -= 1

    backwards = (' ').join(backwards)
    return print(backwards)

lines_printed_backwards(poem1)