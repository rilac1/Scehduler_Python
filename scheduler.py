import sys
import getopt
import manual
from readyqueue import ReadyQueue
from initialize import Initialize
from fcfs       import FCFS
from sjf        import SJF
from rr         import RR
from mlfq       import MLFQ_1
from mlfq       import MLFQ_2

def main():
    rr_or_mlfq = 0      # RR: 1, MLFQ: 2
    q = 0

    try:
        options, args = getopt.getopt(sys.argv[1:], 'hq:', 
        ['help', 'sjf', 'fcfs','rr','mlfq','lott'])
    
    except:
        manual.USAGE()
        exit(2)

    if len(options) == 0:
        manual.INTERFACE()

    for op in options[0]:
        if op in ("-h", "--help"):
            manual.HELP()
            exit()
        elif op == '--sjf':
            SJF().simulate()
            exit()
        elif op == '--fcfs':
            FCFS().simulate()
            exit()
        elif op == '--rr':
            rr_or_mlfq = 1
        elif op == '--mlfq':
            rr_or_mlfq = 2
        elif op == '--lott':
            LOTT().simulate()
            exit()
        elif op == '-q':
            q = op[1]
            if rr_or_mlfq==1:
                RR(q).simulate()
                exit()
            elif rr_or_mlfq==2:
                MLFQ(q).simulate()
                exit()
    if rr_or_mlfq and q==0:
        print('Error! RR or MLFQ, You must set the time quantum.')
        print('more: scheduler.py [-help] or scheduler.py [-h]')


if __name__ == "__main__": 
    main()