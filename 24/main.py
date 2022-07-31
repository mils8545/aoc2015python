import easygui
import time

AOCDAY = "25"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    vals = lines[0].split(" ")
    return(int(vals[15][:-1]), int(vals[17][:-1]))

def code_count(row, column):
    num = row * range - 2
    sum = num * (num + 1) / 2
    return sum + column

def part1(lines):
    row, column = parseLines(lines)
    print(row, column)

    #return(f"The quantum entanglement of the best arrangement is {quantumCalc(groupings[0])}")

def part2(lines):
    pass

def main ():
    fileName = easygui.fileopenbox(default=f"./"+AOCDAY+"/"+"*.txt")
    lines = readFile(fileName)
    p1StartTime = time.perf_counter()
    p1Result = part1(lines)
    p1EndTime = time.perf_counter()
    print("Advent of Code 2015 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    p2StartTime = time.perf_counter()
    p2Result = part2(lines)
    p2EndTime = time.perf_counter()
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()