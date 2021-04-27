from collections import defaultdict
from collections.abc import MutableMapping
from typing import List
from task import Task
from readyqueue import ReadyQueue

class Initialize:
    task_num   : int            = 0
    total_time : int            = 0
    task       : List[Task]     = []
    rq         : ReadyQueue
    o_ui = {'A':'🟥', 'B':'🟦', 'C': '🟨','D':'🟩','E':'🟪','F':'⬜'}

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
        #> br을 사용하면 안됩니다.

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
        # [Item Underscore] Use in loop
        for _ in self.task:
            print(_)
        #> 값이 필요없는 루프에서 언더스코어를 사용하였습니다.

    def print_UI(self, output):
        for id in self.task:
            id = id.tsk_id
            print(id+'│', end = '')
            # [Item 7] Prefer enumerate Over range
            for t, target in enumerate(output):
                if target == id:
                    # [Item 16] Prefer get over in and KeyError to Handle Missing Dictionary Keys
                    print(self.o_ui.get(id,'⬛'), end = '')
                    #> 딕셔너리에 정의되어 있는 A,B,C,D,E 이외의 키값을 참조하면 검은색을 출력하게 하였습니다. 
                elif t>0 and (t) % 5 == 0:
                    print('%c' %'|', end=' ')
                else:
                    print('  ', end = '')
            #> for 문에서 index 값과 반복횟수를 모두 사용해야 하기 때문에 enumerate를 사용하였습니다.
            print()
        print('  ', end='')
        for i in range(self.total_time):
            print('──', end='')
        print()
        print("  0", end = '')
        for i in range (5, self.total_time+1, 5):
            print('%10d' %i, end='')
        print('\n')
        # [Item 4] The format built-in and str.format
        formatted = format(' '.join(map(str, output)), '<s')
        print("▶ ",formatted, end='\n\n')
        #> formatting을 사용하여 출력을 지정하여 코드를 간단하게 하였습니다.


    # [Item 14] Sort by Complex Criteria using the key Parameter
    def sort_proc(self):
        _proc = []
        f = open("./input.txt", 'r')
        
        for line in f:
            x = line.split()
            _proc.append(str(x[0], int(x[1])))
        f.close()

        print('Unsorted:', repr(_proc))
        _proc.sort(key=lambda x: x.name)
        print('\nSorted: ', )
    #> process 클래스를 선언하여 프로세스들을 도착시간에 맞게 정렬하는 함수를 구현하였습니다. 

    def print_Serv(self):
        p_id = []
        p_serv = []
        f = open("./input.txt", 'r')
        for line in f:
            x = line.split()
            p_id.append(str(x[0]))
            p_serv.append(int(x[2]))
        f.close()
        # [Item 8] : Use zip to Process Iterators in Parallel
        proc_zip = zip(p_id, p_serv)
        for name, count in proc_zip:
            print(name + count)
        #> zip을 활용하여 각 프로세스의 servicetime을 출력하는 함수를 작성하였습니다. 

    def print_parsed(self):
        # [Item 13] Prefer Catch-All Unpacking Over Slicing
        proc_id, *rest = self.task
        print(f'Process {proc_id} : {rest}')
        # input.txt파일로부터 parse한 task정보를 process id 와 나머지 정보로 나누어 한번에 출력합니다.

# [Item 18] Know How to Construct KeyDependent Default Values with
class SearchProc(dict):
    def __missing__(self, key):
        print('no match process exist!')
# Process딕셔너리를 전달받아 process id에 따라 조회할 때 만약 해당하는 프로세스가 없으면 에러메시지를 출력한다

class Proc:
    def __init__(self, name, ariv):
        self.name = name
        self.ariv = ariv

    def __repr__(self):
        return f'Tool({self.name!r}, {self.ariv})'

class proc_level:
    def __init__(self):
        # [Item 17] Prefer defaultdict over setdefault to Handle Missing Items in Internal State
        self.proc = defaultdict(int)
        # defaultdict을 통해 키에 대한 값이 없으면 값을 0으로 초기화하여 
        # process의 priority를 따로 초기화 하지 않아도 사용할 수 있도록 설정하였습니다. 
    def add(self, pname, priority):
        self.proc[pname].add(priority)

