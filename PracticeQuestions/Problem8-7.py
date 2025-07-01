# Write a python function to remove a given word from a list ad strip it at the same time.

def remove_element(li, word):
    nl = []
    for item in li:
        if not (item == word):
            nl.append(item.strip(word))
            # li.remove(item)
    return nl

lists = ["hanRohan", "Kamal", "Reigns", "han"]

new_list = remove_element(lists, "han")

print(new_list)
    