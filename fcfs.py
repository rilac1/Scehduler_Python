from task import Task
from typing import List
from simulator import Simulator

class Fcfs(Simulator):
    output : List[str]
    next_idx : int = 0
    cpu_time : int = 0
    
    def simulate(self):
        self.output = [str] * self.total_time
        cur = self.task[self.next_idx]
        self.next_idx += 1
        while self.cpu_time < self.total_time:
            while self.next_idx < self.task_num and self.task[self.next_idx].ariv_t == self.cpu_time:
                self.rq.enqueue(self.task[self.next_idx])
                self.next_idx += 1
            self.output[self.cpu_time] = cur.tsk_id
            self.cpu_time += 1
            cur.rema_t -= 1
            cur.time_q -= 1
            if cur.rema_t == 0:
                cur = self.rq.dequeue()

        print("FCFS     :", '%s ' % ', '.join(map(str, self.output)))