from dictlinkedlist import Dictlinkedlist
from menuabstract import menuAbstract
from entry import Entry
import csv
#step6 part we forgot to do
class DictMenu(menuAbstract):
  #for step 6 
  def __init__(self):
    self.dictlist = Dictlinkedlist() #linkedlistdictionary we made

  def search_meal(self,meal):
    if meal in self.dictlist:
      return self.dictlist[meal]
  
  def search_type(self, type):
    tmplist = []
    if type in self.dictlist:
      tmplist.append(type) 
  
  def print_menu(self):#yahir
    print(
            "[Meals], [Calories], [Ingredients], [Food Types], [Prices]"
        )
    self.dictlist.print_LL()
    
  def add_menu(self, key, value):#yahir
    self.dictlist._insert(key,value)
  
  def remove_menu(self, restaurant, meal):#yahir
     if meal == None:
      return self.not_found()
     else:
      self.dictlist.pop(meal)
  #christian next 2
  def edit_inventory(self, meal,calories,ingredients,type,price):
    entry = self.search_meal(meal)
    if entry == None:
      return None
    entry.set_calories(calories)
    entry.set_ingredients(ingredients)
    entry.set_type(type)
    entry.set_price(price)
    
  #christian
  
  def create_inventory(self, restaurant): 
    with open(restaurant,"r") as csvfile:
      csvreader = csv.reader(csvfile)
      for line in csvreader:
        entry = Entry()
        entry.set_meal(line[0])
        entry.set_calories(line[1])
        entry.set_ingredients(line[2])
        entry.set_type(line[3])
        entry.set_price(line[4])
        self.dictlist[entry.get_meal()] = entry
        
    
  def write_back(self, restaurant): #yahir
    with open(restaurant, "w") as csvfile:
          csvwriter = csv.writer(csvfile)
          for meal in self.__list_meal:
            meal_list = [meal.get_meal(), str(meal.get_calories()), meal.get_ingredients(), meal.get_type(), str(float(meal.get_price()))]
            csvwriter.writerow(meal_list)

  def give_options(self):
        print()
        print("[0] - Exit Program")
        print("[1] - Search")
        print("[2] - Print Menu")
        print("[3] - Add to the Menu")
        print("[4] - Remove from the Menu")
        print("[5] - Edit Menu")

  def not_found(self):
        print("The inputed value was either not in our system or mispelled. Please try again.")


    
          