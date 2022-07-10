import easygui
import time

AOCDAY = "03"

def readFile(fileName):
    with open(fileName, "r") as file:
        return file.readlines()

def part1(lines):
    inputString = lines[0]
    moves = {"<": [-1, 0], ">": [1, 0], "^": [0, -1], "v": [0, 1]}
    pos = [0,0]
    visited = ["0:0"]
    for move in inputString:
        pos[0] += moves[move][0]
        pos[1] += moves[move][1]
        if str(pos[0]) + ":" + str(pos[1]) not in visited:
            visited.append(str(pos[0]) + ":" + str(pos[1]))
    return(f"Santa visited {len(visited)} houses")

def part2(lines):
    inputString = lines[0]
    moves = {"<": [-1, 0], ">": [1, 0], "^": [0, -1], "v": [0, 1]}
    pos = [[0,0],[0,0]]

    visited = ["0:0"]
    for i in range(len(inputString)):
        pos[i%2][0] += moves[inputString[i]][0]
        pos[i%2][1] += moves[inputString[i]][1]
        if str(pos[i%2][0]) + ":" + str(pos[i%2][1]) not in visited:
            visited.append(str(pos[i%2][0]) + ":" + str(pos[i%2][1]))
    return(f"Santa visited {len(visited)} houses")

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