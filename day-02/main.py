SCORING_CHOICE = {"rock": 1, "paper": 2, "scissors": 3}
SCORING_RESULT = {"win": 6, "draw": 3, "lose": 0}


def part1(input):

    totalScore = 0
    for entry in input:
        e = entry.strip("\n").split()
        if e[0] == "A":
            if e[1] == "X":
                score = SCORING_RESULT["draw"] + SCORING_CHOICE["rock"]
            elif e[1] == "Y":
                score = SCORING_RESULT["win"] + SCORING_CHOICE["paper"]
            elif e[1] == "Z":
                score = SCORING_RESULT["lose"] + SCORING_CHOICE["scissors"]
        elif e[0] == "B":
            if e[1] == "X":
                score = SCORING_RESULT["lose"] + SCORING_CHOICE["rock"]
            elif e[1] == "Y":
                score = SCORING_RESULT["draw"] + SCORING_CHOICE["paper"]
            elif e[1] == "Z":
                score = SCORING_RESULT["win"] + SCORING_CHOICE["scissors"]
        elif e[0] == "C":
            if e[1] == "X":
                score = SCORING_RESULT["win"] + SCORING_CHOICE["rock"]
            elif e[1] == "Y":
                score = SCORING_RESULT["lose"] + SCORING_CHOICE["paper"]
            elif e[1] == "Z":
                score = SCORING_RESULT["draw"] + SCORING_CHOICE["scissors"]
        totalScore += score

    print("Part 1:")
    print(totalScore)


def part2(input):
    totalScore = 0
    for entry in input:
        e = entry.strip("\n").split()
        if e[0] == "A":  # rock
            if e[1] == "X":
                score = SCORING_RESULT["lose"] + SCORING_CHOICE["scissors"]
            elif e[1] == "Y":
                score = SCORING_RESULT["draw"] + SCORING_CHOICE["rock"]
            elif e[1] == "Z":
                score = SCORING_RESULT["win"] + SCORING_CHOICE["paper"]
        elif e[0] == "B":  # paper
            if e[1] == "X":
                score = SCORING_RESULT["lose"] + SCORING_CHOICE["rock"]
            elif e[1] == "Y":
                score = SCORING_RESULT["draw"] + SCORING_CHOICE["paper"]
            elif e[1] == "Z":
                score = SCORING_RESULT["win"] + SCORING_CHOICE["scissors"]
        elif e[0] == "C":  # scissors
            if e[1] == "X":
                score = SCORING_RESULT["lose"] + SCORING_CHOICE["paper"]
            elif e[1] == "Y":
                score = SCORING_RESULT["draw"] + SCORING_CHOICE["scissors"]
            elif e[1] == "Z":
                score = SCORING_RESULT["win"] + SCORING_CHOICE["rock"]
        totalScore += score

    print("Part 2:")
    print(totalScore)


def __main__():
    inputFile = open("day-02/input.txt")
    input = inputFile.readlines()
    part1(input)
    part2(input)
    inputFile.close()


if __name__ == "__main__":
    __main__()
