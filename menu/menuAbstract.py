from abc import abstractmethod, ABC

class MenuAbstract(ABC):

    @abstractmethod
    def searchMeal(self, meal):
        pass

    @abstractmethod
    def searchType(self, mealType):
        pass

    @abstractmethod
    def addMenu(self, restaurant, newItem):
        pass

    @abstractmethod
    def removeMenu(self, restaurant, meal):
        pass

    @abstractmethod
    def printMenu(self):
        pass

    @abstractmethod
    def createInventory(self, restaurant):
        pass

    # @abstractmethod
    # def editInventory(self, restaurant):
    #     pass

    @abstractmethod
    def giveOptions(self):
        pass

    @abstractmethod
    def notFound(self):
        pass
