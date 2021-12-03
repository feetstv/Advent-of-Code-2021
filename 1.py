def p1(lines):
    """
    Zip each item with the next item, then compare them. If the next item
    is greater than the previous, add an item to a list, then count the length
    of the list. Saves having to import functools.
    """
    lines = zip(lines, lines[1:])
    return len([1 for x, y in lines if y > x])


# Read the lines in from the text file for both parts.
lines = [int(line) for line in open("1.txt", "r+").readlines()]
# Sum the first, second, and third numbers in sequence together for part two.
sums = [x + y + z for x, y, z in zip(lines, lines[1:], lines[2:])]

# Print the answers.
print(f"DAY ONE\nPart one: {p1(lines)}\nPart two: {p1(sums)}")
