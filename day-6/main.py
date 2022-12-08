def part1(input):
    charsProcessed = 4
    for i in range(3, len(input)):
        firstCheck = (
            input[i] != input[i - 1]
            and input[i] != input[i - 2]
            and input[i] != input[i - 3]
        )
        secondCheck = input[i - 1] != input[i - 2] and input[i - 1] != input[i - 3]
        thirdCheck = input[i - 2] != input[i - 3]
        if firstCheck and secondCheck and thirdCheck:
            break
        else:
            charsProcessed += 1
    print("Part 1:")
    print(charsProcessed)


def part2(input):
    charsProcessed = 14
    for i in range(len(input) - 14):
        substring = input[i : i + 14]
        letters = []
        for letter in substring:
            if letter not in letters:
                letters.append(letter)
                if len(letters) == 14:
                    print("Part 2:")
                    print(charsProcessed)
                    return
            else:
                charsProcessed += 1
                break


def main():
    inputFile = open("day-6/input.txt")
    input = inputFile.readline()
    part1(input)
    part2(input)
    inputFile.close()


if __name__ == "__main__":
    main()
