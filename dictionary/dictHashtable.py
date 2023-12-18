from dictionary.dictAbstract import DictAbstract 
# this class will be like linkedlist
#ask about needing an abstract class for hashtable
class DictHashtable(DictAbstract):
  def __init__(self):
    self.__size = 18 #place holder changed from 100 to 18
    self.arr = [None] * self.__size # would be the list of meals

  def __str__(self):
    return str(self.key) + ": " + str(self.value)
    
  def __len__(self):
    return self.__size

  def __contains__(self,key):
    return not self.search(key)

  def __getitem__(self, key): 
    search_key = self.search(key)
    if search_key == None:
      return None #will return none if serarch_key is None
    return search_key

  def __setitem__(self, key, value):
    self.add(key, value)
    
  def pop(self, key): 
    value = self[key]
    self.delete(key)
    return value
    
  def hashFunction(self, key):  
    hash = 0
    for i in str(key):
      hash += ord(i)
    return hash % self.__size
    
  def delete(self, key):
    #to delete an item from a hash table, we need to know the key and with that we get rid of the value corresponding to the key. 
    # We do not have to worry about the  order of the hash table, so it's fine
    hashing = self.hashFunction(key)
    # getting a variable and setting it
    #to the return valued from hashFunction
    if self.arr[hashing] is None:
       return None
    # if it's not empty, then we need to go through 
      #our list and check if the encoded key
      #is equal to our given key, if we go through
      #and it is equal then it is going to pop it out
    i = 0
    while i<self.__size:
      if self.arr[hashing][i][0]==key:
        self.arr[hashing].pop(i)
        break
      else:
        i+=1
  #| will add to the hash table by checking if table is empty, if it is then it adds the key and value to the table. 
  # If it is not empty then it checks if the key exists in the table already. If the key does exists it updates the value to the next index. 
  # If the key doesn't exist, it will append the the key to the hash table along with its value. 
  def add(self,key, value): 
    hashing = self.hashFunction(key)
    key_value = [key, value] #list holds key and value
    if self.arr[hashing] is None:
      self.arr[hashing] = list([key_value]) #if table[self.arr[hashing] is empty, it creates a list object containing key and value within the table
    else:
      i = 0
      while self.arr[hashing][i][0]==key:
        i+=1
      self.arr[hashing][i][1] = value 
      self.arr[hashing].append(key_value) #if new key, it just adds to the table
      
  def printLL(self):
    for item in self.arr:
      if item != None: # self.arr[hashing]
        for value in item: # looping through self.arr[hashing]
          print(value[1])

  def search(self, key):
    hashing = self.hashFunction(key)
    if self.arr[hashing] is not None:
        for i in self.arr[hashing]:
            if i[0] == key:
                return i[1]
    return None
  
    # table = ""
    # table += value[1] 
    # table += "\n"      
    # outside the for loop: return table   

  def __iter__(self): 
    self.arr = 1
    return self

  def __next__(self): #just putting how it should look like
    x = self.a
    self.a += 1
    return x
    