from interface import interface, menuAnalysis
# from generateData import generateData
import random 
import os

def generateData(randFileName, noEntries):
    fileName = "temp.csv"
    with open(fileName, "w") as writeFile:
        for i in range(1, noEntries + 1):
            mealName = "pastora" + str(i)
            mealCalories = "210"
            mealIngredients = "meat"
            mealType = "Mexican"
            mealPrice = "12"
            writeFile.write(mealName + "," + mealCalories + "," + mealIngredients + "," + mealType + "," + mealPrice + '\n')
    with open(fileName, 'r') as source:
        data = [(random.random(), line) for line in source]
    data.sort()
    with open(randFileName, 'w') as target:
        for _, line in data:
            target.write(line)
    os.remove(fileName)
    
def mainAnalysis():
    noEntries = int(input('Enter number of entries into the file for testing\nenter here: '))
    fileName = "rand_file_" + str(noEntries) + ".txt"
    generateData(fileName, noEntries)
    menuAnalysis(fileName, noEntries, noEntries)
    os.remove(fileName)
    
if __name__ == "__main__":
    choice = int(input('[0] - testing speed with different data structures\n[1] - for menu Creation\nEnter Here: '))
    if choice == 0:
        mainAnalysis()
    elif choice == 1:
        interface()

