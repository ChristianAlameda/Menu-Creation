from abc import ABC, abstractmethod
class DictAbstract(ABC):
  #setting all our magic methods
  @abstractmethod
  #getting the length of the dictionary
  def __len__(self):
    pass
  @abstractmethod
  # will show if the dictionary contains an item
  def __contains__(self,key):
    pass
  @abstractmethod
  #dont know if we need get and set
  # will go through the dictionary and get the item or items we need
  def __getitem__(self,key):#getitem
    pass
  @abstractmethod
  #will grab the item from get item and set it so we can use it
  def __setitem__(self,key,value):
    pass
  
  @abstractmethod
  def printLL(self):
    pass
  @abstractmethod
  def pop(self,key):
    pass
  