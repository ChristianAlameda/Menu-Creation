import csv
from entry import Entry
from menuabstract import * #inheriting abstractmethods

#This class will contain all of our functions that have to do with the inventory
class Menu(menuAbstract):
    #Yumong 5-27
    #Making a list for the menu
    def __init__(self):
        self.__list_meal = []
      
    def search_meal(self,meal):  #Returns other values in accordance with meal name
        #__list_meal is dependent on create inventory, since we are only putting in one line with the
        #
        for i in self.__list_meal:
            if i.get_meal() == meal:
                return i
        return None

    # This is a search function that returns a list of
    # entries with the same type
    # take the type, compare the type of every entry to the given type
    def search_type(self, type):
        a = []
        for i in self.__list_meal:
            if i.get_type() == type:
               a.append(i)
        return a

    #yahir 29 - 45
    def print_menu(self):  #prints the menu in its entirety
        print(
            "       [Meals], [Calories], [Ingredients], [Food Types], [Prices]"
        )
        for i in range(len(self.__list_meal)):
            print("Meal " + str(i + 1) + ": " + str(self.__list_meal[i]))

    def add_menu(self, restaurant, new_item):  #will add onto the menu, may have to add onto list and append that into the file
        self.__list_meal.append(new_item)  #appends the user input to the end of the list

    def remove_menu(self, restaurant, meal):  #will delete all items that make up the meal inputted by the user
      search = self.search_meal(meal)  # running meal into search_meal and putting that variable into another variable
      if search == None:
          return self.not_found()
      else:
          self.__list_meal.remove(search)
          
    def write_back(self, restaurant): # writing back list to file
      with open(restaurant, "w") as csvfile:
          csvwriter = csv.writer(csvfile)
          for meal in self.__list_meal:
            meal_list = [meal.get_meal(), str(meal.get_calories()), meal.get_ingredients(), meal.get_type(), str(float(meal.get_price()))]
            csvwriter.writerow(meal_list)
            
    # Yumong Lee 47-54
    # Allows the user to choose from a row and edits that whole row

    def edit_inventory(self, meal, calories, ingredients, type, price):
      shop = self.search_meal(meal)
      if shop ==None:
        return None
      shop.set_calories(calories)
      shop.set_ingredients(ingredients)
      shop.set_type(type)
      shop.set_price(price)
      return shop


    '''
    
    
    
    
    
    
    def edit_inventory(self, restaurant):
      # Read Before testing it out
      # Code works, but needs some adjustment
      # It will print out the first meal only and only the first meal, but is editing one row before the user's input
      # It will skip the row number that the user inputed and go to the next one Ex.(1) = row(2). row 6 = row 7 instead of row 6, row 16 = row 17 instead of row 16, etc 
      fileList = [] 
      with open(restaurant, "r") as file:
        editFile = csv.reader(file)
        for row in editFile:
          fileList.append(row) #Going to append the csv file
        editRow = int(input("\nWhich row would you like to change? 1-" + str(len(fileList)) + ": "))
        print("Please enter the new details for each of the folowing:")
        for i in range (len(fileList[0])): #Getting the length (rows) of csv file
          newInfo = input("Enter new info for: " + str(fileList[0][i]) + ": \n") # User input new information into list
          fileList[editRow][i] = newInfo
          with open(restaurant, 'w+') as file: #Write back to the csv file with user's new information
            editFile = csv.writer(file) 
            for i in range (len(fileList)):
              editFile.writerow(fileList[i])
    '''
          # It's gonna get the user's # input and then match it with the row  within the csv file
          # After that it's gonna allow the user to edit that certain line with whatever they want to change it to.
          # But I am not sure if I implemented it correctly.
     # Chrisitan 93-118
              #make a function that will take in restaurant and go through the lines
    def create_inventory(self, restaurant): 
      #read in the file
        with open(restaurant, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
              #make an object that will be able to distinguish between the items in the row
                entry = Entry(
              )  # Sets the Meal, Calories, Ingridients, Type, and Price
                entry.set_meal(line[0])
                entry.set_calories(int(line[1]))
                entry.set_ingredients(line[2])
                entry.set_type(line[3])
                entry.set_price(int(float(line[4])))
#we want to entry to be our linked list now instead of our list
                self.__list_meal.append(entry)  # Appends the menu

    # I believe I need to make a new function which reads restaurant but will simply take all the lines
    # I disliked repeating myself over and over again
    def give_options(self):
        print()
        print("[0] - Exit Program")
        print("[1] - Search")
        print("[2] - Print Menu")
        print("[3] - Add to the Menu")
        print("[4] - Remove from the Menu")
        print("[5] - Edit Menu")
      
      
  # make a function that prints for when user typed something in wrong or its not in our system
    def not_found(self):
        print("The inputed value was either not in our system or mispelled. Please try again.")
