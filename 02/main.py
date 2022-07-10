import easygui
import time

AOCDAY = "02"

def readFile(fileName):
    with open(fileName, "r") as file:
        return file.readlines()

def part1(lines):
    dimensions = [line.split("x") for line in lines]
    faceAreas = []
    paperTotal = 0
    for i in range(len(dimensions)):
        #dimensions[i] = list(map(int, dimensions[i]))
        dimensions[i] = [int(dim) for dim in dimensions[i]]
        faceAreas.append([dimensions[i][0]*dimensions[i][1], 
            dimensions[i][0]*dimensions[i][2], 
            dimensions[i][1]*dimensions[i][2]])

    for i in range(len(faceAreas)):
        paperTotal += 2*sum(faceAreas[i]) + min(faceAreas[i])
    return(f"Total paper required is {paperTotal}")

def part2(lines):
    dimensions = [line.split("x") for line in lines]
    faceCircumferences = []
    ribbonTotal = 0
    for i in range(len(dimensions)):
        #dimensions[i] = list(map(int, dimensions[i]))
        dimensions[i] = [int(dim) for dim in dimensions[i]]
        faceCircumferences.append([(dimensions[i][0]+dimensions[i][1])*2,
            (dimensions[i][0]+dimensions[i][2])*2,
            (dimensions[i][1]+dimensions[i][2])*2])  

    for i in range(len(dimensions)):
        ribbonTotal += min(faceCircumferences[i]) + (dimensions[i][0]*dimensions[i][1]*dimensions[i][2])
    return(f"Total ribbon required is {ribbonTotal}")

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