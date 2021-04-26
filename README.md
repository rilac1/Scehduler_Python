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

14 - `Key` 값을 이용해서 정렬.   
    : `(ariv_t, serv_t)` 딕셔너리로 만들어서 정렬하면 좋을듯.    
15 - underscore - initalize   
16 - initialize  
19 - 함수의 반환값이 3개 이상이면 안된다.  
20 - readyqueue   

*총 12개 완료함*

---
### * 미완
> 8 - 여러개의 리스트에서 동일한 인덱스를 사용할 때 `zip`을 사용해라.  
12 - 슬라이싱과 인덱싱을 한번에 하지 마라.  
13 - 슬라이싱 보다는 언패킹을 사용해라.  
**<14~18> 딕셔너리 관련**
17 - `defaultdick` 를 사용해서 키가 없는 경우를 처리해라.  
18 - `__missing__`를 사용해서 키에 따라 다른 디폴트 값을 생성해라.  

## usage
```
python3 scheduler.py                // user interface mode
python3 scheduler.py --mlfq -q -2   // process directly
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
