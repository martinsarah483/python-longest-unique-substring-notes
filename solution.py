def longest(text):
    positions = {}
    start = 0
    best = ''
    for index, char in enumerate(text):
        start = max(start, positions.get(char, -1) + 1)
        positions[char] = index
        if index + 1 - start > len(best):
            best = text[start:index+1]
    return best

def solve(value):
    return longest(value)
