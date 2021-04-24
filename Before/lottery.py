import random
from task import Task
from typing import List
from initialize import Initialize
from readyqueue import ReadyQueue

class LOTT(Initialize):
    task        : List[Task] = []
    output      : List[str]
    next_idx    : int = 0
    cpu_time    : int = 0
    
    def simulate(self):
        self.output = [str] * self.total_time
        cur : Task
        self.rq.enqueue(self.task[0])
        while self.cpu_time < self.total_time:
            while self.next_idx < self.task_num and self.task[self.next_idx].ariv_t == self.cpu_time:
                self.rq.enqueue(self.task[self.next_idx])
                self.next_idx += 1
            cur = self.get_winner()
            cur.rema_t -= 1
            self.output[self.cpu_time] = cur.tsk_id
            self.cpu_time += 1
            if cur.rema_t <= 0:
                self.rq.del_data(cur)

        print()
        for i in range(self.total_time//2):
            print(end='  ')
        print('【Lottery】')
        self.print_UI(self.output)

    def getTotaltickets(self):
        total_ticket = 0
        index = 0
        for i in range(1,self.rq.count + 1):
            index = (self.rq.front + i) % self.rq.size
            total_ticket += self.rq.buff[index].ticket
        return total_ticket
    
    def get_random(self):
        total = self.getTotaltickets()
        if total == 0: return 0
        return random.randrange(0, total)

    def get_winner(self):
        counter = 0
        index = 0
        winner = self.get_random()
        for i in range(1,self.rq.count+1):
            index = (self.rq.front + i) % self.rq.size
            counter += self.rq.buff[index].ticket
            if counter > winner:
                return self.rq.buff[index]

def main():
    LOTT().simulate()

if __name__ == "__main__": 
    main()