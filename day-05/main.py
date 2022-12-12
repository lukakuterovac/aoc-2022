def parseCrates(crates):
    cratesParsed = {}
    for i in range(1, 10):
        cratesParsed[i] = ""
    for i in range(0, len(crates) - 1):
        for j in range(1, 10):
            letter = crates[i][(j - 1) * 4 + 1]
            if letter.isupper():
                cratesParsed[j] += letter
    for i in range(1, 10):
        cratesParsed[i] = list(map(str, cratesParsed[i]))
    return cratesParsed


def part1(crates, moves):
    cratesParsed = parseCrates(crates)
    message = ""
    for line in moves:
        move = line.split()
        count = int(move[1])
        point1 = int(move[3])
        point2 = int(move[5])
        for i in range(count):
            crate = cratesParsed[point1].pop(0)
            cratesParsed[point2].insert(0, crate)
    for i in range(1, 10):
        message += cratesParsed[i][0]
    print("Part 1:")
    print(message)


def part2(crates, moves):
    cratesParsed = parseCrates(crates)
    message = ""
    for line in moves:
        move = line.split()
        count = int(move[1])
        point1 = int(move[3])
        point2 = int(move[5])
        crateStack = []
        for i in range(count):
            crateStack.append(cratesParsed[point1].pop(0))
        crateStack.reverse()
        for crate in crateStack:
            cratesParsed[point2].insert(0, crate)
    for i in range(1, 10):
        message += cratesParsed[i][0]
    print("Part 2:")
    print(message)


def main():
    inputFile = open("day-05/input.txt")
    input = inputFile.readlines()
    crates = input[0:9]
    moves = input[10:]
    part1(crates, moves)
    part2(crates, moves)
    inputFile.close()


if __name__ == "__main__":
    main()
