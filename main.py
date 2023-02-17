from interface import interface
from random_file import generate_data

import interface
def main_analysis():
  no_entries = int(input('Enter number of entries into the file for testing\nenter here: '))
  file_name = "rand_file_"+str(no_entries)+".txt"
  generate_data(file_name, no_entries)
  interface.menu_analysis(file_name, no_entries, no_entries)#changed car analysis to menu analysis
if __name__ == "__main__":
  choice = int(input('[0] - testing speed with different data structures\n[1] - for menu Creation\nEnter Here: '))
  if choice == 0:
    main_analysis()
  elif choice == 1:
    interface()




  


