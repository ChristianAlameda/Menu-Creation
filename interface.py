from entry import Entry
from menu import Menu
from dictmenu import DictMenu
from dicthashtable import *
from menuhashtable import Menuhashtable
import time
import random


#class Interface: #Holds the function for the interface
    # Yumong Lee 1-15
def interface():
    dataStructure = input('[0] - list\n[1] - hash\n[3] - Linked Lists\nEnter Here: ')
    if dataStructure == '0':
      cInventory = Menu()
    elif dataStructure == '1':
      cInventory = Menuhashtable()
    elif dataStructure == '2':
      cInventory = DictMenu()
    elif dataStructure == '3':
      cInventory = ()
    cInventory.create_inventory("restaurant.csv")
    print("**********************************************************")
    print("**********************************************************")
    print("*****   Welcome to Menu Creation and Customization   *****")
    print("**********************************************************")
    print("**********************************************************")
    cInventory.give_options()
    a = input("Enter Number Here: ")
    if a == "0":
      exit()
      #Christian:16-46
      # want a system so that if they press a certain button they will get to a certain place
    while(a!="0"):
      if(a=="1"):
          print("\n[1] To search for the meal name\n[2] To search for the food type")
          a1 = input("Enter Number Here: ")
          if(a1=="1"):
            # if 1 is chosen we ask user for a meal name from our menu
            # and if it is on there we will print the meal and all
            #that comes with it, if not we read them a message
            #that says that item is not on the menu
            meal = str.lower(input("Enter meal name: "))
            mealInfo = cInventory.search_meal(meal)     
            if mealInfo == None:        
              cInventory.not_found()
            else:
              print(mealInfo.__str__())#just does tostada
              cInventory.give_options()
              a = input("\nEnter Number: ")
              if(a=="0"):
                
                exit() #exits program
                #if user chooses 2 we will get the meals that are a certain nationality that the user specifies
          elif(a1=="2"):
            print("Enter the Type of Food you will like to search for: ")
            type = input().capitalize()
            mealInfo = cInventory.search_type(type) 
            #if the list of meals that is a certain nationality are not on the 
            #menu we will read a message saying that it is not on our menu
            if mealInfo == None:
              cInventory.not_found()
            #if not then we will give them a list of the types
            # by concatenating from the list we made in menu
            else: 
              output = 'Type: ' + type + '\n'
              for info in mealInfo:
                output+= str('\t'+info.str()+'\n')
              print(output)
            #after this step is done we need to give more options and allow the user to 
            #continue if not they can press 0 to exit
            cInventory.give_options()
            a = input("\nEnter Number: ")
            if(a=="0"):
                
                exit() #exits program
           #yahir 47 - 72  
      elif(a=="2"): #prints menu and brings down the menu that prompts the user with the other options
        cInventory.print_menu()
        cInventory.give_options()
        a = input("\nEnter Number: ")
        if(a=="0"):
          
          exit() #exits program
  
      elif(a=="3"): #add_menu function
        print("Please insert the meal name, calories, ingredients, type, and price.")
        print("Please put quotation marks in between to separate the ingredients.")
        new_item = input()
        cInventory.add_menu("restaurant.csv", new_item)
        cInventory.give_options()
        a = input("\nEnter Number: ")
        if(a=="0"):
          
          exit() #exits program
          
      elif(a=="4"): #remove_menu
        meal = input("Enter the meal you would like to remove: ")
        cInventory.remove_menu("restaurant.csv", meal)
        cInventory.print_menu()
        cInventory.give_options()
        a = input("\nEnter Number: ")
        if(a=="0"):
          
          exit()

      # Yumong Lee 75-81
      # Doesn't work yet
      elif(a=="5"): # Edit rows within csv file
        cInventory.print_menu()
        meal=input("Enter a meal: ")
        
        calories=input("Enter ammount of calories: ")
        ingredients=input("Enter ingredients: ")
        type=input("Enter a type for the meal: ")
        price =input("Enter a price for the meal: ")
        cInventory.edit_inventory(meal, calories, ingredients, type, price)
        cInventory.give_options()
        a = input("\n Enter Number: ")
        if(a=="0"):
          
          exit()
      
@staticmethod
def menu_analysis(rand_file_name, no_queries,no_entries):
  # rand_file_name: the name of the file containing the random data
  # no_queries: the number of queries to run on the system
  # no_entries: the max number of entries in the file
  # this function is responsible for including all the necessary code to analyze the performance of the system

  # menu based on list
  cMenu = Menu()
  cMenu.create_inventory(rand_file_name)
  # menu based on the LinkedLists
  cMenu_dict = DictMenu()
  cMenu_dict.create_inventory(rand_file_name)

  #generating no_queries random queries 
  # using the random meal
  random_meal_list = []
  for i in range(0,no_queries):
      n = random.randint(1, no_entries)
      random_meal_list.append(n)
  
  #starting time calculation
  start_time = time.time()
  results1 = []
  #running the no_queries query search
  for rand_meal in random_meal_list:
    result = cMenu.search_meal(rand_meal) #changed to searchmeal
    results1.append(result)
  #calculating the time after the for loop
  end_time = time.time()
  # calculating how long it took to run the 1000 queries
  print("No of entries: "+ str(no_entries))
  print("searching " + str(no_queries) + " queries using the List based implementation: --- %s seconds ---" % (end_time - start_time))  

  # starting the time calculation for the Dict based implementation
  start_time2 = time.time()
  results2 = []
  #running the no_queries query search
  for rand_meal in random_meal_list:
    result = cMenu_dict.search_meal(rand_meal)
    results2.append(result)
  #calculating the time after the for loop
  end_time2 = time.time()
  # calculating how long it took to run the 1000 queries
  print("searching " + str(no_queries) + " queries using the Linked List based implementation: --- %s seconds ---" % (end_time2 - start_time2)) 
  
  