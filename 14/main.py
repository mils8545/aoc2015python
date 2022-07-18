import easygui
import time

AOCDAY = "14"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    reindeer = []
    for line in lines:
        terms = line.split(" ")
        reindeer.append({"name":terms[0], "speed":int(terms[3]), "duration":int(terms[6]),
            "rest":int(terms[-2]), "period":int(terms[-2])+int(terms[6])})
    return reindeer

def part1(lines):
    reindeer = parseLines(lines)
    targetTime = 2503

    for deer in reindeer:
        deer["distance"] = (targetTime // deer["period"]) * deer["speed"] * deer["duration"] + (min(deer["duration"], targetTime % deer["period"]) * deer["speed"])
    fastestReindeer = max(reindeer, key=lambda x: x["distance"])
    fName = fastestReindeer["name"]
    fDistance = fastestReindeer["distance"]
    return(f"The reindeer that wins after {targetTime} seconds is {fName} with a distance of {fDistance}.")

def stepTime(reindeer, time):
    for deer in reindeer:
        if time % deer["period"] < deer["duration"]:
            deer["distance"] += deer["speed"]
    leadDistance = 0
    for deer in reindeer:
        if deer["distance"] > leadDistance:
            leadDistance = deer["distance"]
    for deer in reindeer:
        if deer["distance"] == leadDistance:
            deer["score"] += 1

def part2(lines):
    reindeer = parseLines(lines)
    targetTime = 2503
    for deer in reindeer:
        deer["distance"] = 0
        deer["score"] = 0

    for time in range(targetTime):
        stepTime(reindeer, time)
    
    winner = max(reindeer, key=lambda x: x["score"])
    wName = winner["name"]
    wScore = winner["score"]
    print(reindeer)
    return(f"The reindeer that wins after {targetTime} seconds is {wName} with a score of {wScore}.")

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