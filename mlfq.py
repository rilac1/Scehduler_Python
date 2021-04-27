from collections import defaultdict
from task import Task
from typing import List
from initialize import Initialize
from readyqueue import ReadyQueue

class MLFQ(Initialize):
    task        : List[Task] = []
    output      : List[str]
    next_idx    : int = 0
    cpu_time    : int = 0
    time_quantum: int
    MAX_LEVEL   : int = 10

    def __init__(self,time_quantum = 1, queue_size = 10):
        self.parseInput()
        self.sortInput()
        self.setTotalTime()
        self.rq = ReadyQueue(queue_size)

        self.time_quantum = time_quantum
        self.setTimeQ(1)
    
    def simulate(self):
        self.output = [str] * self.total_time
        cur = self.task[self.next_idx]
        self.next_idx += 1

        flag = 0

        while self.cpu_time < self.total_time:
            while self.next_idx < self.task_num and self.task[self.next_idx].ariv_t == self.cpu_time:
                self.rq.enqueue(self.task[self.next_idx])
                self.next_idx += 1

            if flag == 1:
                if self.rq.count > 0:
                    cur.qlevel += 1
                    cur.time_q = self.time_quantum**cur.qlevel
                    self.rq.enqueue(cur)
                    self.sortbylevel()
                    cur = self.rq.dequeue()
                else :
                    cur.time_q = self.time_quantum**cur.qlevel
                flag = 0
            
            if flag == 2:
                self.sortbylevel()
                cur = self.rq.dequeue()
                flag = 0

            self.output[self.cpu_time] = cur.tsk_id
            cur.rema_t -= 1
            cur.time_q -= 1

            if cur.rema_t <= 0:
                flag = 2
            elif cur.time_q <= 0:
                flag = 1
            self.cpu_time += 1

        print()
        for i in range(self.total_time//3):
            print(end='  ')
        print('【MLFQ】')
        self.print_UI(self.output)

    def sortbylevel(self):
        tmp_arr = [Task] * (self.rq.count+1)
        next = 1
        index = 0
        while next <= self.rq.count:
            for i in range(0, self.MAX_LEVEL):
                for j in range(1, self.rq.count + 1):
                    index = (self.rq.front + j) % self.rq.size
                    if self.rq.buff[index].qlevel == i:
                        tmp_arr[next] = self.rq.buff[index]
                        next += 1
        
        for i in range(1, self.rq.count+1):
            index = (self.rq.front + i) % self.rq.size
            self.rq.buff[index] = tmp_arr[i]
