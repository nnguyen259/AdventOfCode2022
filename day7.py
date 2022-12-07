def part1():
    with open("input/day7.txt") as input:
        data = input.read().splitlines()

    pwd = []
    sizes = {}

    for line in data:
        match line.split(" "):
            case "$", "cd", "/":
                pwd = []
            case "$", "cd", "..":
                pwd.pop()
            case "$", "cd", name:
                pwd.append(name)
            case "$", "ls":
                pass
            case "dir", _:
                pass
            case size, _:
                for i in range(len(pwd)):
                    folder = ".".join(pwd[0 : i + 1])
                    if folder not in sizes:
                        sizes[folder] = 0
                    sizes[folder] += int(size)

    output = sum([x for x in sizes.values() if x < 100000])
    return output


def part2():
    with open("input/day7.txt") as input:
        data = input.read().splitlines()

    current_dir = "/"
    folders = {"/": {"parent": "", "total_size": 0}}

    for line in data:
        if line.startswith("$"):
            if line.startswith("$ cd"):
                _, command, option = line.split(" ")
                if command == "cd":
                    if option == "/":
                        current_dir = "/"
                    elif option == "..":
                        current_dir = f"{current_dir.rsplit('/', maxsplit=2)[0]}/"
                    else:
                        current_dir += f"{option}/"
        else:
            size, name = line.split(" ")
            new_dir = f"{current_dir}{name}/"
            if size == "dir":
                if new_dir not in folders:
                    folders[new_dir] = {
                        "parent": current_dir,
                        "total_size": 0,
                    }
                else:
                    print("weird", line)
            else:
                size = int(size)
                folders[current_dir]["total_size"] += size
                parent_dir = folders[current_dir]["parent"]
                while parent_dir != "":
                    folders[parent_dir]["total_size"] += size
                    parent_dir = folders[parent_dir]["parent"]

    space_left = 70000000 - folders["/"]["total_size"]
    space_needed = 30000000 - space_left

    current_min_size = folders["/"]["total_size"]

    for folder in folders.values():
        if (
            folder["total_size"] >= space_needed
            and folder["total_size"] <= current_min_size
        ):
            current_min_size = folder["total_size"]

    return current_min_size


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
