def getPriority(letter):
    if letter.isupper():
        return 27 + ord(letter) - ord("A")
    elif letter.islower():
        return 1 + ord(letter) - ord("a")


def part1(input):
    totalPriority = 0

    for entry in input:
        entryNew = entry.strip("\n")
        priority = 0
        half = int(len(entryNew) / 2)
        firstCompartment = entryNew[0:half:]
        secondCompartment = entryNew[half : len(entryNew) :]
        for letter in firstCompartment:
            if letter in secondCompartment:
                priority += getPriority(letter)
                break
        totalPriority += priority

    print("Part 1:")
    print(totalPriority)


def part2(input):
    totalPriority = 0

    for i in range(0, len(input), 3):
        priority = 0
        firstRucksack = input[i].strip("\n")
        secondRucksack = input[i + 1].strip("\n")
        thirdRucksack = input[i + 2].strip("\n")
        for letter in firstRucksack:
            if letter in secondRucksack and letter in thirdRucksack:
                priority += getPriority(letter)
                break
        totalPriority += priority

    print("Part 2:")
    print(totalPriority)


def main():
    inputFile = open("day-03/input.txt")
    input = inputFile.readlines()
    part1(input)
    part2(input)
    inputFile.close()


if __name__ == "__main__":
    main()
