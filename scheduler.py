import sys
import getopt
import usage
from readyqueue import ReadyQueue
from initialize import Initialize
from fcfs       import FCFS
from sjf        import SJF
from rr         import RR
from mlfq       import MLFQ_1
from mlfq       import MLFQ_2

def main():
    rr_or_mlfq = 0      # RR: 1, MLFQ: 2
    options = getopt.getopt(sys.argv[1:], 'help:h:sjf:fcfs:rr:mlfq:q')
    
    if options.len == 0:
        usage.INTERFACE()

    for  op in options:
        if op == '-help' or op == '-h':
            usage.HELP()
        elif op == '-sjf':
            SJF().simulate()
        elif op == '-fcfs':
            FCFS().simulate()
        elif op == '-lott':
            LOTT().simulate()
        elif op == '-rr':
            rr_or_mlfq = 1
        elif op == '-mlfq':
            rr_or_mlfq = 2
        elif op == '-q':
            q = op
            if rr_or_mlfq==1:
                RR(q).simulate()
            elif rr_or_mlfq==2:
                if q>0:
                    MLFQ_1(q).simulate()
                else:
                    MLFQ_2(q).simulate()
        else:
            usage.HELP()
    

if __name__ == "__main__":
    main()