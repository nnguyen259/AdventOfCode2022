def part1():
    with open("input/day3.txt") as input:
        data = input.read().splitlines()

    output = 0
    for line in data:
        first, second = line[: len(line) // 2], line[len(line) // 2 :]
        char = set(first).intersection(set(second)).pop()
        if "a" <= char <= "z":
            output += 1 + ord(char) - ord("a")
        else:
            output += 27 + ord(char) - ord("A")
    return output


def part2():
    with open("input/day3.txt") as input:
        data = input.read().splitlines()

    output = 0
    for i in range(len(data) // 3):
        first, second, third = data[3 * i], data[3 * i + 1], data[3 * i + 2]
        char = set(first).intersection(set(second)).intersection(set(third)).pop()
        if "a" <= char <= "z":
            output += 1 + ord(char) - ord("a")
        else:
            output += 27 + ord(char) - ord("A")
    return output


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
