import sys
import getopt
from readyqueue import ReadyQueue
from initialize import Initialize
from fcfs       import FCFS
from sjf        import SJF
from rr         import RR
from mlfq       import MLFQ
from lottery    import LOTT

usage = """
    Usage : scheduler.py [--help] or scheduler.py [-h]
            scheduler.py
            scheduler.py [--sjf]
            scheduler.py [--fcfs]
            scheduler.py [--lott]
            scheduler.py [--rr] [-q num]
            scheduler.py [--mlfq] [-q num]
    """

supplement = """
            -- sjf: Shortest Job First
            -- fcfs: First Come First Served
            -- lott: Lottery
            -- rr: Round Robin
            -- mlfq: Multi Level Feedback Queue
            -q: time quantum

    *  If you select RR or MLFQ, You must set the time quantum.
    *  In MLFQ, Time quantum is n^i (i : priority level)

    Caution!!
    The argument [-q] should be located at last.

    *  If you want to run it as a user interface, 
      you don't need to input any arguments.
    
    'Your Python version is %s'
    """ %sys.version  # [Item 1] Check the version of your Python
    #> 사용자들에게 실행중인 파이썬의 버전을 알려주기 위해 Item 1을 사용하였습니다.

def HELP():
    print(usage, end='')
    print(supplement)
    exit()

def USAGE():
    print(usage)

def INTERFACE():
    interface = """
┌────────────────────────────────────────┐
│ *Choose the type of Scheduler.*        │
│                                        │
│  1: SJF (Shortest Job First            │
│  2: FCFS (First Come First Served)     │
│  3: RR (Round Robin)                   │
│  4: MLFQ (Multi Level Feedback Queue   │
│  5: Lottery                            │
└────────────────────────────────────────┘
    """
    op = 0
    print(interface)
    print('Input a number from 1 to 5: ', end='')
    op = int(input())

    if op == 1:
        SJF().simulate()
    elif op == 2:
        FCFS().simulate()
    elif op == 5:
        LOTT().simulate()
    elif op == 3:
        print('Set the time quantum: ', end = '')
        q = int(input())
        RR(q).simulate()
    elif op == 4:        
        print('[Time quantum = nⁱ (i: priority level)]')
        print('Input n: ', end = '')
        q = int(input())
        MLFQ(q).simulate()
    else:
        print('Error! Input a number from 1 to 5')