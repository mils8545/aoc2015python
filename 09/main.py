import easygui
import time

AOCDAY = "09"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    pathDict = {}
    for line in lines:
        terms = line.split(" ")
        if terms[0] not in pathDict:
            pathDict[terms[0]] = {}
        pathDict[terms[0]][terms[2]] = int(terms[4])
        if terms[2] not in pathDict:
            pathDict[terms[2]] = {}
        pathDict[terms[2]][terms[0]] = int(terms[4])
    return pathDict

def dfsStep(pathDict, currentPath, paths, targetLength):
    if len(currentPath) == targetLength:
        paths.append(currentPath)
        return paths
    for connection in list(pathDict[currentPath[-1]].keys()):
        if connection not in currentPath:
            paths = dfsStep(pathDict, currentPath + [connection], paths, targetLength)
    return paths

def pathCost(pathDict, path):
    totalCost = 0
    for i in range(len(path)-1):
        totalCost += pathDict[path[i]][path[i+1]]
    return totalCost

def part1(lines):
    pathDict = parseLines(lines)
    cities = []
    for city in list(pathDict.keys()):
        cities.append(city)
    paths = []
    for city in cities:
        paths = dfsStep(pathDict, [city], paths, len(cities))
    pathCosts = []
    for path in paths:
        pathCosts.append(pathCost(pathDict, path))
    return(f"The shortest path to all locations is {min(pathCosts)}.")

def part2(lines):
    pathDict = parseLines(lines)
    cities = []
    for city in list(pathDict.keys()):
        cities.append(city)
    paths = []
    for city in cities:
        paths = dfsStep(pathDict, [city], paths, len(cities))
    pathCosts = []
    for path in paths:
        pathCosts.append(pathCost(pathDict, path))
    return(f"The longest path to all locations is {max(pathCosts)}.")

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