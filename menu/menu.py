import csv
from menu.entry import Entry
from menu.menuAbstract import MenuAbstract  # inheriting abstractmethods

class Menu(MenuAbstract):
    def __init__(self):
        self.__listMeal = []

    def searchMeal(self, meal):  # Returns other values in accordance with meal name
        for i in self.__listMeal:
            if i.getMeal() == meal:
                return i
        return None

    def searchType(self, type):
        result = []
        for i in self.__listMeal:
            if i.getType() == type:
                result.append(i)
        return result

    def printMenu(self):
        print("[Meals], [Calories], [Ingredients], [Food Types], [Prices]")
        for i in range(len(self.__listMeal)):
            print("Meal " + str(i + 1) + ": " + str(self.__listMeal[i]))

    def addMenu(self, restaurant, newItem):
        self.__listMeal.append(newItem)

    def removeMenu(self, restaurant, meal):
        search = self.searchMeal(meal)
        if search is None:
            return self.notFound()
        else:
            self.__listMeal.remove(search)

    def writeBack(self, restaurant):
        with open(restaurant, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            for meal in self.__listMeal:
                mealList = [meal.getMeal(), str(meal.getCalories()), meal.getIngredients(), meal.getType(),
                            str(float(meal.getPrice()))]
                csvwriter.writerow(mealList)

    def editInventory(self, meal, calories, ingredients, mealType, price):
        shop = self.searchMeal(meal)
        if shop is None:
            return None
        shop.setCalories(calories)
        shop.setIngredients(ingredients)
        shop.setType(mealType)
        shop.setPrice(price)
        return shop

    def createInventory(self, restaurant):
        with open(restaurant, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                entry = Entry()
                entry.setMeal(line[0])
                entry.setCalories(int(line[1]))
                entry.setIngredients(line[2])
                entry.setType(line[3])
                entry.setPrice(int(float(line[4])))
                self.__listMeal.append(entry)

    def giveOptions(self):
        print("\n[0] - Exit Program")
        print("[1] - Search")
        print("[2] - Print Menu")
        print("[3] - Add to the Menu")
        print("[4] - Remove from the Menu")
        print("[5] - Edit Menu")

    def notFound(self):
        print("The inputed value was either not in our system or mispelled. Please try again.")
