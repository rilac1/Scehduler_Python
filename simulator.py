from typing import List
from task import Task
from readyqueue import ReadyQueue

class Simulator:
    task_num   : int            = 0
    total_time : int            = 0
    task       : List[Task]     = []
    rq         : ReadyQueue

    def __init__(self,time_quantum = 1, queue_size = 10) :
        self.parseInput()
        self.sortInput()
        self.setTotalTime()
        self.setTimeQ(time_quantum)
        self.rq = ReadyQueue(queue_size)

    def parseInput(self):
        self.task_num = 0
        f = open("./input.txt")
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
        for _ in self.task:
            print(_)
    
