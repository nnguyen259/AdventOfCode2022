def left_possible(shape, x, y, stack):
    if x == 0:
        return False

    if shape == 0:
        return stack[y][x - 1] == "."

    if shape == 1:
        return stack[y][x] == "." and stack[y - 1][x - 1] == "." and stack[y - 2][x] == "."

    if shape == 2:
        return stack[y][x - 1] == "." and stack[y - 1][x + 1] == "." and stack[y - 2][x + 1] == "."

    if shape == 3:
        return stack[y][x - 1] == "." and stack[y - 1][x - 1] == "." and stack[y - 2][x - 1] == "." and stack[y - 3][x - 1] == "."

    if shape == 4:
        return stack[y][x - 1] == "." and stack[y - 1][x - 1] == "."


def right_possible(shape, x, y, stack):
    if shape == 0:
        if x + 4 > 6:
            return False
        return stack[y][x + 4] == "."

    if shape == 1:
        if x + 3 > 6:
            return False
        return stack[y][x + 2] == "." and stack[y - 1][x + 3] == "." and stack[y - 2][x + 2] == "."

    if shape == 2:
        if x + 3 > 6:
            return False
        return stack[y][x + 3] == "." and stack[y - 1][x + 3] == "." and stack[y - 2][x + 3] == "."

    if shape == 3:
        if x + 1 > 6:
            return False
        return stack[y][x + 1] == "." and stack[y - 1][x + 1] == "." and stack[y - 2][x + 1] == "." and stack[y - 3][x + 1] == "."

    if shape == 4:
        if x + 2 > 6:
            return False
        return stack[y][x + 2] == "." and stack[y - 1][x + 2] == "."


def down_possible(shape, x, y, stack):
    if y == -1:
        return False

    if shape == 0:
        return stack[y + 1][x] == "." and stack[y + 1][x + 1] == "." and stack[y + 1][x + 2] == "." and stack[y + 1][x + 3] == "."

    if shape == 1:
        return stack[y][x] == "." and stack[y + 1][x + 1] == "." and stack[y][x + 2] == "."

    if shape == 2:
        return stack[y + 1][x] == "." and stack[y + 1][x + 1] == "." and stack[y + 1][x + 2] == "."

    if shape == 3:
        return stack[y + 1][x] == "."

    if shape == 4:
        return stack[y + 1][x] == "." and stack[y + 1][x + 1] == "."


def shape_max_height(shape, y):
    y = -y

    if shape == 0:
        return y

    if shape == 1:
        return y + 2

    if shape == 2:
        return y + 2

    if shape == 3:
        return y + 3

    if shape == 4:
        return y + 1


def fill_stack(shape, x, y, stack):
    if shape == 0:
        stack[y][x] = "@"
        stack[y][x + 1] = "@"
        stack[y][x + 2] = "@"
        stack[y][x + 3] = "@"

    if shape == 1:
        stack[y][x + 1] = "@"
        stack[y - 1][x] = "@"
        stack[y - 1][x + 1] = "@"
        stack[y - 1][x + 2] = "@"
        stack[y - 2][x + 1] = "@"

    if shape == 2:
        stack[y][x] = "@"
        stack[y][x + 1] = "@"
        stack[y][x + 2] = "@"
        stack[y - 1][x + 2] = "@"
        stack[y - 2][x + 2] = "@"

    if shape == 3:
        stack[y][x] = "@"
        stack[y - 1][x] = "@"
        stack[y - 2][x] = "@"
        stack[y - 3][x] = "@"

    if shape == 4:
        stack[y][x] = "@"
        stack[y][x + 1] = "@"
        stack[y - 1][x] = "@"
        stack[y - 1][x + 1] = "@"


def part1():
    with open("input/day17.txt") as input:
        data = input.read()

    max_height = 0
    length = len(data)
    stack = [["." for _ in range(7)] for _ in range(10)]

    shape = 0
    step = 0
    for i in range(2022):
        x = 2
        y = -(max_height + 4)

        while True:
            direction = data[step % length]
            step += 1
            if direction == "<" and left_possible(shape, x, y, stack):
                x -= 1

            if direction == ">" and right_possible(shape, x, y, stack):
                x += 1

            if not down_possible(shape, x, y, stack):
                break

            y += 1

        max_height = max(max_height, shape_max_height(shape, y))
        fill_stack(shape, x, y, stack)

        if len(stack) - max_height <= 7:
            temp = [["." for _ in range(7)] for _ in range(10)]
            temp.extend(stack)
            stack = temp

        shape = (shape + 1) % 5

    return max_height


def part2():
    with open("input/day17.txt") as input:
        data = input.read()

    max_height = 0
    length = len(data)
    stack = [["." for _ in range(7)] for _ in range(10)]

    shape = 0
    step = 0
    for i in range(1000000000000):
        x = 2
        y = -(max_height + 4)

        while True:
            direction = data[step % length]
            step += 1
            if direction == "<" and left_possible(shape, x, y, stack):
                x -= 1

            if direction == ">" and right_possible(shape, x, y, stack):
                x += 1

            if not down_possible(shape, x, y, stack):
                break

            y += 1

        max_height = max(max_height, shape_max_height(shape, y))
        fill_stack(shape, x, y, stack)

        if len(stack) - max_height <= 7:
            temp = [["." for _ in range(7)] for _ in range(10)]
            temp.extend(stack)
            stack = temp

        shape = (shape + 1) % 5

    return max_height


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
