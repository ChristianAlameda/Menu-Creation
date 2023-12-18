import csv
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llStr = ''
        while itr:
            llStr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llStr)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insertAt(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid Index")

        if index == 0:
            self.insertAtBeginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def removeAt(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insertValues(self, dataList):
        self.head = None
        for data in dataList:
            self.insertAtEnd(data)

    def search(self, x):
        current = self.head
        while current is not None:
            if current.data == x:
                return True  # data found

            current = current.next
        return False  # data not found
