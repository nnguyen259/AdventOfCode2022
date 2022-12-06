def part1():
    with open("input/day6.txt") as input:
        data = input.read()

    for i in range(len(data)):
        if i < 3:
            continue
        if len(set(data[i - 3 : i + 1])) == 4:
            return i + 1


def part2():
    with open("input/day6.txt") as input:
        data = input.read()

    for i in range(len(data)):
        if i < 13:
            continue
        if len(set(data[i - 13 : i + 1])) == 14:
            return i + 1


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
