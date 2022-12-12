def part1():
    with open("input/day12.txt") as input:
        data = input.read().splitlines()

    height = len(data)
    width = len(data[0])

    startx = starty = endx = endy = None
    terrain_num = [[0 for _ in range(width)] for _ in range(height)]
    steps = [[-1 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            char = data[y][x]

            if char == "S":
                starty, startx = y, x
                char = "a"
                steps[y][x] = 0

            if char == "E":
                endy, endx = y, x
                char = "z"

            terrain_num[y][x] = ord(char) - ord("a")

    next_step = [(starty, startx)]
    while True:
        temp = list()
        for stepy, stepx in next_step:
            for y, x in [
                (stepy + 1, stepx),
                (stepy - 1, stepx),
                (stepy, stepx + 1),
                (stepy, stepx - 1),
            ]:
                if y in (-1, height) or x in (-1, width):
                    continue
                if terrain_num[y][x] in range(
                    terrain_num[stepy][stepx] + 2,
                ):
                    if steps[y][x] == -1 or (
                        steps[y][x] > steps[stepy][stepx] + 1
                        and terrain_num[y][x] > terrain_num[stepy][stepx]
                    ):
                        steps[y][x] = steps[stepy][stepx] + 1
                        temp.append((y, x))

        next_step = temp
        if len(next_step) == 0:
            break
    return steps[endy][endx]


def part2():
    with open("input/day12.txt") as input:
        data = input.read().splitlines()

    height = len(data)
    width = len(data[0])

    startx = starty = endx = endy = None
    terrain_num = [[0 for _ in range(width)] for _ in range(height)]

    start_pos = list()
    for y in range(height):
        for x in range(width):
            char = data[y][x]

            if char in ("S", "a"):
                starty, startx = y, x
                char = "a"
                start_pos.append((y, x))

            if char == "E":
                endy, endx = y, x
                char = "z"

            terrain_num[y][x] = ord(char) - ord("a")

    results = list()
    for starty, startx in start_pos:
        steps = [[-1 for _ in range(width)] for _ in range(height)]
        steps[starty][startx] = 0
        next_step = [(starty, startx)]
        while True:
            temp = list()
            for stepy, stepx in next_step:
                for y, x in [
                    (stepy + 1, stepx),
                    (stepy - 1, stepx),
                    (stepy, stepx + 1),
                    (stepy, stepx - 1),
                ]:
                    if y in (-1, height) or x in (-1, width):
                        continue
                    if terrain_num[y][x] in range(
                        terrain_num[stepy][stepx] + 2,
                    ):
                        if steps[y][x] == -1 or (
                            steps[y][x] > steps[stepy][stepx] + 1
                            and terrain_num[y][x] > terrain_num[stepy][stepx]
                        ):
                            steps[y][x] = steps[stepy][stepx] + 1
                            temp.append((y, x))

            next_step = temp
            if len(next_step) == 0:
                break
        if steps[endy][endx] != -1:
            results.append(steps[endy][endx])
    return min(results)


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
