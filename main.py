from readyqueue import ReadyQueue
from initialize import Initialize
from fcfs       import FCFS
from sjf        import SJF
from rr         import RR
from mlfq       import MLFQ
from lottery    import Lottery
def main():
    
    SJF().simulate()
    FCFS().simulate()
    RR(1).simulate()
    MLFQ(1).simulate()
    

if __name__ == "__main__":
    main()