def symbol_generator(i, j, symbol_type):
    if symbol_type == 'star':
        return '* '
    elif symbol_type == 'number':
        return f'{j + 1} '
    elif symbol_type == 'alpha':
        return f'{chr(65 + j)} '
    return '# '  # default fallback


def triangle(rows, symbol_type, align='left', reverse=False):
    rng = range(1, rows + 1) if not reverse else range(rows, 0, -1)
    for i in rng:
        line = ''
        if align == 'right':
            line += ' ' * (rows - i) * 2
        for j in range(i):
            line += symbol_generator(i, j if symbol_type == 'number' or symbol_type == 'alpha' else i, symbol_type)
        print(line)


def pyramid(rows, symbol_type, reverse=False):
    rng = range(1, rows + 1) if not reverse else range(rows, 0, -1)
    for i in rng:
        line = ' ' * (rows - i)
        for j in range(i):
            line += symbol_generator(i, j, symbol_type)
        print(line)


def diamond(rows, symbol_type):
    pyramid(rows, symbol_type)
    pyramid(rows - 1, symbol_type, reverse=True)


def main():
    print("🎨 Pattern Generator")
    rows = int(input("Enter number of rows: "))

    print("\nSelect pattern type:")
    print("1. Left Triangle")
    print("2. Right Triangle")
    print("3. Inverted Left Triangle")
    print("4. Inverted Right Triangle")
    print("5. Centered Pyramid")
    print("6. Inverted Pyramid")
    print("7. Diamond")
    pattern_choice = int(input("Enter choice (1-7): "))

    print("\nSelect symbol type:")
    print("1. * (star)")
    print("2. Numbers")
    print("3. Alphabets")
    symbol_map = {1: 'star', 2: 'number', 3: 'alpha'}
    symbol_choice = int(input("Enter choice (1-3): "))
    symbol_type = symbol_map.get(symbol_choice, 'star')

    print("\nGenerated Pattern:\n")

    if pattern_choice == 1:
        triangle(rows, symbol_type, align='left', reverse=False)
    elif pattern_choice == 2:
        triangle(rows, symbol_type, align='right', reverse=False)
    elif pattern_choice == 3:
        triangle(rows, symbol_type, align='left', reverse=True)
    elif pattern_choice == 4:
        triangle(rows, symbol_type, align='right', reverse=True)
    elif pattern_choice == 5:
        pyramid(rows, symbol_type)
    elif pattern_choice == 6:
        pyramid(rows, symbol_type, reverse=True)
    elif pattern_choice == 7:
        diamond(rows, symbol_type)
    else:
        print("Invalid pattern choice.")


if __name__ == "__main__":
    main()

    