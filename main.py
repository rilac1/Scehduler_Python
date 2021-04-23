from readyqueue import ReadyQueue
from simlator import Simulator

def main():
    s = Simulator()
    for _ in s.task:
        print(_)

if __name__ == "__main__":
    main()