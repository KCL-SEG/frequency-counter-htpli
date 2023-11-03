"""Frequencies function."""

def frequencies(*args):
    frequencies = {}
    for item in args:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies

# print(frequencies(1, 7, 7, 7, 8, 8, 'Hello, World!', False))
# print(frequencies('0', 4,4,'4','d','d','e',0,'a','d','4'))
# print(frequencies('a', 'a', 'b', 'b', 'b', 'c'))
# print(frequencies(100, 'Hello', '100', '100', 100))
# print(frequencies(''))
# print(frequencies())