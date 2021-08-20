class Node:
    def __init__(self, initData) -> None:
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, next):
        self.next = next


class UnorderedList:
    def __init__(self) -> None:
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            return True
        else:
            return False

    def insert(self, index, item):
        current = self.head
        previous = None
        count = 0
        while current != None and count != index:
            count += 1
            previous = current
            current = current.getNext()

        if current == None:
            return False
        else:
            temp = Node(item)
            temp.setNext(current)
            if previous == None:
                self.head = temp
            else:
                previous.setNext(temp)
            return True

    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            data = self.head.data
            self.head = None
            return data
        else:
            previous.setNext(None)
            return current.data


class OrderList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    ul = UnorderedList()
    ul.add(1)
    assert ul.length() == 1
    ul.add(2)
    assert ul.length() == 2
    assert ul.search(2)
    assert ul.search(4) == False
    ul.insert(0, 10)
    assert ul.head.getData() == 10
    ul.insert(0, 20)
    assert ul.head.getData() == 20
    assert ul.head.getNext().getData() == 10
    ul = UnorderedList()
    ul.append(1)
    ul.append(2)
    assert ul.length() == 2
    ul = UnorderedList()
    for i in range(10):
        ul.append(i)
    assert ul.pop() == 9

    ol = OrderList()
    ol.add(10)
    ol.add(9)
    ol.add(13)
