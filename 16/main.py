import easygui
import time

AOCDAY = "16"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    aunts = {}
    for line in lines:
        terms = line.split(" ")
        aunts[terms[1][0:-1]] = {}
        for i in range(2, len(terms)-2, 2):
            aunts[terms[1][0:-1]][terms[i][0:-1]] = int(terms[i+1][0:-1])
        aunts[terms[1][0:-1]][terms[-2][0:-1]] = int(terms[-1])
    return aunts

def part1(lines):
    aunts = parseLines(lines)
    match = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0,
                "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    for aunt in list(aunts.keys()):
        auntMatch = True
        for key in aunts[aunt].keys():
            if key in match:
                if aunts[aunt][key] != match[key]:
                    auntMatch = False
        if auntMatch:
            return(f"The Aunt to thank is {aunt}.")

def part2(lines):
    aunts = parseLines(lines)
    match = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0,
                "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    greater = ["cats", "trees"]
    lesser = ["pomeranians", "goldfish"]
    for aunt in list(aunts.keys()):
        auntMatch = True
        for key in aunts[aunt].keys():
            if key in match:
                if key in greater:
                    if aunts[aunt][key] <= match[key]:
                        auntMatch = False
                elif key in lesser:
                    if aunts[aunt][key] >= match[key]:
                        auntMatch = False
                elif aunts[aunt][key] != match[key]:
                    auntMatch = False
        if auntMatch:
            return(f"The Aunt to thank is {aunt}.")

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