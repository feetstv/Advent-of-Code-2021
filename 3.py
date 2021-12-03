lines = open("3.txt", "r+").readlines()


def p1(lines):
    """Calculates gamma and epsilon rates, returned as a tuple."""
    columns = [[line[i] for line in lines] for i in range(len(lines[0]) - 1)]
    g = int("".join([max(column, key=column.count) for column in columns]), 2)
    e = int("".join([min(column, key=column.count) for column in columns]), 2)

    return g * e


def p2(lines):
    o_lines = lines.copy()
    co2_lines = lines.copy()

    def calculate_rate(calc_lines, o=True):
        one = "1" if o else "0"
        zero = "0" if o else "1"
        visited = []
        while len(calc_lines) > 1:
            columns = [[line[i] for line in calc_lines]
                       for i in range(len(calc_lines[0]) - 1)]
            for i, column in enumerate(columns):
                if not i in visited:
                    old_len = len(calc_lines)
                    val = one if column.count(
                        "1") >= column.count("0") else zero
                    calc_lines = [
                        line for line in calc_lines if line[i] == val]
                    visited.append(i)
                    if not old_len == len(calc_lines):
                        break
        return int(calc_lines[0], 2)

    o = calculate_rate(o_lines, True)
    co2 = calculate_rate(co2_lines, False)

    return o * co2


print(f"DAY THREE\nPart one: {p1(lines)}\nPart two: {p2(lines)}")
