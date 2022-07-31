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
    return(int(vals[16][:-1]), int(vals[18][:-1]))

def codeCount(row, column):
    num = row + column - 2
    sum = (num * (num + 1)) // 2
    return sum + column

def codeCalc(codeNum):
    calcNum = 20151125
    for i in range(1, codeNum):
        calcNum = (calcNum * 252533) % 33554393
    return calcNum

def part1(lines):
    row, column = parseLines(lines)
    codeNum = codeCount(row, column)
    return(f"The code at row {row}, column {column} is {codeCalc(codeNum)}.")

def main ():
    fileName = easygui.fileopenbox(default=f"./"+AOCDAY+"/"+"*.txt")
    lines = readFile(fileName)
    p1StartTime = time.perf_counter()
    p1Result = part1(lines)
    p1EndTime = time.perf_counter()
    print("Advent of Code 2015 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))

main()