from SLDict import SLDict
class Interface2:
  dict = SLDict() #creates instance for SLDict class
  print("#####################################################")
  print("#####################################################")
  print("###############      Our code     ###################")
  print("#####################################################")
  print("#####################################################")
  a = (input("1 for print, 2 for remove, 3 for adding, 0 for ending program: "))
  if a == "0":
      exit()
  while(a != "0"):
    if a == "1": #print
      dict.print_LL()
      dict.giveOptions()
      a = input("New a: ")
      if a == "0":
        exit()
    elif a == "2": #remove
      key = int(input("What key do you want deleted: "))
      dict.remove(key)
      dict.giveOptions()
      a = input("New a: ")
      if a == "0":
        exit()
    elif a == "3": #add you gotta do add first
      key = int(input("Please add the key that you want to add into the list: "))
      value = input("Please add the value that you want to add into the list: ")
      dict.insert(key, value)
      dict.giveOptions()
      a = input("give me a: ")
      if a == "0":
        exit()
    
  