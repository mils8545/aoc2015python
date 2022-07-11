import easygui
import time

from numpy import true_divide

AOCDAY = "05"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1NaughtyCheck(line):
    naughtyCombo = ["ab", "cd", "pq", "xy"]
    vowelCount = 0
    for i in range(len(line)):
        if line[i] in "aeiou":
            vowelCount += 1
    doubleLetter = False
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            doubleLetter = True
    naughtyComboFound = False
    for combo in naughtyCombo:
        if combo in line:
            naughtyComboFound = True
    return (vowelCount < 3 or (not doubleLetter) or naughtyComboFound)    

def doubleDuoCheck(line):
    duoDict = {}
    doubleDuo = False
    for i in range(len(line)-1):
        duo = line[i] + line[i+1]
        if (duo) in duoDict:
            duoDict[duo] += 1
            if line[i-1] == line[i] and line[i-1] == line[i+1]:
                duoDict[duo] -= 1
        else:
            duoDict[duo] = 1
    for key in duoDict:
        if duoDict[key] > 1:
            doubleDuo = True
    return doubleDuo

def part2NaughtyCheck(line):
    doubleDuo = doubleDuoCheck(line)
    quad = False
    for i in range(len(line)-3):
        if line[i] == line[i+1] and line[i] == line[i+2] and line[i] == line[i+3]:
            quad = True
    spacedDuo = False
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            spacedDuo = True

    return (not ((doubleDuo or quad) and spacedDuo))    

def part1(lines):
    niceCount = 0
    for line in lines:
        if not part1NaughtyCheck(line):
            niceCount += 1
    return(f"There are {niceCount} nice strings.")
        
def part2(lines):
    niceCount = 0
    for line in lines:
        if not part2NaughtyCheck(line):
            niceCount += 1
    return(f"There are {niceCount} nice strings.")

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