class CircularQueue:  
    def __init__(self, max_size):
        #최대 크기, queue 생성, 필요한 포인터 초기화
        self.max_size = max_size
        self.front = 0
        self.rear = 0 #하나 들어오면 rear값이 1씩 늘어남. 하나 나가면 front값이 1씩 늘어남
        self.queue = [None] * max_size 

    def enqueue(self, data):
        if(self.size() == self.max_size):
            return None
        self.queue[self.rear % self.max_size] = data
        self.rear += 1    
        return True

    def dequeue(self):
        if(self.size() == 0):
            return None
        data = self.queue[self.front % self.max_size]
        self.queue[self.front % self.max_size] = None
        self.front += 1
        return data

    def is_full(self):
        if(self.size() == self.max_size):
            return True
        return False

    def is_empty(self):
        if(self.size() == 0):
            return True
        return False

    def size(self):
        return self.rear - self.front


if __name__ == "__main__":
    q = CircularQueue(3)
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Enque 10", q.enqueue(10))
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())
    print("Enque 20", q.enqueue(20))
    print("Enque 30", q.enqueue(30))
    print("Enque 40", q.enqueue(40))
    print("Deque", q.dequeue())
    print("Enque 50", q.enqueue(50))
    print("Deque", q.dequeue())
    print("Deque", q.dequeue())
    print("Enque 60", q.enqueue(60))
    print("Enque 70", q.enqueue(70))

    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print(len(q.queue)) # should be 4. list 자체의 크기는 변하지 않아야 함


"""
Empty? True , Full? False , Size= 0
Enque 10 True
Empty? False , Full? False , Size= 1
Enque 20 True
Enque 30 True
Enque 40 None
Deque 10
Enque 50 True
Deque 20
Deque 30
Enque 60 True
Enque 70 True
Empty? False , Full? True , Size= 3
Deque 50
Empty? False , Full? False , Size= 2
Deque 60
Empty? False , Full? False , Size= 1
Deque 70
Empty? True , Full? False , Size= 0
Deque None
Empty? True , Full? False , Size= 0
4
"""