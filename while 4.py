i = 1

while i <= 4:
    spaces = 4 - i
    space_count = 0
    while space_count < spaces:
        print(" ", end="")
        space_count += 1
    j = 1
    while j <= (2 * i - 1):
        print("o", end="")
        j += 1
    print()
    i += 1