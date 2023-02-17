import random 
import os

def generate_data(rand_file_name, no_entries):
  file_name = "temp.csv"
  with open(file_name, "w") as writefile:
    for i in range(1, no_entries +1):
      meal_name = "pastora" + str(i)
      meal_calories = "210"
      meal_ingredients = "meat"
      meal_type = "Mexican"
      meal_price = "12"
      writefile.write(meal_name + ","+ meal_calories +","+ meal_ingredients +","+ meal_type +","+ meal_price + '\n')
  with open(file_name, 'r') as source:
    data = [(random.random(), line) for line in source]
  data.sort()
  with open(rand_file_name,'w') as target:
    for _, line in data:
      target.write(line)
  os.remove(file_name)