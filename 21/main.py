import easygui
import time

AOCDAY = "21"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

equipmentList = {
    "Dagger": {"Cost": 8, "Damage": 4, "Armor": 0},
    "Shortsword": {"Cost": 10, "Damage": 5, "Armor": 0},
    "Warhammer": {"Cost": 25, "Damage": 6, "Armor": 0},
    "Longsword": {"Cost": 40, "Damage": 7, "Armor": 0},
    "Greataxe": {"Cost": 74, "Damage": 8, "Armor": 0},
    "None": {"Cost": 0, "Damage": 0, "Armor": 0},
    "Leather": {"Cost": 13, "Damage": 0, "Armor": 1},
    "Chainmail": {"Cost": 31, "Damage": 0, "Armor": 2},
    "Splintmail": {"Cost": 53, "Damage": 0, "Armor": 3},
    "Bandedmail": {"Cost": 75, "Damage": 0, "Armor": 4},
    "Platemail": {"Cost": 102, "Damage": 0, "Armor": 5},
    "None2": {"Cost": 0, "Damage": 0, "Armor": 0},
    "Damage +1": {"Cost": 25, "Damage": 1, "Armor": 0},
    "Damage +2": {"Cost": 50, "Damage": 2, "Armor": 0},
    "Damage +3": {"Cost": 100, "Damage": 3, "Armor": 0},
    "Defense + 1": {"Cost": 20, "Damage": 0, "Armor": 1},
    "Defense + 2": {"Cost": 40, "Damage": 0, "Armor": 2},
    "Defense + 3": {"Cost": 80, "Damage": 0, "Armor": 3}
}

weapons = ["Dagger", "Shortsword", "Warhammer", "Longsword", "Greataxe"]
armors = ["None", "Leather", "Chainmail", "Splintmail", "Bandedmail", "Platemail"]
rings = ["None", "None2", "Damage +1", "Damage +2", "Damage +3", "Defense + 1", "Defense + 2", "Defense + 3"]

def runBattle(player, boss):
    while player["HP"] > 0 and boss["HP"] > 0:
        boss["HP"] -= max(1, player["Damage"] - boss["Armor"])
        if boss["HP"] > 0:
            player["HP"] -= max(1, boss["Damage"] - player["Armor"])
    return player["HP"] > 0

def generateEquipmentCombinations():
    combinations = []
    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring1 != ring2:
                        combinations.append({"Weapon": weapon, "Armor": armor, "Ring1": ring1, "Ring2": ring2})
    return combinations

def loadOutStats(equipment):
    stats = {"cost": 0, "damage": 0, "armor": 0}
    for key in equipment:
        stats["cost"] += equipmentList[equipment[key]]["Cost"]
        stats["damage"] += equipmentList[equipment[key]]["Damage"]
        stats["armor"] += equipmentList[equipment[key]]["Armor"]
    return stats

def part1(lines):
    boss = {"HP": int(lines[0].split(":")[1].strip()), "Damage": int(lines[1].split(":")[1].strip()), "Armor": int(lines[2].split(":")[1].strip())}
    player = {"HP": 100, "Damage": 0, "Armor": 0}
    combinations = generateEquipmentCombinations()
    loadOuts = []
    for combination in combinations:
        loadOut = {"Weapon": combination["Weapon"], "Armor": combination["Armor"], "Ring1": combination["Ring1"], "Ring2": combination["Ring2"]}
        stats = loadOutStats(loadOut)
        loadOut["cost"] = stats["cost"]
        loadOut["damage"] = stats["damage"]
        loadOut["armor"] = stats["armor"]
        loadOuts.append(loadOut)
    loadOuts.sort(key=lambda x: x["cost"])

    won = False
    while not won:
        for loadOut in loadOuts:
            player = {"HP": 100, "Damage": 0, "Armor": 0}
            boss = {"HP": int(lines[0].split(":")[1].strip()), "Damage": int(lines[1].split(":")[1].strip()), "Armor": int(lines[2].split(":")[1].strip())}
            player["Damage"] = loadOut["damage"]
            player["Armor"] = loadOut["armor"]
            won = runBattle(player, boss)
            if won:
                return f"The least expensive loadout to still beat the boss has a cost of {loadOut['cost']}."

def part2(lines):
    boss = {"HP": int(lines[0].split(":")[1].strip()), "Damage": int(lines[1].split(":")[1].strip()), "Armor": int(lines[2].split(":")[1].strip())}
    player = {"HP": 100, "Damage": 0, "Armor": 0}
    combinations = generateEquipmentCombinations()
    loadOuts = []
    for combination in combinations:
        loadOut = {"Weapon": combination["Weapon"], "Armor": combination["Armor"], "Ring1": combination["Ring1"], "Ring2": combination["Ring2"]}
        stats = loadOutStats(loadOut)
        loadOut["cost"] = stats["cost"]
        loadOut["damage"] = stats["damage"]
        loadOut["armor"] = stats["armor"]
        loadOuts.append(loadOut)
    loadOuts.sort(key=lambda x: -x["cost"])

    won = True
    while won:
        for loadOut in loadOuts:
            player = {"HP": 100, "Damage": 0, "Armor": 0}
            boss = {"HP": int(lines[0].split(":")[1].strip()), "Damage": int(lines[1].split(":")[1].strip()), "Armor": int(lines[2].split(":")[1].strip())}
            player["Damage"] = loadOut["damage"]
            player["Armor"] = loadOut["armor"]
            won = runBattle(player, boss)
            if not won:
                return f"The most expensive loadout to still lose to the boss has a cost of {loadOut['cost']}"

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