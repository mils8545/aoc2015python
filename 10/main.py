import easygui
import time

AOCDAY = "10"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def stepString(string):
    newString = ""
    lastChar = ""
    lastCount = 0
    for i in range(len(string)):
        if string[i] == lastChar:
            lastCount += 1
        else:
            newString += str(lastCount) if lastCount > 0 else ""
            newString += lastChar
            lastChar = string[i]
            lastCount = 1
    newString += str(lastCount)
    newString += lastChar
    return newString

def part1(lines):
    curString = lines[0]
    for i in range(40):
        curString = stepString(curString)

    return(f"The result is {len(curString)} in length.")

def part2(lines):
    curString = lines[0]
    for i in range(50):
        curString = stepString(curString)

    return(f"The result is {len(curString)} in length.")

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