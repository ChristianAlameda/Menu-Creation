'''
Implement a sorting function 
Reimplement the search function to search faster
inherit from dinct linked List which is inheriting from Dict Abstract
'''

from dictionary.dictAbstract import DictAbstract

class DictSortedLL(DictAbstract):
  
  def __init__(self): #constructor building list
    self.key = []
    self.value = []
    #[10:burgers, 12:tacos, 15:bananas, 20: cheese]
    #[#][value]
    #2d list

  #getting the length of the dictionary
  def __len__(self):
    return len(self.key)
  
  # will show if the dictionary contains an item
  def __contains__(self,key):
    return not self.binarySearch(key)

  #dont know if we need get and set
  # will go through the dictionary and get the item or items we need
  def __getitem__(self,key):
    index = self.binarySearch(key)
    if index == None:
      raise KeyError("item does not exist")
  
  #will grab the item from get item and set it so we can use it
  def __setitem__(self,key,value):
    if self.value == None:
      print("There are no keys nor value")
    else:
      self.key.append(key)
      self.value.append(value)
      
  def printLL(self):
    if self.key == None:
      print("there are no keys or values stored")
    else:
      for i in range(0, len(self.key)):
        print(str(self.key[i]) + ":" + str(self.value[i]))

  def pop(self,key): 
    value = self[key]
    self.remove(key)
    return value
  
  def remove(self, input1): 
    search = self.binarySearch(input1) #turns key into a value
    for i in range(0, len(self.value)):
        if self.value[i] == search: #checks if value found is equal to the one we want
            self.value.pop(i) and self.key.pop(i) #will pop both elements out of each list
            break

  
  '''
  insert will act as our add
  and we will give a newKey and a new Value
  and that newKey and Value will go into the 
  self.key and self.value list respectively
  '''
  def insert(self, newKey, newValue):
    self.key.append(newKey)
    self.value.append(newValue)
    self.shellSort()
  '''
  shell_sort() won't take any arguments
  it will have both arrays through the self
  keyword and we want to use floor division on
  the length of the the key value list and 
  do it by 2 and while interval is less than
  0 we will go from interval to the length of the list
  keep a temp and a temp1 for both of our arrays so they
  can move together
  

  '''
  '''
  It's more eficient than insertion and   bubble, and less complicated 
  than mergesort or quicksort especially with two lists working   
  simultaneously
  
  '''
  def shellSort(self):
    array = self.key
    array1 = self.value
    n = len(array)
    interval = n // 2
    while interval > 0:
      for i in range(interval, n):
        temp = array[i]
        temp1 = array1[i]
        j = i
        while j >= interval and array[j - interval] > temp and array1[j-interval]:
          array[j] = array[j-interval]
          array1[j] = array1[j-interval]
          j -= interval
        array[j] =temp
        array1[j] = temp1
      interval //= 2

    #print("new self.key: "+str(self.key))
    #print("new self.value: "+ str(self.value))
    #return self.key not needed
    '''
     returns either the index of the key in question
     or if the key is not Found then it will return
     not found
    
    '''

  def binarySearch(self,x):
    low = 0
    high = len(self.key) - 1
    array = self.key
    while low <= high:
      mid = low + (high - low) // 2
      if array[mid] == x:
        # mid represents the index of the found key in the self.key array
        # accessing the value array with the mid index to return the 
        # value corresponding to the found key 
        # self.key[1], self.value[1]
        return self.value[mid]
      elif array[mid] < x:
        low = mid + 1
      else:
        high = mid - 1
    return None
    
  def giveOptions(self):
    print("1 for print, 2 for remove, 3 for adding, 0 for ending program: ")
