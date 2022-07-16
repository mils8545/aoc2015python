import easygui
import time

AOCDAY = "07"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    instructions = []
    for line in lines:
        terms = line.split(" ")
        if line[0:3] == "NOT":
            instructions.append({"type": terms[0], "a": terms[1], "target": terms[3]})
        elif terms[1] == "->":
            instructions.append({"type": terms[1], "a": terms[0], "target": terms[2]})
        else:
            instructions.append({"type": terms[1], "a": terms[0], "b": terms[2], "target": terms[4]})
    return instructions

def part1(lines):
    wires = {}
    instructions = parseLines(lines)
    for instruction in instructions:
        try:
            wires[instruction["a"]] = int(instruction["a"])
        except:
            pass
        try:
            wires[instruction["b"]] = int(instruction["b"])
        except:
            pass

    while "a" not in wires:
        for instruction in instructions:
            if instruction["type"] == "->" and instruction["a"] in wires:
                wires[instruction["target"]] = wires[instruction["a"]]
            elif instruction["type"] == "NOT" and instruction["a"] in wires:
                wires[instruction["target"]] = ~wires[instruction["a"]]
            elif instruction["a"] in wires and instruction["b"] in wires:
                if instruction["type"] == "AND":
                    wires[instruction["target"]] = wires[instruction["a"]] & wires[instruction["b"]]
                elif instruction["type"] == "OR":
                    wires[instruction["target"]] = wires[instruction["a"]] | wires[instruction["b"]]
                elif instruction["type"] == "LSHIFT":
                    wires[instruction["target"]] = wires[instruction["a"]] << wires[instruction["b"]]
                elif instruction["type"] == "RSHIFT":
                    wires[instruction["target"]] = wires[instruction["a"]] >> wires[instruction["b"]]
    return(f"Wire a has a signal of {wires['a']}.")

def part2(lines):
    wires = {}
    instructions = parseLines(lines)
    for instruction in instructions:
        try:
            wires[instruction["a"]] = int(instruction["a"])
        except:
            pass
        try:
            wires[instruction["b"]] = int(instruction["b"])
        except:
            pass

    while "a" not in wires:
        for instruction in instructions:
            if instruction["target"] not in wires:
                if instruction["type"] == "->" and instruction["a"] in wires:
                    wires[instruction["target"]] = wires[instruction["a"]]
                elif instruction["type"] == "NOT" and instruction["a"] in wires:
                    wires[instruction["target"]] = ~wires[instruction["a"]]
                elif instruction["a"] in wires and instruction["b"] in wires:
                    if instruction["type"] == "AND":
                        wires[instruction["target"]] = wires[instruction["a"]] & wires[instruction["b"]]
                    elif instruction["type"] == "OR":
                        wires[instruction["target"]] = wires[instruction["a"]] | wires[instruction["b"]]
                    elif instruction["type"] == "LSHIFT":
                        wires[instruction["target"]] = wires[instruction["a"]] << wires[instruction["b"]]
                    elif instruction["type"] == "RSHIFT":
                        wires[instruction["target"]] = wires[instruction["a"]] >> wires[instruction["b"]]

    wires = {"b": wires["a"]}
    for instruction in instructions:
        try:
            wires[instruction["a"]] = int(instruction["a"])
        except:
            pass
        try:
            wires[instruction["b"]] = int(instruction["b"])
        except:
            pass
    while "a" not in wires:
        for instruction in instructions:
            if instruction["target"] not in wires:
                if instruction["type"] == "->" and instruction["a"] in wires:
                    wires[instruction["target"]] = wires[instruction["a"]]
                elif instruction["type"] == "NOT" and instruction["a"] in wires:
                    wires[instruction["target"]] = ~wires[instruction["a"]]
                elif instruction["a"] in wires and instruction["b"] in wires:
                    if instruction["type"] == "AND":
                        wires[instruction["target"]] = wires[instruction["a"]] & wires[instruction["b"]]
                    elif instruction["type"] == "OR":
                        wires[instruction["target"]] = wires[instruction["a"]] | wires[instruction["b"]]
                    elif instruction["type"] == "LSHIFT":
                        wires[instruction["target"]] = wires[instruction["a"]] << wires[instruction["b"]]
                    elif instruction["type"] == "RSHIFT":
                        wires[instruction["target"]] = wires[instruction["a"]] >> wires[instruction["b"]]
    return(f"Wire a has a signal of {wires['a']}.")


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