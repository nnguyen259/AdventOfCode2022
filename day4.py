def part1():
    with open("input/day4.txt") as input:
        data = input.read().splitlines()

    count = 0
    for line in data:
        first, second = line.split(",")
        fmin, fmax = map(int, first.split("-"))
        smin, smax = map(int, second.split("-"))

        if (smin >= fmin and smax <= fmax) or (fmin >= smin and fmax <= smax):
            count += 1

    return count


def part2():
    with open("input/day4.txt") as input:
        data = input.read().splitlines()

    count = 0
    for line in data:
        first, second = line.split(",")
        fmin, fmax = map(int, first.split("-"))
        smin, smax = map(int, second.split("-"))

        if (
            (fmin <= smin <= fmax)
            or (fmin <= smax <= fmax)
            or (smin <= fmax <= smax)
            or (smin <= fmin <= smax)
        ):
            count += 1

    return count


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
