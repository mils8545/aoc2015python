import easygui
import time

AOCDAY = "22"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

spellBook = {"Magic Missile": 53, "Drain": 73, "Shield": 113, "Poison": 173, "Recharge": 229}

def battleStep(gameState):
    gameState["castList"] = gameState["castList"] + [gameState["nextSpell"]] 
    gameState["playerMana"] -= spellBook[gameState["nextSpell"]]

    if gameState["playerHP"] <= 0:
        returnState = gameState.copy()
        returnState["status"] = "Lost"
        return returnState

    if gameState["poisonTimer"] > 0:
        gameState["bossHP"] -= 3
        gameState["poisonTimer"] -= 1
    if gameState["shieldTimer"] > 0:
        gameState["shieldTimer"] -= 1
    if gameState["rechargeTimer"] > 0:
        gameState["playerMana"] += 101
        gameState["rechargeTimer"] -= 1
    if gameState["playerMana"] < 0:
        returnState = gameState.copy()
        returnState["status"] = "Lost"
        return returnState
            
    if gameState["nextSpell"] == "Magic Missile":
        gameState["bossHP"] -= 4
    elif gameState["nextSpell"] == "Drain":
        gameState["bossHP"] -= 2
        gameState["playerHP"] += 2
    elif gameState["nextSpell"] == "Shield":
        if gameState["shieldTimer"] == 0:
            gameState["shieldTimer"] = 6
        else:
            returnState = gameState.copy()
            returnState["status"] = "Lost"
            return returnState
    elif gameState["nextSpell"] == "Poison":
        if gameState["poisonTimer"] == 0:
            gameState["poisonTimer"] = 6
        else:
            returnState = gameState.copy()
            returnState["status"] = "Lost"
            return returnState
    elif gameState["nextSpell"] == "Recharge":
        if gameState["rechargeTimer"] == 0:
            gameState["rechargeTimer"] = 5
        else:
            returnState = gameState.copy()
            returnState["status"] = "Lost"
            return returnState

    if gameState["poisonTimer"] > 0:
        gameState["bossHP"] -= 3
        gameState["poisonTimer"] -= 1
    if gameState["shieldTimer"] > 0:
        gameState["shieldTimer"] -= 1
    if gameState["rechargeTimer"] > 0:
        gameState["playerMana"] += 101
        gameState["rechargeTimer"] -= 1

    if gameState["bossHP"] <= 0:
        returnState = gameState.copy()
        returnState["status"] = "Win"
        return returnState

    gameState["playerHP"] -= max(1, gameState["bossDamage"] - (7 if gameState["shieldTimer"] > 0 else 0))
    if gameState["playerHP"] <= 0:
        returnState = gameState.copy()
        returnState["status"] = "Lost"
        return returnState

    gameState["status"] = "Going"
    return gameState

def part1(lines):    
    boss = {"HP": int(lines[0].split(":")[1].strip()), "Damage": int(lines[1].split(":")[1].strip())}
    player = {"HP": 50, "Mana": 500}
    gameStateQueue = []
    for spell in spellBook:
        gameStateQueue.append({"playerHP": player["HP"], "playerMana": player["Mana"], 
        "bossHP": boss["HP"], "bossDamage": boss["Damage"],
        "shieldTimer": 0, "poisonTimer": 0, "rechargeTimer": 0,
        "castList": [], "nextSpell": spell, 
        "totalCost": spellBook[spell], "status": "Going"})
    while len(gameStateQueue) > 0:
        gameState = gameStateQueue.pop(0)
        result = battleStep(gameState)
        if result["status"] == "Win":
            return result
        elif result["status"] == "Going":
            for spell in spellBook:
                newState = result.copy()
                newState["nextSpell"] = spell
                newState["totalCost"] = result["totalCost"] + spellBook[spell]
                gameStateQueue.append(newState)
        gameStateQueue.sort(key=lambda x: x["totalCost"])

def part2(lines):
    boss = {"HP": int(lines[0].split(":")[1].strip()), "Damage": int(lines[1].split(":")[1].strip())}
    player = {"HP": 50, "Mana": 500}
    gameStateQueue = []
    for spell in spellBook:
        gameStateQueue.append({"playerHP": player["HP"], "playerMana": player["Mana"], 
        "bossHP": boss["HP"], "bossDamage": boss["Damage"],
        "shieldTimer": 0, "poisonTimer": 0, "rechargeTimer": 0,
        "castList": [], "nextSpell": spell, 
        "totalCost": spellBook[spell], "status": "Going"})
    while len(gameStateQueue) > 0:
        gameState = gameStateQueue.pop(0)
        gameState["playerHP"] -= 1
        result = battleStep(gameState)
        if result["status"] == "Win":
            return result
        elif result["status"] == "Going":
            for spell in spellBook:
                newState = result.copy()
                newState["nextSpell"] = spell
                newState["totalCost"] = result["totalCost"] + spellBook[spell]
                gameStateQueue.append(newState)
        gameStateQueue.sort(key=lambda x: x["totalCost"])

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