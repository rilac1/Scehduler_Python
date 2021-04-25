from typing import List
from task import Task
from readyqueue import ReadyQueue

class Initialize:
    task_num   : int            = 0
    total_time : int            = 0
    task       : List[Task]     = []
    rq         : ReadyQueue

    def __init__(self,time_quantum = 1, queue_size = 10) :
        self.parseInput()
        self.sortInput()
        self.setTotalTime()
        self.rq = ReadyQueue(queue_size)

    def parseInput(self):
        self.task_num = 0
        # [Item 3] Default input and output operations
        # involving file handles follows str types instead of raw bytes
        f = open("./input.txt", 'r')
        # br을 사용하면 안됩니다.

        for line in f:
            ps = Task()
            x = line.split()
            ps.tsk_id = str(x[0])
            ps.ariv_t = int(x[1])
            ps.rema_t = int(x[2])
            ps.serv_t = int(x[2])
            ps.qlevel = 0
            ps.ticket = int(x[3])
            self.task.append(ps)
            self.task_num += 1
        f.close()
    
    def sortInput(self) :
        tmp : Task
        for i in range(self.task_num - 1, 0, -1) :
            for j in range(0, i) :
                if self.task[j].ariv_t > self.task[j].ariv_t :
                    tmp = self.task[j+1]
                    self.task[j+1] = self.task[j]
                    self.task[j] = tmp
                elif self.task[j].ariv_t == self.task[j+1].ariv_t and self.task[j].p_name > self.task[j+1].p_name :
                    tmp = self.task[j+1]
                    self.task[j+1] = self.task[j]
                    self.task[j] = tmp
    
    def setTotalTime(self) :
        sum : int = 0 
        for i in range(0, self.task_num) :
            sum += self.task[i].serv_t
        self.total_time = sum

    def setTimeQ(self, q : int) :
        for i in range(0,self.task_num) :
            self.task[i].time_q = q

    def printTask(self):
        # [Item Underscore]
        # Use in loop
        for _ in self.task:
            print(_)
        # 값이 필요없는 루프에서 언더스코어를 사용하였습니다.

    def print_UI(self, output):
        for id in self.task:
            id = id.tsk_id
            print(id+'│', end = '')
            for t in range(self.total_time):
                if output[t] == id:
                    print('🟫', end = '')
                else:
                    print('  ', end = '')
            print()
        print('  ', end='')
        for i in range(self.total_time):
            print('──', end='')
        print()
        print("  0", end = '')
        for i in range (5, self.total_time+1, 5):
            formatted = format(i, '10d')
            print(formatted, end = '')
        print('\n')
        # [Item 4] The format built-in and str.format
        formatted = format(' '.join(map(str, output)), '<s')
        print("▶ ",formatted, end='\n\n')
        