import numpy


def parseInput(input):
    for i in range(len(input)):
        input[i] = input[i].strip("\n")
        input[i] = list(map(int, input[i]))
    return input


def checkVisibility(tree, row):
    for height in row:
        if tree <= height:
            return False
    return True


def calculateScenicScore(tree, row):
    counter = 0
    for i in range(0, len(row)):
        if row[i] >= tree:
            counter += 1
            break
        else:
            counter += 1
    return counter


def reverseList(list):
    return list[::-1]


def part1(input):
    transposedInput = numpy.transpose(input)
    visibleTrees = 0
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            tree = input[i][j]
            leftSide = input[i][0:j]
            rightSide = input[i][j + 1 : len(input[i])]
            topSide = transposedInput[j][0:i]
            bottomSide = transposedInput[j][i + 1 : len(transposedInput[j])]
            if (
                checkVisibility(tree, leftSide)
                or checkVisibility(tree, rightSide)
                or checkVisibility(tree, topSide)
                or checkVisibility(tree, bottomSide)
            ):
                visibleTrees += 1
    print("Part 1:")
    print(visibleTrees)


def part2(input):
    transposedInput = numpy.transpose(input).tolist()
    maxScenicScore = 0
    for i in range(1, len(input) - 1):
        for j in range(1, len(input[i]) - 1):
            tree = input[i][j]
            leftSide = input[i][0:j]
            rightSide = input[i][j + 1 : len(input[i])]
            topSide = transposedInput[j][0:i]
            bottomSide = transposedInput[j][i + 1 : len(transposedInput[i])]
            left = calculateScenicScore(tree, reverseList(leftSide))
            right = calculateScenicScore(tree, rightSide)
            top = calculateScenicScore(tree, reverseList(topSide))
            bottom = calculateScenicScore(tree, bottomSide)
            treeScenicScore = left * right * top * bottom
            if treeScenicScore > maxScenicScore:
                maxScenicScore = treeScenicScore
    print("Part 2:")
    print(maxScenicScore)


def main():
    inputFile = open("day-8/input.txt")
    input = inputFile.readlines()
    parsedInput = parseInput(input)
    part1(parsedInput)
    part2(parsedInput)
    inputFile.close()


if __name__ == "__main__":
    main()
