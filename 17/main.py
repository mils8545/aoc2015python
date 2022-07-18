import easygui
import time

AOCDAY = "17"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    sizes = []
    for line in lines:
        sizes.append(int(line))
    return sizes

def calcPermutations(sizes, currentPermutation, permutations, GOAL):
    if sum(currentPermutation) > GOAL:
        return permutations
    if sum(currentPermutation) == GOAL:
        return permutations + [currentPermutation]
    for i in range(len(sizes)):
        newPermutation = currentPermutation + [sizes[i]]
        permutations = calcPermutations(sizes[i+1:], newPermutation, permutations, GOAL)
    return permutations

def part1(lines):
    sizes = parseLines(lines)
    GOAL = 150
    permutations = calcPermutations(sizes, [], [], GOAL)
    return(f"The number of permutations of containers is {len(permutations)}.")

def part2(lines):
    sizes = parseLines(lines)
    GOAL = 150
    permutations = calcPermutations(sizes, [], [], GOAL)
    smallestSet = 150
    for permutation in permutations:
        if len(permutation) < smallestSet:
            smallestSet = len(permutation)
    setCount = 0
    for permutation in permutations:
        if len(permutation) == smallestSet:
            setCount += 1
    return(f"The minimum set that holds {GOAL} is {smallestSet} cups large. There are {setCount} such sets.")

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