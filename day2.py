def part1():
    scores = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3, 0: 3, 1: 6, 2: 0}
    with open("input/day2.txt") as input:
        data = input.read().splitlines()

    score = 0

    for line in data:
        opponent, player = line.split(" ")
        score += scores[player]
        score += scores[(scores[player] - scores[opponent]) % 3]
    return score


def part2():
    scores = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}
    with open("input/day2.txt") as input:
        data = input.read().splitlines()

    score = 0
    for line in data:
        opponent, player = line.split(" ")
        score += scores[player]
        if player == "X":
            tmp = scores[opponent] + 2
            if tmp <= 3:
                score += tmp
            else:
                score += tmp % 3
        elif player == "Y":
            score += scores[opponent]
        else:
            tmp = scores[opponent] + 1
            if tmp <= 3:
                score += tmp
            else:
                score += tmp % 3
    return score


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
