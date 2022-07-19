import easygui
import time

AOCDAY = "23"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    instructions = []
    for line in lines:
        instruction = {"instruction": line.split(" ")[0]}
        if line.split(" ")[1][0] == "a" or line.split(" ")[1][0] == "b":
            instruction["register"] = line.split(" ")[1][0]
        if instruction["instruction"] == "jmp":
            instruction["value"] = int(line.split(" ")[1])
        if instruction["instruction"][0:2] == "ji":
            instruction["value"] = int(line.split(" ")[2])
        instructions.append(instruction)
    return(instructions)

def part1(lines):
    instructions = parseLines(lines)
    progCounter = 0
    registers = {"a": 0, "b": 0}
    while progCounter < len(instructions):
        instruction = instructions[progCounter]
        if instruction["instruction"] == "hlf":
            registers[instruction["register"]] = registers[instruction["register"]] // 2
            progCounter += 1
        elif instruction["instruction"] == "tpl":
            registers[instruction["register"]] = registers[instruction["register"]] * 3
            progCounter += 1
        elif instruction["instruction"] == "inc":
            registers[instruction["register"]] += 1
            progCounter += 1
        elif instruction["instruction"] == "jmp":
            progCounter += instruction["value"]
        elif instruction["instruction"] == "jie":
            if registers[instruction["register"]] % 2 == 0:
                progCounter += instruction["value"]
            else:
                progCounter += 1
        elif instruction["instruction"] == "jio":
            if registers[instruction["register"]] == 1:
                progCounter += instruction["value"]
            else:
                progCounter += 1
    return(f"The program finishes and register b is {registers['b']}")

def part2(lines):
    instructions = parseLines(lines)
    progCounter = 0
    registers = {"a": 1, "b": 0}
    while progCounter < len(instructions):
        instruction = instructions[progCounter]
        if instruction["instruction"] == "hlf":
            registers[instruction["register"]] = registers[instruction["register"]] // 2
            progCounter += 1
        elif instruction["instruction"] == "tpl":
            registers[instruction["register"]] = registers[instruction["register"]] * 3
            progCounter += 1
        elif instruction["instruction"] == "inc":
            registers[instruction["register"]] += 1
            progCounter += 1
        elif instruction["instruction"] == "jmp":
            progCounter += instruction["value"]
        elif instruction["instruction"] == "jie":
            if registers[instruction["register"]] % 2 == 0:
                progCounter += instruction["value"]
            else:
                progCounter += 1
        elif instruction["instruction"] == "jio":
            if registers[instruction["register"]] == 1:
                progCounter += instruction["value"]
            else:
                progCounter += 1
    return(f"The program finishes and register b is {registers['b']}")

def main ():
    fileName = easygui.fileopenbox(default=f"./"+AOCDAY+"/"+"*.txt")
    lines = readFile(fileName)
    p1StartTime = time.perf_counter()
    p1Result = part1(lines)
    p1EndTime = time.perf_counter()
    print("Advent of Code 2015 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    p2StartTime = time.perf_counter()
    p2Result = part2(lines)
    p2EndTime = time.perf_counter()
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()