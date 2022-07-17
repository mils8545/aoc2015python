import easygui
import time

AOCDAY = "11"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def incrementPassword(password):
    done = False
    passwordArray = list(password)
    target = len(password)-1
    while not done:
        if passwordArray[target] == "z":
            passwordArray[target] = "a"
            target -= 1
        else:
            passwordArray[target] = chr(ord(passwordArray[target])+1)
            done = True
    return "".join(passwordArray)

def validatePassword(password):
    sequential = False
    for i in range(len(password)-2):
        if ord(password[i]) == ord(password[i+1])-1 and ord(password[i+1]) == ord(password[i+2])-1:
            sequential = True
    noIOL = not("i" in password or "o" in password or "l" in password)
    pairs = []
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            pairs.append(password[i])
    twoPairs = len(pairs) > 1 and pairs[0] != pairs[1] 
    return sequential and noIOL and twoPairs

def part1(lines):
    curString = lines[0]
    while not validatePassword(curString):
        curString = incrementPassword(curString)
    return(f"The new Password is {curString} in length.")

def part2(lines):
    curString = lines[0]
    while not validatePassword(curString):
        curString = incrementPassword(curString)
    curString = incrementPassword(curString)
    while not validatePassword(curString):
        curString = incrementPassword(curString)
    return(f"The new Password is {curString} in length.")

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