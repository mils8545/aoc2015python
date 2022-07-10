import easygui
import time

AOCDAY = "05"

def readFile(fileName):
    with open(fileName, "r") as file:
        return file.readlines()

def md5(s):
    import hashlib
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def part1(lines):
    calcedHash = "fffffffffffff"
    num = -1
    while calcedHash [:5] != "00000":
        num += 1
        calcedHash = md5(lines[0] + str(num))
    return(f"The number is {num}.")

def part2(lines):
    calcedHash = "fffffffffffff"
    num = -1
    while calcedHash [:6] != "000000":
        num += 1
        calcedHash = md5(lines[0] + str(num))
    return(f"The number is {num}.")

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