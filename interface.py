from menu.menu import Menu
from menu.dictMenu import DictMenu
from dictionary.dictHashtable import *
from menu.menuHashtable import MenuHashtable
import time
import random

def interface():
    dataStructure = input('[0] - list\n[1] - hash\n[2] - Linked Lists\nEnter Here: ')
    if dataStructure == '0':
        cInventory = Menu()
    elif dataStructure == '1':
        cInventory = MenuHashtable()
    elif dataStructure == '2':
        cInventory = DictMenu()
    cInventory.createInventory("restaurant.csv")
    print("**********************************************************")
    print("**********************************************************")
    print("*****   Welcome to Menu Creation and Customization   *****")
    print("**********************************************************")
    print("**********************************************************")
    cInventory.giveOptions()
    a = input("Enter Number Here: ")
    if a == "0":
        exit()
    
    while a != "0":
        if a == "1":
            print("\n[1] To search for the meal name\n[2] To search for the food type")
            a1 = input("Enter Number Here: ")
            if a1 == "1":
                meal = str.lower(input("Enter meal name: "))
                mealInfo = cInventory.searchMeal(meal)     
                if mealInfo is None:        
                    cInventory.notFound()
                else:
                    print(mealInfo.__str__())
                    cInventory.giveOptions()
                    a = input("\nEnter Number: ")
                    if a == "0":
                        exit()
            elif a1 == "2":
                print("Enter the Type of Food you will like to search for: ")
                mealType = input().capitalize()
                mealInfo = cInventory.searchType(mealType)
                if mealInfo is None:
                    cInventory.notFound()
                else:
                    output = 'Type: ' + mealType + '\n'
                    for info in mealInfo:
                        output += str('\t' + info.display() + '\n')
                    print(output)
                cInventory.giveOptions()
                a = input("\nEnter Number: ")
                if a == "0":
                    exit()
        elif a == "2":
            cInventory.printMenu()
            cInventory.giveOptions()
            a = input("\nEnter Number: ")
            if a == "0":
                exit()
        elif a == "3":
            print("Please insert the meal name, calories, ingredients, type, and price.")
            print("Please put quotation marks in between to separate the ingredients.")
            newItem = input()
            cInventory.addMenu("restaurant.csv", newItem)
            cInventory.giveOptions()
            a = input("\nEnter Number: ")
            if a == "0":
                exit()
        elif a == "4":
            meal = input("Enter the meal you would like to remove: ")
            cInventory.removeMenu("restaurant.csv", meal)
            cInventory.printMenu()
            cInventory.giveOptions()
            a = input("\nEnter Number: ")
            if a == "0":
                exit()
        elif a == "5":
            cInventory.printMenu()
            meal = input("Enter a meal: ")
            calories = input("Enter amount of calories: ")
            ingredients = input("Enter ingredients: ")
            mealType = input("Enter a type for the meal: ")
            price = input("Enter a price for the meal: ")
            cInventory.editInventory(meal, calories, ingredients, mealType, price)
            cInventory.giveOptions()
            a = input("\n Enter Number: ")
            if a == "0":
                exit()

@staticmethod
def menuAnalysis(randFileName, noQueries, noEntries):
    cMenu = Menu()
    cMenu.createInventory(randFileName)
    
    cMenuDict = DictMenu()
    cMenuDict.createInventory(randFileName)
    
    cMenuHashtable = MenuHashtable()
    cMenuHashtable.createInventory(randFileName)
    
    randomMealList = []
    for i in range(0, noQueries):
        n = random.randint(1, noEntries)
        randomMealList.append(n)

    startTime = time.time()
    results1 = []
    for randMeal in randomMealList:
        result = cMenu.searchMeal(randMeal)
        results1.append(result)
    endTime = time.time()
    print("No of entries: " + str(noEntries))
    print("searching " + str(noQueries) + " queries using the List based implementation: --- %s seconds ---"
            % (endTime - startTime))

    startTime2 = time.time()
    results2 = []
    for randMeal in randomMealList:
        result = cMenuDict.searchMeal(randMeal)
        results2.append(result)
    endTime2 = time.time()
    print("searching " + str(noQueries) + " queries using the Linked List based implementation: --- %s seconds ---"
            % (endTime2 - startTime2))
    
    startTime3 = time.time()
    results3 = []
    for randMeal in randomMealList:
        result = cMenuHashtable.searchMeal(randMeal)
        results3.append(result)
    endTime3 = time.time()
    print("searching " + str(noQueries) + " queries using the Hash Table based implementation: --- %s seconds ---"
            % (endTime3 - startTime3))