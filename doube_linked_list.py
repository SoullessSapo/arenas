import collections
import queue
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    def getprevious(self):
        return self.previous

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext
    def setprevious(self, newprevious):
        self.previous = newprevious


# Linked List definition
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None and self.tail == None

    def add(self, item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node
    def addleft(self,item):
        node = node(item)
        node.setprevious(self.tail)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def printList(self):
        current = self.head
        while current != None:
            if current.getData() is not None:
                print(current.getData())

            current = current.getNext()
    def printlist_backwards(self):
        current = self.tail
        while current != None:
            if current.getData() is not None:
                print(current.getData())
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    def tail(self):
        return self.tail

    def head(self):
        return self.head
    def remove(self, item):
        try:
            current = self.head
            previous = None
            found = False
            while current != None and not found:
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()

            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        except:
            return -1
    def insertion(self, data):
        y = "NIL ?"
        x = self.root

    def delete(self,Data):
        if data.previous ==
