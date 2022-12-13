from functools import cmp_to_key


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b

    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)

    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])

    result = 0
    for i in range(min(len(a), len(b))):
        result = compare(a[i], b[i])
        if result:
            return result

    return len(a) - len(b)


def part1():
    with open("input/day13.txt") as input:
        data = input.read().split("\n\n")

    output = 0

    for i, pair in enumerate(data):
        left, right = map(eval, pair.split("\n"))

        result = compare(left, right)
        if result < 0:
            output += i + 1

    return output


def part2():
    with open("input/day13.txt") as input:
        data = list(
            map(eval, [line for line in input.read().splitlines() if line != ""])
        )

    data.extend([[[2]], [[6]]])

    data.sort(key=cmp_to_key(compare))
    return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
