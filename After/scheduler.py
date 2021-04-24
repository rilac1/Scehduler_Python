import sys
import getopt
import manual
from readyqueue import ReadyQueue
from initialize import Initialize
from fcfs       import FCFS
from sjf        import SJF
from rr         import RR
from mlfq       import MLFQ
from lottery    import LOTT

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

    for op in options:
        if op[0] in ("-h", "--help"):
            manual.HELP()
            exit()
        elif op[0] == '--sjf':
            SJF().simulate()
            exit()
        elif op[0] == '--fcfs':
            FCFS().simulate()
            exit()
        elif op[0] == '--rr':
            rr_or_mlfq = 1
        elif op[0] == '--mlfq':
            rr_or_mlfq = 2
        elif op[0] == '--lott':
            LOTT().simulate()
            exit()
        elif op[0] == '-q':
            q = int(op[1])
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