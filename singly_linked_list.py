class SinglyLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        if (self.head != None):
            self.next = self.head
            self.head = self.Node(value)
            self.head.next = self.next
        else:
            self.head = self.Node(value)

    def insert_tail(self, value):
        if (self.head == None):
            self.head = self.Node(value)
        else:
            p = self.head
            while p.next:
                p = p.next
            temp = p
            temp.next = self.Node(value)

    def delete_head(self):
        v = self.head.value
        self.head = self.head.next
        return v


list = SinglyLinkedList()
list.insert_head(5)
list.insert_head(10)
list.insert_head(3)
v = list.delete_head()
print(v) #3

list.insert_tail(7)
list.insert_tail(2)

p = list.head
while p:
    print(p.value, end = " ")
    p = p.next # 한 바퀴 돔
print()
    # 출력 결과 : 10 5