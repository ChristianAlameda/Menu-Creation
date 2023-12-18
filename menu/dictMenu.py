from dictionary.dictLinkedlist import DictLinkedList
from menu.menuAbstract import MenuAbstract
from menu.entry import Entry
import csv

class DictMenu(MenuAbstract):
    def __init__(self):
        self.dictList = DictLinkedList()

    def searchMeal(self, meal):
        if meal in self.dictList:
            return self.dictList[meal]

    def searchType(self, mealType):
        tmp = []
        if mealType in self.dictList:
            tmp.append(mealType)

    def printMenu(self):  
        print("[Meals], [Calories], [Ingredients], [Food Types], [Prices]")
        self.dictList.print_LL()

    def addMenu(self, key, value):  
        self.dictList._insert(key, value)

    def removeMenu(self, restaurant, meal):  
        if meal is None:
            return self.notFound()
        else:
            self.dictList.pop(meal)
            
    def editInventory(self, meal, calories, ingredients, mealType, price):
        entry = self.searchMeal(meal)
        if entry is None:
            return None
        entry.setCalories(calories)
        entry.setIngredients(ingredients)
        entry.setType(mealType)
        entry.setPrice(price)

    
    def createInventory(self, restaurant):
        with open(restaurant, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                entry = Entry()
                entry.setMeal(line[0])
                entry.setCalories(line[1])
                entry.setIngredients(line[2])
                entry.setType(line[3])
                entry.setPrice(line[4])
                self.dictList[entry.getMeal()] = entry

    def writeBack(self, restaurant):  
        with open(restaurant, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            for meal in self.dictList:
                mealList = [meal.getMeal(), str(meal.getCalories()), meal.getIngredients(), meal.getType(),
                            str(float(meal.getPrice()))]
                csvwriter.writerow(mealList)

    def giveOptions(self):
        print()
        print("[0] - Exit Program")
        print("[1] - Search")
        print("[2] - Print Menu")
        print("[3] - Add to the Menu")
        print("[4] - Remove from the Menu")
        print("[5] - Edit Menu")

    def notFound(self):
        print("The inputed value was either not in our system or mispelled. Please try again.")
