def part1():
    with open("input/day1.txt") as input:
        data = input.readlines()

    max_weight = 0
    current_weight = 0

    for line in data:
        if line == "\n":
            if current_weight > max_weight:
                max_weight = current_weight
            current_weight = 0
        else:
            weight = line.replace("\n", "")
            current_weight += int(weight)

    if current_weight > max_weight:
        return current_weight
    else:
        return max_weight


def part2():
    with open("input/day1.txt") as input:
        data = input.readlines()

    weights = list()
    current_weight = 0

    for line in data:
        if line == "\n":
            weights.append(current_weight)
            current_weight = 0
        else:
            weight = line.replace("\n", "")
            current_weight += int(weight)

    weights.append(current_weight)
    weights.sort()
    return sum(weights[-3:])


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
