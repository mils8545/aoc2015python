import easygui
import time
import random
from random import shuffle

AOCDAY = "19"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    replacements = {}
    for line in lines[:-2]:
        terms = line.split(" => ")
        if terms[0] not in replacements:
            replacements[terms[0]] = []
        replacements[terms[0]].append(terms[1])
    chemical = lines[-1]
    return chemical, replacements

def part1(lines):
    chemical, replacements = parseLines(lines)
    newChemicals = []
    for i in range(len(chemical)):
        if chemical[i] in replacements:
            for replacement in replacements[chemical[i]]:
                newChemical = chemical[:i] + replacement + chemical[i+1:]
                if newChemical not in newChemicals:
                    newChemicals.append(newChemical)
    for i in range(len(chemical)-1):
        if chemical[i:i+2] in replacements:
            for replacement in replacements[chemical[i:i+2]]:
                newChemical = chemical[:i] + replacement + chemical[i+2:]
                if newChemical not in newChemicals:
                    newChemicals.append(newChemical)
    return(f"The number of possible chemicals after 1 substitution is {len(newChemicals)}.")

def part2(lines):
    count = 0
    chemical, replacements = parseLines(lines)
    reps = []
    for source in list(replacements.keys()):
        for target in replacements[source]:
            reps.append((source, target))

    testChemical = chemical
    while testChemical != "e":
        lastChemical = testChemical
        for source, target in reps:
            if target in testChemical:
                count += 1
                testChemical = testChemical.replace(target, source, 1)

    return(f"The number of steps to get from e to the chemical is {count}.")

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