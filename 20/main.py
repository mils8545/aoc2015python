import easygui
import time

AOCDAY = "20"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    targetNumber = int(lines[0])
    houses = []
    for i in range(1,targetNumber+1):
        houses.append(0)
    for i in range (1, targetNumber // 40 + 1):
        for j in range(i, targetNumber // 40 + 1, i):
            houses[j] += i * 10
    for i in range(len(houses)):
        if houses[i] >= targetNumber:
            return f"The first house that receives at least {targetNumber} presents is {i}."

def part2(lines):
    targetNumber = int(lines[0])
    houses = []
    for i in range(1,targetNumber+1):
        houses.append(0)
    for i in range (1, targetNumber // 40 + 1):
        for j in range(i, min(i * 50 + 1, targetNumber // 40), i):
            houses[j] += i * 11
    for i in range(len(houses)):
        if houses[i] >= targetNumber:
            return f"The first house that receives at least {targetNumber} presents is {i}."

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