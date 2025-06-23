# Striping



def rem(list, word):

    n = []

    for item in list:
        if not(item == word):

            # list.remove(word)
            n.append(item.strip(word))
        
    return n

list = ["Mayur", "Solom", "Suraj", "om"]
print(rem(list, "om"))

