from dictionary.dictHashtable import DictHashtable
from menu.menuAbstract import MenuAbstract
from menu.entry import Entry
import csv

class MenuHashtable(MenuAbstract):
    def __init__(self):
        self.hashtable = DictHashtable()

    def searchMeal(self, meal):
        return self.hashtable.search(meal)

    def searchType(self, mealType):
        # not doing this one
        pass

    def printMenu(self):  
        self.hashtable.printLL()

    def addMenu(self, key, value):  
        self.hashtable.add(key, value)

    def removeMenu(self, restaurant, meal):  
        if meal is None:
            return self.notFound()
        else:
            self.hashtable.pop(meal)

    def editInventory(self, meal, calories, ingredients, mealType, price):  
        entry = self.searchMeal(meal)
        if entry is None:
            return None

        entry.setCalories(calories)
        entry.setIngredients(ingredients)
        entry.setType(mealType)
        entry.setPrice(price)

    def createInventory(self, restaurant):
        with open("restaurant.csv", "r") as file:
            csvreader = csv.reader(file)
            for line in csvreader:
                entry = Entry()
                entry.setMeal(line[0])
                entry.setCalories(line[1])
                entry.setIngredients(line[2])
                entry.setPrice(line[3])
                entry.setType(line[4])
                self.hashtable[entry.getMeal()] = entry

    def writeBack(self, restaurant):  
        with open(restaurant, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            meal = self.hashtable
            for value in meal:
                # check if value is none
                # because with hash we have a lot of empty indexes
                if meal[value] is None:  # before adding this will not be true
                    return None
                for j in value:
                    if value[j] is None:  # before adding this will not be true
                        return None
                    else:
                        print("hello")
                        # csvwriter.writer(j) #doesn't work.
    
    def giveOptions(self):
        print("\n[0] - Exit Program")
        print("[1] - Search")
        print("[2] - Print Menu")
        print("[3] - Add to the Menu")
        print("[4] - Remove from the Menu")
        print("[5] - Edit Menu")

    def notFound(self):
        print("The inputed value was either not in our system or mispelled. Please try again.")