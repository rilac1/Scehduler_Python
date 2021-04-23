# scheduler

## Implementation

| Simulator  | Scheduler |     etc     |
| :--------: | :-------: | :---------: |
|    Task    |   Fcfs    | Iofunctions |
| ReadyQueue |    Sjf    |
|     -      |    Srt    |
|     -      |    Rr     |
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
