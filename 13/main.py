import easygui
import time

AOCDAY = "13"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    relationshipDict = {}
    for line in lines:
        terms = line.split(" ")
        if terms[0] not in relationshipDict:
            relationshipDict[terms[0]] = {}
        relationshipDict[terms[0]][terms[10][0:-1]] = int(terms[3]) if terms[2] == "gain" else -int(terms[3])
    return relationshipDict

def dfsStep(relationshipDict, currentTable, seatingPlans, targetLength):
    if len(currentTable) == targetLength:
        seatingPlans.append(currentTable)
        return seatingPlans
    for guest in list(relationshipDict.keys()):
        if guest not in currentTable:
            seatingPlans = dfsStep(relationshipDict, currentTable + [guest], seatingPlans, targetLength)
    return seatingPlans

def seatingPlanCost(relationshipDict, seatingPlan):
    totalCost = 0
    for i in range(len(seatingPlan)-1):
        totalCost += relationshipDict[seatingPlan[i]][seatingPlan[i+1]]
        totalCost += relationshipDict[seatingPlan[i+1]][seatingPlan[i]]
    totalCost += relationshipDict[seatingPlan[-1]][seatingPlan[0]]
    totalCost += relationshipDict[seatingPlan[0]][seatingPlan[-1]]
    return totalCost

# def pathCost(pathDict, path):
#     totalCost = 0
#     for i in range(len(path)-1):
#         totalCost += pathDict[path[i]][path[i+1]]
#     return totalCost

def part1(lines):
    relationshipDict = parseLines(lines)
    guests = list(relationshipDict.keys())
    seatingPlans = []

    for guest in guests:
        seatingPlans = dfsStep(relationshipDict, [guest], seatingPlans, len(guests))
    seatingPlanCosts = []
    for seatingPlan in seatingPlans:
        seatingPlanCosts.append(seatingPlanCost(relationshipDict, seatingPlan))
    return(f"The best seating plan provides {max(seatingPlanCosts)} happiness units.")

def part2(lines):
    relationshipDict = parseLines(lines)
    for guest in list(relationshipDict.keys()):
        relationshipDict[guest]["Me"] = 0
    relationshipDict["Me"] = {}
    for guest in relationshipDict:
        relationshipDict["Me"][guest] = 0
    guests = list(relationshipDict.keys())
    seatingPlans = []

    for guest in guests:
        seatingPlans = dfsStep(relationshipDict, [guest], seatingPlans, len(guests))
    seatingPlanCosts = []
    for seatingPlan in seatingPlans:
        seatingPlanCosts.append(seatingPlanCost(relationshipDict, seatingPlan))
    return(f"The best seating plan provides {max(seatingPlanCosts)} happiness units.")

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