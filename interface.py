from entry import Entry
from menu import Menu
class Interface: #Holds the function for the interface
    cInventory = Menu()
    cInventory.create_inventory("restaurant.csv")
    print("***********************************************************")
    print("***********************************************************")
    print("*   Welcome to Menu Creation and Customization   *")
    print("***********************************************************")
    print("***********************************************************")
    cInventory.give_options()
    a = input("Enter Number Here: ")
    if a == "0":
      cInventory.exit()
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
              print(mealInfo.__str__())
              cInventory.give_options()
              a = input("\nEnter Number: ")
              if(a=="0"):
                cInventory.exit() #exits program
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
                output+= str('\t'+info.__str__()+'\n')
              print(output)
            #after this step is done we need to give more options and allow the user to 
            #continue if not they can press 0 to exit
            cInventory.give_options()
            a = input("\nEnter Number: ")
            if(a=="0"):
                cInventory.exit() #exits program
      elif(a=="2"): #prints menu and brings down the menu that prompts the user with the other options
        cInventory.print_menu()
        cInventory.give_options()
        a = input("\nEnter Number: ")
        if(a=="0"):
          cInventory.exit() #exits program
  
      elif(a=="3"): #add_menu function
        print("Please insert the meal name, calories, ingredients, type, and price.")
        print("Please put quotation marks in between to separate the ingredients.")
        new_item = input()
        cInventory.add_menu("restaurant.csv", new_item)
        cInventory.give_options()
        a = input("\nEnter Number: ")
        if(a=="0"):
          cInventory.write_back("restaurant.csv")
          cInventory.exit() #exits program
          
      elif(a=="4"): #remove_menu
        meal = input("Enter the meal you would like to remove: ")
        cInventory.remove_menu("restaurant.csv", meal)
        cInventory.print_menu()
        cInventory.give_options()
        a = input("\nEnter Number: ")
        if(a=="0"):
          cInventory.write_back("restaurant.csv")
          cInventory.exit()

      elif(a=="5"): # Edit rows within csv file
        cInventory.print_menu()
        cInventory.edit_inventory("restaurant.csv")
        cInventory.give_options()
        a = input("\n Enter Number: ")
        if(a=="0"):
          cInventory.exit()
          
          
          
          
      elif a=="6":
        cInventory.close_csv()
        print("Restaurant.csv closed")
        cInventory.give_options()
        a = input("\n Enter Number: ")
        if(a=="0"):
          cInventory.exit()
      elif a=="7":
        cInventory.open_csv()
        cInventory.give_options()
        a = input("\n Enter Number: ")
        if(a=="0"):
            cInventory.exit()  
      elif a=="8":
        cInventory.transfer()
        print("file was transferred")
        cInventory.give_options()
        a = input("\n Enter Number: ")
        if(a=="0"):
            cInventory.exit()
 
              
          
          
