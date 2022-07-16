import easygui
import time

AOCDAY = "06"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    instructions = []
    for line in lines:
        terms = line.split(" ")
        # print(terms)
        if terms[0][1] == "u":
            instructions.append({"type": terms[1], "start": [int(terms[2].split(",")[0]),int(terms[2].split(",")[1])], "end": [int(terms[4].split(",")[0]),int(terms[4].split(",")[1])]})
        else:
            # instructions.append({"type": terms[0], "start": terms[1], "end": terms[3]})
            instructions.append({"type": terms[0], "start": [int(terms[1].split(",")[0]),int(terms[1].split(",")[1])], "end": [int(terms[3].split(",")[0]),int(terms[3].split(",")[1])]})
    return instructions

def part1(lines):
    instructions = parseLines(lines)
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for instruction in instructions:
        for x in range(instruction["start"][0], instruction["end"][0]+1):
            for y in range(instruction["start"][1], instruction["end"][1]+1):
                if instruction["type"] == "on":
                    grid[x][y] = 1
                elif instruction["type"] == "off":
                    grid[x][y] = 0
                elif instruction["type"] == "toggle":
                    grid[x][y] = (grid[x][y] + 1) % 2
    total = 0
    for x in range(1000):
        for y in range(1000):
            total += grid[x][y]
    return(f"There are a total of {total} lights on.")

def part2(lines):
    instructions = parseLines(lines)
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for instruction in instructions:
        for x in range(instruction["start"][0], instruction["end"][0]+1):
            for y in range(instruction["start"][1], instruction["end"][1]+1):
                if instruction["type"] == "on":
                    grid[x][y] += 1
                elif instruction["type"] == "off":
                    grid[x][y] = 0 if grid[x][y] == 0 else grid[x][y] - 1
                elif instruction["type"] == "toggle":
                    grid[x][y] += 2
    total = 0
    for x in range(1000):
        for y in range(1000):
            total += grid[x][y]
    return(f"The total brightness is {total}.")

def main ():
    fileName = easygui.fileopenbox(default=f"./"+AOCDAY+"/"+"*.txt")
    lines = readFile(fileName)
    p1StartTime = time.perf_counter()
    p1Result = part1(lines)
    p1EndTime = time.perf_counter()
    p2StartTime = time.perf_counter()
    p2Result = part2(lines)
    p2EndTime = time.perf_counter()
    print("Advent of Code 2015 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()