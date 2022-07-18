import easygui
import time

AOCDAY = "18"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    grid = []
    for line in lines:
        gridLine = []
        for char in line:
            gridLine.append(True if char == "#" else False)
        grid.append(gridLine)
    return grid

def stepGrid(grid):
    newGrid = []
    for i in range(len(grid)):
        newGridLine = []
        for j in range(len(grid[i])):
            neighbourCount = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    if (k!=0 or l!=0) and i + k >= 0 and j + l >= 0 and i+k < len(grid) and j + l < len(grid[i]) and grid[i+k][j+l]:
                        neighbourCount += 1
            if grid[i][j]:
                newGridLine.append(True if neighbourCount >= 2 and neighbourCount <= 3 else False)
            else:
                newGridLine.append(True if neighbourCount == 3 else False)
        newGrid.append(newGridLine)
    return newGrid

def lightCount(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                count += 1
    return count

def part1(lines):
    grid = parseLines(lines)
    STEPS = 100
    for i in range(STEPS):
        grid = stepGrid(grid)
    lights = lightCount(grid)
    return(f"The number of lights lit after {STEPS} steps is {lights}.")

def part2(lines):
    grid = parseLines(lines)
    STEPS = 100
    for i in range(STEPS):
        grid = stepGrid(grid)
        grid[0][0] = True
        grid[0][len(grid[0])-1] = True
        grid[len(grid)-1][0] = True
        grid[len(grid)-1][len(grid[0])-1] = True
    lights = lightCount(grid)
    return(f"The number of lights lit after {STEPS} steps is {lights}.")

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