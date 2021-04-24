from task import Task
from typing import List
from initialize import Initialize
from readyqueue import ReadyQueue

class SJF(Initialize):
    task        : List[Task] = []
    output      : List[str]
    next_idx    : int = 0
    cpu_time    : int = 0
    
    def simulate(self):
        self.output = [str] * self.total_time
        cur = self.task[self.next_idx]
        self.next_idx += 1
        while self.cpu_time < self.total_time:
            while self.next_idx < self.task_num and self.task[self.next_idx].ariv_t == self.cpu_time:
                self.rq.enqueue(self.task[self.next_idx])
                self.next_idx += 1
            self.sortbyServ()
            self.output[self.cpu_time] = cur.tsk_id
            self.cpu_time += 1
            cur.rema_t -= 1
            if cur.rema_t == 0:
                cur = self.rq.dequeue()

        print()
        for i in range(self.total_time//2):
            print(end='  ')
        print('【SJF】')
        self.print_UI(self.output)

    def sortbyServ(self):
        tmp : Task
        idx : List[int] = []
        serv_tmp1 : int = 0
        serv_tmp2 : int = 0

        idx = [int] * self.rq.count
        for i in range(0, self.rq.count):
            idx[i] = (self.rq.front + i + 1) % self.rq.size

        for i in range(self.rq.count - 1, 0, -1):
            for j in range(0, i):
                serv_tmp1 = self.rq.buff[idx[j]].serv_t
                serv_tmp2 = self.rq.buff[idx[j+1]].serv_t
                if serv_tmp1 > serv_tmp2:
                    tmp = self.rq.buff[idx[j]]
                    self.rq.buff[idx[j]] = self.rq.buff[idx[j+1]]
                    self.rq.buff[idx[j+1]] = tmp
    