def simulate(hx, hy, tx, ty, direction=None):
    if direction == "R":
        hx += 1
        if hx - tx > 1:
            tx = hx - 1
            if hy != ty:
                ty = hy
        return hx, hy, tx, ty
    if direction == "L":
        hx -= 1
        if tx - hx > 1:
            tx = hx + 1
            if hy != ty:
                ty = hy
        return hx, hy, tx, ty
    if direction == "U":
        hy += 1
        if hy - ty > 1:
            ty = hy - 1
            if hx != tx:
                tx = hx
        return hx, hy, tx, ty
    if direction == "D":
        hy -= 1
        if ty - hy > 1:
            ty = hy + 1
            if hx != tx:
                tx = hx
        return hx, hy, tx, ty

    if hy - ty in (-2, 2):
        ty += (hy - ty) // 2
        if hx > tx:
            tx += 1
        elif hx < tx:
            tx -= 1
    elif hx - tx in (-2, 2):
        tx += (hx - tx) // 2
        if hy > ty:
            ty += 1
        elif hy < ty:
            ty -= 1

    return hx, hy, tx, ty


def part1():
    with open("input/day9.txt") as input:
        data = input.read().splitlines()

    visited = set()
    visited.add((0, 0))
    hx = hy = tx = ty = 0

    for line in data:
        direction, steps = line.split(" ")
        for _ in range(int(steps)):
            hx, hy, tx, ty = simulate(hx, hy, tx, ty, direction)
            visited.add((tx, ty))
    return len(visited)


def part2():
    with open("input/day9.txt") as input:
        data = input.read().splitlines()

    visited = set()
    visited.add((0, 0))
    ropes = [[0, 0] for _ in range(10)]

    for line in data:
        direction, steps = line.split(" ")
        for _ in range(int(steps)):
            i = 0
            hx = ropes[i][0]
            hy = ropes[i][1]
            tx = ropes[i + 1][0]
            ty = ropes[i + 1][1]
            hx, hy, tx, ty = simulate(hx, hy, tx, ty, direction)

            ropes[i][0] = hx
            ropes[i][1] = hy
            ropes[i + 1][0] = tx
            ropes[i + 1][1] = ty
            i += 1

            while i < 9:
                hx = ropes[i][0]
                hy = ropes[i][1]
                tx = ropes[i + 1][0]
                ty = ropes[i + 1][1]
                hx, hy, tx, ty = simulate(hx, hy, tx, ty)

                ropes[i][0] = hx
                ropes[i][1] = hy
                ropes[i + 1][0] = tx
                ropes[i + 1][1] = ty
                i += 1

            visited.add((ropes[-1][0], ropes[-1][1]))
    return len(visited)


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
