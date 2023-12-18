from dictionary.dictAbstract import DictAbstract
class Node:
  def __init__(self, key, value):
    self.key = key #reference to the data stored inside the node
    #our data is like their key
    #and each key needs a value set to it
    self.value = value #data stored inside node
    self.next = None #pointer
  
    def __str__(self): #will allow us to print linked list instead of just printing memory location
      # we want each data to have a value
      # then point next when that box is done
      #head->|key:value|next|->|key:value|next|->null
      return str(self.key)+": "+ str(self.value)

class DictLinkedList(DictAbstract): #(DictAbstract)
  #next 2 functions
  #want to intialize the head or the front of the list
  # as well as the size of the list
  def __init__(self):
    self._head = None #the beginning of the linked list
    self._size = 0 #will track how many nodes are implemented 
    
  def __len__(self): #will return length of the linked list
    return self._size
  #will say if the term or var
    #we are looking for is in this list
    #uses _find for it
  
  #Yumong
  def __contains__(self, key):
    return not self.find(key)#taking out head

  #Yumong
  def __getitem__(self, key):
    index = self.find(key)
    if index == None:
      raise KeyError("Item does not exist")
    return index

    
  # what would be our equivalent to node. 
    #would it be index?

  #Yumong
  #Maybe another way of doing _find
  # Checks to see whether key is present in the Linked List
  def find(self, key):
    present = self._head #Initialize present to head
    while present != None: # Keeps looping until present doens't equal to None
      if present.key == key:
        return True
      present = present.next

    return False
      
    #we don't have the thing in binary tree where we can check left or right
  #  we just need to check if the next value is the answer we asked for and if not check the next, until we either find it or it returns null because thats the end of the list
    
  def pop(self, key):
    value = self[key]
    self._remove(key)
    return value
  

  
  def _remove(self,key):

    # check if the head itself is bad
    prev = 0
    curr = self._head
    #switch prev with current
    if curr != None:
      if curr.key == key:
        self._head = curr.next
        curr = None
        return
    # check to see if others are None
    while curr != None:
      if curr.key == key:
        break
      prev = curr 
      curr = curr.next
    # if list has nothing in it
    if curr == None:
      print("Nothing in this node")
      return
    #deleting
    prev.next = curr.next
    curr = None
          
 
  def __setitem__(self, key, value): #will create the value for the dictionary
    if self._head == None: 
      self._head = Node(key, value) #makes value the information stored in the node if there is nothing in value already
      self._size += 1 
    else:
      self._insert(key, value) #if something is stored in value, it will call the insert function and set the new value 
 
  def _insert(self, key, value): #inserts node to the front of a linked list
    node = Node(key, value) #creates new node
    node.next = self._head #will point the new node to head 
    self._head = node #makes the new node the head of the linked list
    
  def printLL(self): #will be called to main to print out contents of linked list
    if self._head == None: 
      print("Linked list is empty")
    else: 
      n = self._head
      while (n != None):
        print(str(n.key) + ":"+ str(n.value))
        n = n.next #reinitalizes head by pointing it to the next node

