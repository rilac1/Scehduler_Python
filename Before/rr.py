from task import Task
from typing import List
from initialize import Initialize
from readyqueue import ReadyQueue

class RR(Initialize):
    task        : List[Task] = []
    output      : List[str]
    next_idx    : int = 0
    cpu_time    : int = 0
    time_quantum: int

    def __init__(self,time_quantum = 1, queue_size = 10):
        self.parseInput()
        self.sortInput()
        self.setTotalTime()
        self.rq = ReadyQueue(queue_size)

        self.time_quantum = time_quantum
        self.setTimeQ(time_quantum)
    
    def simulate(self):
        self.output = [str] * self.total_time
        cur = self.task[self.next_idx]
        self.next_idx += 1

        tmp : Task
        flag = 0

        while self.cpu_time < self.total_time:
            while self.next_idx < self.task_num and self.task[self.next_idx].ariv_t == self.cpu_time:
                self.rq.enqueue(self.task[self.next_idx])
                self.next_idx += 1

            if flag == 1:
                self.rq.enqueue(tmp)
                cur = self.rq.dequeue()
                flag = 0
            self.output[self.cpu_time] = cur.tsk_id
            self.cpu_time += 1
            cur.rema_t -= 1
            cur.time_q -= 1

            if cur.rema_t <= 0:
                cur = self.rq.dequeue()
            elif cur.time_q <= 0:
                tmp = cur
                tmp.time_q = self.time_quantum
                flag = 1

        print()
        for i in range(self.total_time//2):
            print(end='  ')
        print('【RR】')
        self.print_UI(self.output)
    