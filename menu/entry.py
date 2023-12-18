class Entry:
    def __init__(self):  # constructor
        self.__price = 0
        self.__ingredients = ""
        self.__type = ""
        self.__calories = 0
        self.__meal = ""

    def getMeal(self):
        return self.__meal

    def setMeal(self, meal):  
        self.__meal = meal

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def getIngredients(self):  # will return completed list of ingredients
        return self.__ingredients

    def setIngredients(self, ingredients):  # sets up the ingredients
        self.__ingredients = ingredients

    def getType(self):
        return self.__type

    def setType(self, type):
        self.__type = type

    def getCalories(self):
        return self.__calories

    def setCalories(self, calories):
        self.__calories = calories

    def __str__(self):  # Allows the contents of the list to be printed
        line = self.__meal + " " + str(self.__calories) + " " + self.__ingredients + " " + self.__type + " " + str(
            self.__price)
        return line

    def display(self):  # Allows the search_type function to work as intended
        line = "Meal: " + self.__meal + " | " + "Calories: " + str(
            self.__calories) + " | " + "Ingredients: " + self.__ingredients + " | " + "Food Type: " + self.__type + " | " + "Price: " + str(
            self.__price)
        return line
