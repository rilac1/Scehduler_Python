# scheduler

## 진행상황

### * 완료
>1 - manual  
2 - fcfs  
3 - initalize  
4 - initalize  
5 - scheduler  
6 - scheduler  
7 - initialize  
9 - initialize  
10 - scheduler   
11 - scheduler  
12 -  sjf  
13 -  
14 - initilizer   
15 -  
underscore - initalize   
16 - initialize
17 -  
18 -  
19 - scheduler
20 - readyqueue   

## usage
```
python3 scheduler.py                // user interface mode
python3 scheduler.py --mlfq -q -2   // process directly
python3 scheduler.py  --help        // help function
```
```
    Usage : scheduler.py [--help] or scheduler.py [-h]
            scheduler.py
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
            -q: time quantum

    *  If you select RR or MLFQ, You must set the time quantum.
    *  In MLFQ, Time quantum is n^i (i : priority level)

    Caution!!
    The argument [-q] should be located at last.

    *  If you want to run it as a user interface, 
      you don't need to input any arguments.
    
    'Your Python version is 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0]'
```
## Implementation

| Simulator  | Scheduler |     etc     |
| :--------: | :-------: | :---------: |
|    Task    |   Fcfs    | Iofunctions |
| ReadyQueue |    Sjf    |
|     -      |    Srt    |
|     -      |    Rr     |
|     -      |   MLFQ    |
|     -      |  Lottery  |
|     -      |  Stride   |

**`input.txt` : example**
| task id | arrival time | service time | ticket |
| :-----: | :----------: | :----------: | :----: |
|    A    |      0       |      3       |  100   |
|    B    |      2       |      6       |  100   |
|    C    |      4       |      4       |  100   |
|    D    |      6       |      5       |  100   |
|    E    |      8       |      2       |  100   |

## Link 

### 산코드 
- https://github.com/waterfogSW/Scheduler-Simulator

### 정현 코드
- https://github.com/rilac1/scheduler

## 깃허브 사용법

### 진행사항

상단 `Projects` 확인

### Branch
main branch에 대한 conflict를 방지하기위해 임계영역 수정시 새로운 branch를 생성하여 수정하고 커밋한 후 merge하기

```sh
git chekout -b kim      // `kim` branch로 이동 (-b옵션은 새로운 branch생성옵션)
git add -all            // git 으로 관리할 파일 등록
git commit -m ""        // 로컬 저장소 저장  
git push origin kim     // 원격 저장소 저장 

git checkout main       // `main` branch로 이동
git merge kim           // `main`, `kim` 병합(내용 동기화)
git push origin main    // `main` 브렌치 push
```

```sh
git status              // 현재 작업중인 branch 출력
git branch -d kim       // `kim` branch 삭제 
```

```sh
git push --set-uptream origin kim // `kim` branch를 default 원격 저장소로 지정
```
## 이전 실행결과 
![캡처](https://user-images.githubusercontent.com/28651727/116092879-2693b980-a6e1-11eb-96f0-2b44b3f0a249.PNG)
