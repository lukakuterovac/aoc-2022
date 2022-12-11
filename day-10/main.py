def parseInput(line):
    formatedLine = line.strip("\n").split()
    if formatedLine[0] == "noop":
        return [1, 0]
    elif formatedLine[0] == "addx":
        return [2, int(formatedLine[1])]


def part1(input):
    x = 1
    cycles = [20, 60, 100, 140, 180, 220]
    cycleCount = 0
    signalStrengths = []
    commands = []
    for line in input:
        commands.append(parseInput(line))
    for command in commands:
        for _ in range(0, command[0]):
            cycleCount += 1
            if len(cycles) == 0:
                break
            if cycleCount == cycles[0]:
                signalStrengths.append(x * cycles[0])
                cycles.pop(0)
        x += command[1]
    print("Part 1:")
    print(sum(signalStrengths))


def part2(input):
    x = 1
    crtImage = []
    row = ""
    sprite = "." * (x - 1) + "#" * 3 + "." * (40 - x - 2)
    commands = []
    for line in input:
        commands.append(parseInput(line))
    for _ in range(0, 6):
        for cycle in range(0, 40):
            if sprite[cycle] == "#":
                row += "#"
            else:
                row += " "
            commands[0][0] -= 1
            if commands[0][0] == 0:
                x += commands[0][1]
                sprite = "." * (x - 1) + "#" * 3 + "." * (40 - x - 2)
                commands.pop(0)
        crtImage.append(row)
        row = ""
    print("Part 2:")
    for row in crtImage:
        print(row)


def main():
    inputFile = open("day-10/input.txt")
    input = inputFile.readlines()
    part1(input)
    part2(input)
    inputFile.close()


if __name__ == "__main__":
    main()
