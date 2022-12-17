def part1():
    with open("input/day16.txt") as input:
        data = input.read().splitlines()

    nodes = {}
    distances = {}
    has_flow = {}
    for line in data:
        valve = line.split(" ")[1]
        dests = line.rsplit("to valve")[-1].replace("s ", "").replace(" ", "").split(",")
        flow = int(line.split("=")[-1].split(";")[0])

        if valve not in nodes:
            nodes[valve] = {"flow": flow, "dest": dests}
            distances[valve] = {valve: 0}

        if flow > 0:
            has_flow[valve] = flow

    for valve in nodes:
        visited = set()
        todo = nodes[valve]["dest"]
        i = 1
        while todo:
            temp = list()
            for destination in todo:
                if destination in visited:
                    continue

                visited.add(destination)
                if destination not in distances[valve]:
                    distances[valve][destination] = i
                    distances[destination][valve] = i
                else:
                    distances[valve][destination] = min(i, distances[valve][destination])
                    distances[destination][valve] = min(i, distances[valve][destination])

                temp.extend([node for node in nodes[destination]["dest"] if node not in visited and node != valve])

            i += 1
            todo = temp

    for node in distances:
        distances[node].pop(node)

    distances = {key: {k: v for k, v in value.items() if k in has_flow} for key, value in distances.items() if key in ("AA", *has_flow)}

    pressures = []
    paths = []
    todo = [(30, 0, ["AA"])]
    while todo:
        t, p, path = todo.pop()
        current = path[-1]
        temp_todo = []
        for node, distance in distances[current].items():
            if distance > t - 2 or node in path:
                continue
            tt = t - distance - 1
            pp = p + has_flow[node] * tt
            s = tt, pp, path + [node]
            temp_todo.append(s)
        if temp_todo:
            todo.extend(temp_todo)
        else:
            pressures.append(p)
            # paths always start at AA, so no need to keep first location
            paths.append(path[1:])

    return max(pressures)


def part2():
    with open("input/day16.txt") as input:
        data = input.read().splitlines()


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
