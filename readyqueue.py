from typing import List
from task import Task

class ReadyQueue:
    front   : int
    rear    : int
    count   : int
    size    : int 
    buff    : List[Task]

    def __init__(self,_size) :
        self.front  = _size - 1
        self.rear   = _size - 1
        self.count  = 0
        self.size   = _size
        self.buff   = [Task] * _size
    
    def enqueue(self, item : Task) :
        self.rear = (self.rear + 1) % self.size
        if self.rear == self.front :
            self.rear -= 1
        else :
            self.buff[self.rear] = item
        self.count += 1
    
    def dequeue(self) :
        # [Item 20] Prefer Raising Exceptions to Returning None
        """
        if self.front == self.rear :
            return None
        """
        try: 
            self.front == self.rear
        except: 
            dequeue_Error
            return False, None
        #> 에러가 확실하게 드러날 수 있게 None을 반환하지 않고 예외처리를 발생시켰습니다.

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