from task import Task
from typing import List
from initialize import Initialize
from readyqueue import ReadyQueue

class FCFS(Initialize):
    task        : List[Task] = []
    output      : List[str]
    next_idx    : int = 0
    cpu_time    : int = 0
    
    def simulate(self):
        self.output = [str] * self.total_time
        cur = self.task[self.next_idx]
        self.next_idx += 1
        while self.cpu_time < self.total_time:
                # [Item 2] Expressions and statements
            while self.next_idx < self.task_num and \
                self.task[self.next_idx].ariv_t == self.cpu_time:
                # 긴 조건문을 두 줄로 나누어서 가독성을 높여주었습니다.
                # '\' 사용.
                self.rq.enqueue(self.task[self.next_idx])
                self.next_idx += 1
            self.output[self.cpu_time] = cur.tsk_id
            self.cpu_time += 1
            cur.rema_t -= 1
            if cur.rema_t == 0:
                cur = self.rq.dequeue()

        print()
        for i in range(self.total_time//2):
            print(end='  ')
        print('【FCFS】')
        self.print_UI(self.output)