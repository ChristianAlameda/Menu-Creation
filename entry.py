class Entry: #this class is going to set and get the values that correlate with the function

    def __init__(self):  #constructor
        self.__price = 0
        self.__ingredients = ""
        self.__type = ""
        self.__calories = 0
        self.__meal = ""

    # gets the meal and sets the meal
    # meal is going to be the meal name of each meal
    #we are asking the user for a name and then getting that name and setting it
    def get_meal(self):
        return self.__meal

    def set_meal(self, meal): #yahir line 18 - 26
        self.__meal = meal

        # Will get the price and set the price

    # price is the number of dollars we are asking for the meal
    #we do the same thing as we get price from a setter and if it it is between 0 and 10000 which we thought would be reasonable
    #it will give the price if asked for for
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

       


    #ingredients are the things that get put into the meal
    #We will ask the user to input their ingredients
    #and then we will use those to bring it back to them
    def get_ingredients(self):  #will return completed list of ingredients
        return self.__ingredients

    def set_ingredients(self, ingredients):  #setsup the ingredients
        self.__ingredients = ingredients
#type is going to be the culture that originally made the meal
      #mexican, american, indian, and chinese
      #we do the same thing here as we take in the type the user puts
      #and we return it back so it can be worked with
    # Return the type of dish
    def get_type(self):
        return self.__type

    # sets type of dish
    def set_type(self, type):
        self.__type = type
#Calories are the number given to a meal that represent the healthiness or caloric intake of the meals
      #getting calories from user and saying they must be within reason (0-3000) then setting it for it to be used in mainfunctions.py
    # got the calories and set them while asserting the number it be between

    def get_calories(self):
        return self.__calories

    def set_calories(self, calories):
        self.__calories = calories

    def __str__(self):
      line = "Meal: " + self.__meal + " Calories: " + str(self.__calories) + " Ingredients: " + self.__ingredients + " Type: " + self.__type + " Price: " + str(self.__price)
      return line
