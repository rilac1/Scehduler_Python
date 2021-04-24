import sys
import getopt
from readyqueue import ReadyQueue
from initialize import Initialize
from fcfs       import FCFS
from sjf        import SJF
from rr         import RR
from mlfq       import MLFQ_1
from mlfq       import MLFQ_2

def HELP():
    usage = """
    Usage : scheduler.py [--help] or scheduler.py [-h]
            scheduler.py [--sjf]
            scheduler.py [--fcfs]
            scheduler.py [--lott]
            scheduler.py [--rr] [-q num]
            scheduler.py [--mlfq] [-q num]

            -- sjf: Shortest Job First
            -- fcfs: First Come First Served
            -- lott: Lottery
            -- rr: Round Robin
            -- mlfq: Multi Level Feedback Queue
            -q: tume quantum

    *  If you choose RR or MLFQ, You must set the time quantum.
    *  At MLFQ, if you set a time quantum as a negative number (ex. -n),
      it is handeld internally by n^i (i means a level of MLFQ')

    Caution!!
    The argument [-q] must be entered last.

    *  If you want to run it as a user interface, 
      you don\'t need to enter any arguments.

    """
    print(usage)
    print('This program was developed in Python version ' + sys.version)
    exit()


def INTERFACE():
    op = 0
    print('*Choose the type of Scheduler.*')
    print('1: SJF (Shortest Job First)')
    print('2: FCFS (First Come First Served')
    print('3: RR (Round Robin')
    print('4: MLFQ (Multi Level Feedback Queue')
    print('5: Lottery\n')

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
        print('[If you want to set the time quantum according to the level, \n'
        + 'input the time quantum as negative a number]')
        print('Set the time quantum', end = '')
        q = int(input())
        if q>0:
            MLFQ_1(q).simulate()
        else:
            MLFQ_2(q).simulate()
    else:
        HELP()

    exit()