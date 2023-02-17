from dicthashtable import dicthashtable 
from menuabstract import menuAbstract
from entry import Entry
import csv

class Menuhashtable(menuAbstract):#got rid of dicthashtable
  def __init__(self): #creates instance of implemented data structure
    self.hashtable = dicthashtable()
    
  def search_meal(self, meal):
    return self.hashtable.search(meal)
  
  def search_type(self, type):
    #not doing this one
    pass
    

  def print_menu(self): #yahir
    self.hashtable.print_LL()

  def add_menu(self, key, value): #yahir
    self.hashtable.add(key, value)

  def remove_menu(self, restaurant, meal): #yahir
    if meal == None:
      return self.not_found()
    else:
      self.hashtable.pop(meal)

  def edit_inventory(self, meal, calories, ingredients, type, price): #christian
    entry = self.search_meal(meal)
    if entry == None:
      return None
      
    entry.set_calories(calories)
    entry.set_calories(calories)
    entry.set_ingredients(ingredients)
    entry.set_type(type)
    entry.set_price(price)
  '''
  want to get all our data organized into keys 
  and values, so we set according to the line
  and use get_meal for our key
  '''
  def create_inventory(self,restaurant):
    with open("restaurant.csv","r") as file:
      csvreader = csv.reader(file)
      for line in csvreader:
        entry = Entry()
        entry.set_meal(line[0])
        entry.set_calories(line[1])
        entry.set_ingredients(line[2])
        entry.set_price(line[3])
        entry.set_type(line[4])
        self.hashtable[entry.get_meal()] = entry

  def write_back(self, restaurant): #christian 
    with open(restaurant, "w") as csvfile:
      csvwriter = csv.writer(csvfile)
      meal = self.hashtable
      for value in meal:
        #check if value is none
        #because with hash we have a lot of empty indexes
        if meal[value] is None:# before adding this will not be true
          return None
        for j in value:
          if value[j] is None:# before adding this will not be true
            return None
          else:
            print("hello")
            #csvwriter.writer(j) #doesnt work.
          '''
          j += j[1]# line is not correct(teacher), 
          print(j)
          
          '''
          
      #use nested for loop that concatenates value to a variable and then return variable to write back to csv,Q's for prof, what are we looping through? 
        

  def give_options(self):
    print()
    print("[0] - Exit Program")
    print("[1] - Search")
    print("[2] - Print Menu")
    print("[3] - Add to the Menu")
    print("[4] - Remove from the Menu")
    print("[5] - Edit Menu")

  def not_found(self):
    print("The input value was either not there, or messed up, or typed wrong, please try again")





















      

  
