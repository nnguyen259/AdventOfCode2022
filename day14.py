def part1():
    with open("input/day14.txt") as input:
        data = input.read().splitlines()

    cave = [["." for _ in range(600)] for _ in range(200)]
    abyss = 0

    for line in data:
        walls = line.split(" -> ")
        for i, wall in enumerate(walls[:-1]):
            x, y = map(int, wall.split(","))
            if i == 0:
                if y > abyss:
                    abyss = y
                cave[y][x - 450] = "#"

            x2, y2 = map(int, walls[i + 1].split(","))
            if y2 > abyss:
                abyss = y2
            if x2 == x:
                if y < y2:
                    for j in range(y, y2 + 1):
                        cave[j][x - 450] = "#"
                else:
                    for j in range(y2, y + 1):
                        cave[j][x - 450] = "#"

            if y2 == y:
                if x < x2:
                    for j in range(x, x2 + 1):
                        cave[y][j - 450] = "#"
                else:
                    for j in range(x2, x + 1):
                        cave[y][j - 450] = "#"

    result = 0
    while True:
        x = 50
        y = 0
        cave[y][x] = "o"

        while True:
            if y >= abyss:
                return result

            if cave[y + 1][x] == ".":
                cave[y][x], cave[y + 1][x] = cave[y + 1][x], cave[y][x]
                y += 1
                continue

            if cave[y + 1][x - 1] == ".":
                cave[y][x], cave[y + 1][x - 1] = cave[y + 1][x - 1], cave[y][x]
                y += 1
                x -= 1
                continue

            if cave[y + 1][x + 1] == ".":
                cave[y][x], cave[y + 1][x + 1] = cave[y + 1][x + 1], cave[y][x]
                y += 1
                x += 1
                continue
            break

        result += 1


def part2():
    with open("input/day14.txt") as input:
        data = input.read().splitlines()

    cave = [["." for _ in range(600)] for _ in range(200)]
    abyss = 0

    for line in data:
        walls = line.split(" -> ")
        for i, wall in enumerate(walls[:-1]):
            x, y = map(int, wall.split(","))
            if i == 0:
                if y > abyss:
                    abyss = y
                cave[y][x - 450] = "#"

            x2, y2 = map(int, walls[i + 1].split(","))
            if y2 > abyss:
                abyss = y2
            if x2 == x:
                if y < y2:
                    for j in range(y, y2 + 1):
                        cave[j][x - 450] = "#"
                else:
                    for j in range(y2, y + 1):
                        cave[j][x - 450] = "#"

            if y2 == y:
                if x < x2:
                    for j in range(x, x2 + 1):
                        cave[y][j - 450] = "#"
                else:
                    for j in range(x2, x + 1):
                        cave[y][j - 450] = "#"

    result = 0
    while True:
        x = 50
        y = 0
        if cave[y][x] == "o":
            return result
        else:
            cave[y][x] = "o"

        while True:
            if y == abyss + 1:
                break

            if cave[y + 1][x] == ".":
                cave[y][x], cave[y + 1][x] = cave[y + 1][x], cave[y][x]
                y += 1
                continue

            if cave[y + 1][x - 1] == ".":
                cave[y][x], cave[y + 1][x - 1] = cave[y + 1][x - 1], cave[y][x]
                y += 1
                x -= 1
                continue

            if cave[y + 1][x + 1] == ".":
                cave[y][x], cave[y + 1][x + 1] = cave[y + 1][x + 1], cave[y][x]
                y += 1
                x += 1
                continue
            break

        result += 1


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
