from readyqueue import ReadyQueue
from simulator import Simulator
from fcfs import Fcfs
from sjf import Sjf

def main():
    Fcfs().simulate()
    Sjf().simulate()

if __name__ == "__main__":
    main()