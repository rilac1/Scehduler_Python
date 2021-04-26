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

    # [Item 16] 
    try:
        # [Item 6] Unpacking allows for assigning multiple values in a single statement.
        # [Item 11] Know How to Slice Sequences
        # [Item 19] Never Unpack More Than Three Variables When Functions Return Multiple Values
        options, args = getopt.getopt(sys.argv[1:], 'hq:', ['help', 'sjf', 'fcfs','rr','mlfq','lott'])
        #> getopt()는 두 개의 List를 반환하기 때문에 이들을 Unpacking하여 두 개의 변수에 대입시켰습니다.
        #> 인자를 받을 때 함수 이름에 해당하는 인자는 필요없기 때문에 [1:]로 slice해 주었습니다.
        #> 함수의 반환값을 2개로 제한하였습니다.
    
    except:
        manual.USAGE()
        exit(2)

    if len(options) == 0:
        manual.INTERFACE()
    # [Item 5] Write Helper Functions Instead of Complex Expressions
    helper(options)
    # 복잡한 식 대신에 helper 함수를 따로 작성하여서 프로그램을 모듈화하였고 이를 통해 main 함수를 간결하게 하였습니다.

def helper(options):
    for op in options:
        # [Item 10] Issue 3. Simulate switch-case statement
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
        #> else - if 문을 elif 문으로 사용하여 가독성을 높였습니다.
            if rr_or_mlfq==1:
                RR(q).simulate()
                exit()
            elif rr_or_mlfq==2:
                MLFQ(q).simulate()
                exit()
    # [Item9] Avoid else Block after for and
    else:
        print('Error! RR or MLFQ, You must set the time quantum.')
        print('more: scheduler.py [-help] or scheduler.py [-h]')
    #> for문을 모두 수행했다면 어떤 조건도 만족하지 못했다는 뜻이므로 에러처리를 해주기 위해 for-else문을 사용하였습니다.



if __name__ == "__main__": 
    main()