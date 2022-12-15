def check(x, y, sensor):
    sx, sy, distance = sensor
    if y < 0 or y > 4000000:
        return True
    return (abs(x - sx) + abs(y - sy)) <= distance


def part1(y=2000000):
    with open("input/day15.txt") as input:
        data = input.read().splitlines()

    impossible = set()
    beacons = set()
    for line in data:
        sensor, beacon = [(i.split(" ")[2:]) for i in line.split(": closest beacon ")]
        sensor_x, sensor_y = (int(i.split("=")[-1].replace(",", "")) for i in sensor)
        beacon_x, beacon_y = (int(i.split("=")[-1].replace(",", "")) for i in beacon)

        if beacon_y == y:
            beacons.add(beacon_y)

        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        if (sensor_y - distance) <= y <= (sensor_y + distance):
            distance_x = distance - abs(sensor_y - y)
            for i in range(sensor_x - distance_x, sensor_x + distance_x + 1):
                if i not in beacons:
                    impossible.add(i)

    return len(impossible)


def part2():
    with open("input/day15.txt") as input:
        data = input.read().splitlines()

    sensors = list()
    for line in data:
        sensor, beacon = [(i.split(" ")[2:]) for i in line.split(": closest beacon ")]
        sensor_x, sensor_y = (int(i.split("=")[-1].replace(",", "")) for i in sensor)
        beacon_x, beacon_y = (int(i.split("=")[-1].replace(",", "")) for i in beacon)

        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        sensors.append((sensor_x, sensor_y, distance))

    for sensor in sensors:
        x, y, distance = sensor
        distance += 1

        for x2 in range(max(0, x - distance), min(4000000, x + distance + 1)):
            distance_y = distance - abs(x - x2)

            if any([check(x2, y - distance_y, sensor2) for sensor2 in sensors if sensor2 != sensor]):
                if any([check(x2, y + distance_y, sensor2) for sensor2 in sensors if sensor2 != sensor]):
                    continue
                else:
                    return 4000000 * x2 + (y + distance_y)

            else:
                return 4000000 * x2 + (y - distance_y)


if __name__ == "__main__":
    print(f"Part1={part1()}")
    print(f"Part2={part2()}")
