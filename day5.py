def part1():
    with open("input/day5.txt") as input:
        data = input.read().splitlines()

    data.reverse()
    line = data.pop()

    size = (len(line) + 1) // 4
    containers = [[] for _ in range(size)]

    while line != "":
        for i in range(size):
            if line[i * 4] == "[":
                containers[i].insert(0, line[i * 4 + 1])
        line = data.pop()

    line = data.pop()
    while line:
        _, count, _, source, _, dest = line.split(" ")
        for _ in range(int(count)):
            containers[int(dest) - 1].append(containers[int(source) - 1].pop())
        if not len(data):
            break
        line = data.pop()

    output = ""
    for container in containers:
        output += container[-1]
    return output


def part2():
    with open("input/day5.txt") as input:
        data = input.read().splitlines()

    data.reverse()
    line = data.pop()

    size = (len(line) + 1) // 4
    containers = [[] for _ in range(size)]

    while line != "":
        for i in range(size):
            if line[i * 4] == "[":
                containers[i].insert(0, line[i * 4 + 1])
        line = data.pop()

    line = data.pop()
    while line:
        _, count, _, source, _, dest = line.split(" ")
        tmp = list()
        for _ in range(int(count)):
            tmp.insert(0, containers[int(source) - 1].pop())
        containers[int(dest) - 1].extend(tmp)
        if not len(data):
            break
        line = data.pop()

    output = ""
    for container in containers:
        output += container[-1]
    return output


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
