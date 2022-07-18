from winreg import REG_OPTION_BACKUP_RESTORE
import easygui
import time

AOCDAY = "15"

def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    ingredients = []
    for line in lines:
        terms = line.split(" ")
        ingredients.append({"name":terms[0][0:-1], "stats": [int(terms[2][0:-1]), int(terms[4][0:-1]), int(terms[6][0:-1]), int(terms[8][0:-1]), int(terms[10])]})
    return ingredients

def recipePermuations(numIngredients, RECIPETOTAL, recipes, currentRecipe):
    totalIngredients = 0
    for amount in currentRecipe:
        totalIngredients += amount
    if len(currentRecipe) == numIngredients - 1:
        recipes.append(currentRecipe + [RECIPETOTAL - totalIngredients])
        return recipes
    for i in range(RECIPETOTAL - totalIngredients + 1):
        newRecipe = currentRecipe + [i]
        recipes = recipePermuations(numIngredients, RECIPETOTAL, recipes, newRecipe)
    return recipes

def scoreRecipe(ingredients, recipe):
    scoreTotal = 1
    for i in range(len(ingredients[0]["stats"])-1):
        ingredientTotal = 0
        for j in range(len(recipe)):
            ingredientTotal += recipe[j] * ingredients[j]["stats"][i]
        scoreTotal *= ingredientTotal if ingredientTotal > 0 else 0
    return scoreTotal

def callories(ingredients, recipe):
    calories = 0
    for i in range(len(recipe)):
        calories += ingredients[i]["stats"][-1] * recipe[i]
    return calories

def part1(lines):
    ingredients = parseLines(lines)
    RECIPETOTAL = 100
    recipes = recipePermuations(len(ingredients), RECIPETOTAL, [], [])
    scores = []
    for recipe in recipes:
        scores.append(scoreRecipe(ingredients, recipe))
    return(f"The best cookies has a score of {max(scores)}.")

def part2(lines):
    ingredients = parseLines(lines)
    RECIPETOTAL = 100
    recipes = recipePermuations(len(ingredients), RECIPETOTAL, [], [])
    scores = []
    for recipe in recipes:
        if callories(ingredients, recipe) == 500:
            scores.append(scoreRecipe(ingredients, recipe))

    return(f"The best cookies with 500 callories has a score of {max(scores)}.")

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