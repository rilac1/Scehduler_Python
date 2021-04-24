from readyqueue import ReadyQueue
from initialize import Initialize
from fcfs       import FCFS
from sjf        import SJF
from rr         import RR
from mlfq       import MLFQ_1
from mlfq       import MLFQ_2

def main():
    
    SJF().simulate()
    FCFS().simulate()
    RR(1).simulate()
    MLFQ_1().simulate()
    

if __name__ == "__main__":
    main()