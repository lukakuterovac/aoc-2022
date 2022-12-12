def part1(input):
    overlapCount = 0
    for entry in input:
        formatedEntry = entry.strip("\n").split(",")
        firstSection = formatedEntry[0].split("-")
        secondSection = formatedEntry[1].split("-")
        if int(firstSection[0]) <= int(secondSection[0]) and int(
            firstSection[1]
        ) >= int(secondSection[1]):
            overlapCount += 1
        elif int(secondSection[0]) <= int(firstSection[0]) and int(
            secondSection[1]
        ) >= int(firstSection[1]):
            overlapCount += 1
    print("Part 1:")
    print(overlapCount)


def part2(input):
    overlapCount = 0
    for entry in input:
        formatedEntry = entry.strip("\n").split(",")
        firstSection = formatedEntry[0].split("-")
        secondSection = formatedEntry[1].split("-")
        firstRange = range(int(firstSection[0]), int(firstSection[1]) + 1)
        secondRange = range(int(secondSection[0]), int(secondSection[1]) + 1)
        for num in firstRange:
            if num in secondRange:
                overlapCount += 1
                break
    print("Part 2:")
    print(overlapCount)


def main():
    inputFile = open("day-4/input.txt")
    input = inputFile.readlines()
    part1(input)
    part2(input)
    inputFile.close()


if __name__ == "__main__":
    main()
