"""Frequencies function."""

def frequencies(*args):
    frequencies = {}
    
    item_list = [*args]
    string_list = [str(item) for item in item_list]
    #print(string_list)
    
    for str_item in string_list:
        if(str_item in frequencies):
            frequencies[str_item] += 1
        else:
            frequencies[str_item] = 1
    
    return frequencies

print(frequencies(1, 7, 7, 7, 8, 8, 'Hello, World!', False))
