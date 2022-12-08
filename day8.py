def part1():
    with open("input/day8.txt") as input:
        data = input.read().splitlines()

    rows = len(data)
    cols = len(data[0])

    trees = [[] for _ in range(rows)]
    for i, row in enumerate(data):
        for tree in row:
            trees[i].append(int(tree))

    trees2 = [*zip(*trees)]

    output = 0

    for i, row in enumerate(trees):
        for j, tree in enumerate(row):
            if i in (0, rows - 1) or j in (0, cols - 1):
                output += 1
                continue

            if max(row[0:j]) < tree or max(row[j + 1 : cols]) < tree:
                output += 1
                continue

            col = trees2[j]
            if max(col[0:i]) < tree or max(col[i + 1 : rows]) < tree:
                output += 1
                continue
    return output


def part2():
    with open("input/day8.txt") as input:
        data = input.read().splitlines()

    rows = len(data)
    cols = len(data[0])

    trees = [[] for _ in range(rows)]
    for i, row in enumerate(data):
        for tree in row:
            trees[i].append(int(tree))

    trees2 = [*zip(*trees)]

    score = 0

    for i, row in enumerate(trees):
        if i in (0, rows - 1):
            continue
        for j, tree in enumerate(row):
            if j in (0, cols - 1):
                continue
            col = trees2[j]
            top = down = left = right = 1

            left_j = j - 1
            while left_j >= 1 and row[left_j] < tree:
                left += 1
                left_j -= 1

            right_j = j + 1
            while right_j < cols - 1 and row[right_j] < tree:
                right += 1
                right_j += 1

            top_i = i - 1
            while top_i >= 1 and col[top_i] < tree:
                top += 1
                top_i -= 1

            down_i = i + 1
            while down_i < rows - 1 and col[down_i] < tree:
                down += 1
                down_i += 1
            if (top * down * left * right) > score:
                score = top * down * left * right

    return score


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
