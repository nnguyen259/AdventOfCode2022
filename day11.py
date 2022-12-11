def part1():
    with open("input/day11.txt") as input:
        data = input.read()

    monkeys = [str.split(i, "\n")[1:] for i in data.split("\n\n")]

    inventories = [[] for _ in range(len(monkeys))]
    operands = []
    operation_number = []
    test_number = []
    test_true = []
    test_false = []

    activity_count = [0 for i in range(len(monkeys))]

    for i, monkey in enumerate(monkeys):
        inventory = map(int, monkey[0].split(": ")[-1].split(", "))
        inventories[i].extend(inventory)

        _, operand, number = monkey[1].split("= ")[1].split(" ")
        operands.append(operand)
        if number == "old":
            operation_number.append(number)
        else:
            operation_number.append(int(number))

        test_number.append(int(monkey[2].split("by ")[1]))
        test_true.append(int(monkey[3].split("monkey ")[1]))
        test_false.append(int(monkey[4].split("monkey ")[1]))

    for _ in range(20):
        for i, inventory in enumerate(inventories):
            activity_count[i] += len(inventory)
            while len(inventory) > 0:
                item = inventory.pop(0)
                if operation_number[i] == "old":
                    number = item
                else:
                    number = operation_number[i]

                worry = eval(f"{item} {operands[i]} {number}") // 3
                if worry % test_number[i] == 0:
                    inventories[test_true[i]].append(worry)
                else:
                    inventories[test_false[i]].append(worry)

    activity_count.sort(reverse=True)
    return activity_count[0] * activity_count[1]


def part2():
    with open("input/day11.txt") as input:
        data = input.read()

    monkeys = [str.split(i, "\n")[1:] for i in data.split("\n\n")]

    inventories = [[] for _ in range(len(monkeys))]
    operands = []
    operation_number = []
    test_number = []
    test_true = []
    test_false = []

    divisor_prod = 1

    activity_count = [0 for i in range(len(monkeys))]

    for i, monkey in enumerate(monkeys):
        inventory = map(int, monkey[0].split(": ")[-1].split(", "))
        inventories[i].extend(inventory)

        _, operand, number = monkey[1].split("= ")[1].split(" ")
        operands.append(operand)
        if number == "old":
            operation_number.append(number)
        else:
            operation_number.append(int(number))

        divisor_number = int(monkey[2].split("by ")[1])
        divisor_prod *= divisor_number
        test_number.append(divisor_number)
        test_true.append(int(monkey[3].split("monkey ")[1]))
        test_false.append(int(monkey[4].split("monkey ")[1]))

    for _ in range(10000):
        for i, inventory in enumerate(inventories):
            activity_count[i] += len(inventory)
            while len(inventory) > 0:
                item = inventory.pop(0) % divisor_prod
                if operation_number[i] == "old":
                    number = item
                else:
                    number = operation_number[i]

                worry = eval(f"{item} {operands[i]} {number}")
                if worry % test_number[i] == 0:
                    inventories[test_true[i]].append(worry)
                else:
                    inventories[test_false[i]].append(worry)

    activity_count.sort(reverse=True)
    return activity_count[0] * activity_count[1]


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
