from typing import List
import Task

class ReadyQueue:
    buff  : List[Task] = []
    front : int = 0
    rear  : int = 0
    count : int = 0

    def __init__(self,_size) :
        self.front  = _size - 1
        self.rear   = _size - 1
        self.count  = 0
        self.size   = _size

    def enqueue(self, item : Task) :
        self.rear = (self.rear + 1) % self.size
        if self.rear == self.front :
            self.rear -= 1
        else :
            self.buff[self.rear] = item
        self.count
    
    def dequeue(self) :
        if self.front == self.rear :
            return None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return self.buff[self.front]

    def del_data(self, p : Task) :
        count = self.count
        tmp : Task
        for _ in range(count):
            tmp = self.dequeue()
            if tmp != p :
                self.enqueue(tmp)

    def getFront(self) :
        return self.buff[(self.front + 1) % self.size]