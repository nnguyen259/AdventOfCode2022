def part1():
    with open("input/day10.txt") as input:
        data = input.read().splitlines()

    cycles = [1]
    for line in data:
        cycles.append(cycles[-1])
        if line.startswith("addx"):
            amount = int(line.split(" ")[1])
            cycles.append(cycles[-1] + amount)

    output = 0

    for i, amount in enumerate(cycles[19::40]):
        output += (20 + 40 * i) * amount
    return output


def part2():
    with open("input/day10.txt") as input:
        data = input.read().splitlines()

    cycles = [1]
    output = ["" for _ in range(6)]
    for line in data:
        cycles.append(cycles[-1])
        if line.startswith("addx"):
            amount = int(line.split(" ")[1])
            cycles.append(cycles[-1] + amount)

    for i, amount in enumerate(cycles):
        line = i // 40
        if line > 5:
            break

        if (i % 40) in (amount, amount + 1, amount - 1):
            output[line] += "#"
        else:
            output[line] += "."

    for line in output:
        print(line)


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
