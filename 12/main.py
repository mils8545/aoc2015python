import easygui
import time
import json

AOCDAY = "12"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1TotalJSON(json, total):
    for element in json:
        if type(element) == int:
            total += element
        elif type(element) == list:
            total = part1TotalJSON(element, total)
        elif type(element) == dict:
            total = part1TotalJSON(element.values(), total)
    return total

def part2TotalJSON(json, total):
    for element in json:
        if type(element) == int:
            total += element
        elif type(element) == list:
            total = part2TotalJSON(element, total)
        elif type(element) == dict:
            if "red" not in element.values():
                total = part2TotalJSON(element.values(), total)
    return total

def part1(lines):
    curString = lines[0]
    total = part1TotalJSON(json.loads(curString).values(), 0)
    return(f"The total of all the numbers in the string is {total}.")

def part2(lines):
    curString = lines[0]
    total = part2TotalJSON(json.loads(curString).values(), 0)
    return(f"The total of all the numbers in the string is {total}.")

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