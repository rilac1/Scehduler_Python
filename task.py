from dataclasses import dataclass

@dataclass
class Task:
    tsk_id : str = ''       # task id
    ariv_t : int = 0        # arrive time
    rema_t : int = 0        # remain time
    serv_t : int = 0        # service time
    time_q : int = 0        # time quantum
    ticket : int = 0        # ticket
