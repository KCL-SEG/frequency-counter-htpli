"""Frequencies function."""

def frequencies(items):
    frequencies = {}
    for item in items:
        if isinstance(item, str):   #if item is string
            frequencies[item] = frequencies.get(item, 0) + 1
        else:
            item_str = str(item)
            frequencies[item_str] = frequencies.get(item_str, 0) + 1
    return frequencies