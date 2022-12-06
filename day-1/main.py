def part1(input):
    elves = []
    elf = []

    for entry in input:
        if entry == "\n":
            elves.append(elf)
            elf = []
        else:
            elf.append(int(entry.strip("\n")))

    allCalories = []
    for e in elves:
        calories = 0
        for calorie in e:
            calories += calorie
        allCalories.append(calories)
    allCalories.sort(reverse=True)

    print("Part 1:")
    print(allCalories[0])
    return allCalories


def part2(allCalories):
    print("Part 2:")
    print(allCalories[0] + allCalories[1] + allCalories[2])


def __main__():
    inputFile = open("day-1/input.txt")
    input = inputFile.readlines()
    allCalories = part1(input)
    part2(allCalories)


if __name__ == "__main__":
    __main__()
