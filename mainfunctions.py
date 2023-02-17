from entry import Entry
from menu import Menu
# This class's main role is to be called into main 
#yahir 5-20
def main_meal():
    s = Entry() # s will be the object we will simply add functions from main to 
  #going to the menu class and setting all of the variables we made
    s.set_meal("Taco")
    s.set_calories("500") 
    s.set_ingredients("Meat, cheese") 
    s.set_type("Mexican")
    s.set_price("140")
  #printing the information that was set 
    print("Meal info: \n" + "Meal Name: "+str(s.get_meal()) + " \nAmmount of Calories: "+str(s.get_calories()) +
          "\nType of Food: " + s.get_type() + "\nPrice of Meal: "+ (str(s.get_price())))

    # Search for user input (menu) and returns 
#def main_inventory():
 #   cInventory = Menu()
 #   cInventory.create_inventory("restaurant.csv")
  