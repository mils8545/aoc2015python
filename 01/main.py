import easygui
import time

AOCDAY = "01"

def readFile(fileName):
    with open(fileName, "r") as file:
        return file.readlines()

def part1(lines):
    inputString = lines[0]
    count = 0
    values = {"(": 1, ")": -1}
    for i in range(len(inputString)):
        if inputString[i] in values:
            count += values[inputString[i]]
    return(f"Ending score is {count}")

def part2(lines):
    inputString = lines[0]
    count = 0
    values = {"(": 1, ")": -1}
    for i in range(len(inputString)):
        if inputString[i] in values:
            count += values[inputString[i]]
        if count < 0:
            return f"Santa entered the basement on position {i+1}"
    return(f"Santa never entered the basement")

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
    print("  Part 1 Execution Time: " + str(round(p1EndTime - p1StartTime,4)) + " seconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " + str(round(p2EndTime - p2StartTime,4)) + " seconds")
    print("  Part 2 Result: " + str(p2Result))

main()