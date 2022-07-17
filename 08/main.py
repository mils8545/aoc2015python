import easygui
import time

AOCDAY = "08"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def charCount(string):
    count = 0
    string = string.replace("\\\\", "!")
    for i in range(len(string)):
        if string[i] == '\\':
            if string[i+1] == 'x':
                count -= 2
        elif not string[i] == ' ':
            count += 1
    return count - 2

def part1(lines):
    totalMemChars = 0
    totalPrintChars = 0
    for line in lines:
        totalMemChars += charCount(line)
        totalPrintChars += len(line)
    return(f"The difference in mem vs print charachters is {totalPrintChars - totalMemChars}.")

def part2(lines):
    totalExpandedChars = 0
    totalPrintChars = 0
    for line in lines:
        expandedLine = line[1:-1]
        expandedLine = expandedLine.replace("\\", "\\\\")
        expandedLine = expandedLine.replace("\"", "\\\"")
        expandedLine = "\"\\\"" + expandedLine +  "\\\"\""
        totalExpandedChars += len(expandedLine)
        totalPrintChars += len(line)
    return(f"The difference in expanded and original charachters is {totalExpandedChars - totalPrintChars}.")


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