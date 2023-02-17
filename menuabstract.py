from abc import abstractmethod
from abc import ABC


#did as group
class menuAbstract(ABC):

    @abstractmethod
    def search_meal(self, meal):
        pass

    @abstractmethod
    def search_type(self, type):
        pass

    @abstractmethod
    def add_menu(self, restaurant, new_item):
        pass

    @abstractmethod
    def remove_menu(self, restaurant, meal):
        pass

    @abstractmethod
    def print_menu(self):
        pass

    @abstractmethod
    def create_inventory(self, restaurant):
        pass

    # @abstractmethod
    # def edit_inventory(self, restaurant):
    #     pass

    @abstractmethod
    def give_options(self):
      pass

    @abstractmethod
    def not_found(self):
      pass
