from readyqueue import ReadyQueue
from initialize import Initialize
from fcfs import Fcfs
from sjf import Sjf

def main():
    
    Sjf().simulate()
    Fcfs().simulate()

if __name__ == "__main__":
    main()