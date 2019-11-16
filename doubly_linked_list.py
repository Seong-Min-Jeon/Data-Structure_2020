class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
        def __str__(self):
            return f"NODE[{self.value}]"

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        if(self.size == 0):
            return True
        else:
            return False

    def add_after(self, node, value):
        temp1 = node
        temp2 = node.next
        new_node = self.Node(value)
        temp1.next = new_node
        new_node.next = temp2
        new_node.prev = temp1
        temp2.prev = new_node
        self.size += 1
#
    def add_before(self, node, value):
        temp1 = node
        temp2 = node.prev
        new_node = self.Node(value)
        temp1.prev = new_node
        new_node.prev = temp2
        new_node.next = temp1
        temp2.next = new_node
        self.size += 1

    def add_head(self, value):
        if(self.is_empty() == True):
           self.head = self.Node(value) 
           self.tail = self.head
           self.size += 1
        else:
            node = self.head
            self.head = self.Node(value)
            self.head.next = node
            node.prev = self.head
            self.size += 1  

    def add_tail(self, value):
        if(self.is_empty == True):
            self.head = self.Node(value) 
            self.tail = self.head
            self.size += 1
        else:
            node = self.tail
            self.tail = self.Node(value)
            self.tail.prev = node
            node.next = self.tail
            self.size += 1

    def remove(self, node):
        if (node == self.head):
            self.remove_head()
        elif (node == self.tail):
            self.remove_tail()
        else:
            if(self.is_empty == True):
                return None
            temp1 = node.prev
            temp2 = node.next
            temp1.next = temp2
            temp2.prev = temp1
            self.size -= 1

    def remove_head(self):
        if(self.is_empty == True):
            return None
        else:
            temp = self.head.next
            self.head = temp
            try:
                temp.prev = None
            except:
                pass
            self.size -= 1

    def remove_tail(self):
        if(self.is_empty == True):
            return None
        else:
            temp = self.tail.prev
            self.tail = temp
            try:
                temp.next = None
            except:
                pass
            self.size -= 1

    def traverse(self, dir = 1):
        # generator를 이용하여 리스트를 정방향(dir=1) 혹은 역방향(dir=-1)으로 순회할 수 있도록 함
        node = self.head.next if dir == 1 else self.head.prev
        while node != self.head:
            yield node
            node = node.next if dir == 1 else node.prev

    def find(self, value, from_node = None):
        if(from_node == None):
            p3 = self.head
        else:
            p3 = from_node.next
        idx2 = 0
        while(p3.value != value and idx2 < self.size):
            p3 = p3.next
            idx2 += 1
        if(idx2 >= self.size):
            return None
        else:
            return p3

    def print(self, dir = 1):
        """
        print("FORWARD: " if dir==1 else "BACKWARD:", end = "")
        if(self.size == 0):
            print()
            return
        for node in self.traverse(dir):
            print(node.value, end="->")
        print()
        """
        #이해를 못해서 singly linked list와 비슷하게 만들었습니다.
        if(dir == 1):
            p = self.head
            print("FORWARD: ",end="")
            while p:
                print(p.value, end="->")
                p = p.next
            print()
        else:
            p = self.tail
            print("BACKWARD: ",end="")
            while p:
                print(p.value, end="->")
                p = p.prev
            print()

if __name__ == "__main__":
    list = LinkedList()
    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())
    list.add_head(1)
    list.add_head(3)
    list.add_tail(3)
    list.add_tail(4)
    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())
    a = list.find(3)
    print(a)
    b = list.find(3, from_node=a)
    print(b)
    list.add_before(b, 9)
    list.add_after(b, 5)

    list.print()
    list.print(-1)

    c = list.find(4)
    list.remove(c)

    list.print()
    list.print(-1)

    list.remove_head()
    list.remove_head()

    list.print()
    list.print(-1)

    list.remove_tail()
    list.remove_tail()

    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())

    list.remove_head()
    list.print()
    print("IS_EMPTY?", list.is_empty())


"""
FORWARD:
BACKWARD:
IS_EMPTY? True
FORWARD: 3->1->3->4->
BACKWARD: 4->3->1->3->
IS_EMPTY? False
NODE[3]
NODE[3]
FORWARD: 3->1->9->3->5->4->
BACKWARD: 4->5->3->9->1->3->
FORWARD: 3->1->9->3->5->
BACKWARD: 5->3->9->1->3->
FORWARD: 9->3->5->
BACKWARD: 5->3->9->
FORWARD: 9->
BACKWARD: 9->
IS_EMPTY? False
FORWARD:
IS_EMPTY? True
"""