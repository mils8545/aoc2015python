import easygui
import time

AOCDAY = "24"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    integers = []
    for line in lines:
        integers.append(int(line))
    return(integers)

def quantumCalc(integers):
    total = 1
    for i in integers:
        total *= i
    return(total)

def part1(lines):
    packages = parseLines(lines)
    total = sum(packages)
    target = total // 3

    groupings = [[]]
    for package in packages:
        for grouping in groupings:
            if package not in grouping:
                if package + sum(grouping) <= target:
                    groupings.append(grouping + [package])
    
    goodGroupings = []
    for grouping in groupings:
        if sum(grouping) == target:
            goodGroupings.append(grouping)
    
    minLength = len(packages)
    for grouping in goodGroupings:
        if len(grouping) < minLength:
            minLength = len(grouping)

    groupings = []

    for grouping in goodGroupings:
        if len(grouping) == minLength:
            groupings.append(grouping)

    groupings.sort(key=lambda x: quantumCalc(x))
    return(f"The quantum entanglement of the best arrangement is {quantumCalc(groupings[0])}")

def part2(lines):
    packages = parseLines(lines)
    total = sum(packages)
    target = total // 4

    groupings = [[]]
    for package in packages:
        for grouping in groupings:
            if package not in grouping:
                if package + sum(grouping) <= target:
                    groupings.append(grouping + [package])
    
    goodGroupings = []
    for grouping in groupings:
        if sum(grouping) == target:
            goodGroupings.append(grouping)
    
    minLength = len(packages)
    for grouping in goodGroupings:
        if len(grouping) < minLength:
            minLength = len(grouping)

    groupings = []

    for grouping in goodGroupings:
        if len(grouping) == minLength:
            groupings.append(grouping)

    groupings.sort(key=lambda x: quantumCalc(x))
    return(f"The quantum entanglement of the best arrangement is {quantumCalc(groupings[0])}")

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