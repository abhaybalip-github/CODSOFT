# python
# ToDo List
import tkinter;

# Data structure
task_count = 0
task_list = []
task_status = []

def insert_task(task: str):
    task_list.insert(task)
    task_status.insert(1)
    task_count += 1
    print('Task Added',end='\n\n')

def delete_task(key: int):
    task_list.pop(key)
    task_status.pop(key)
    task_count -= 1
    print('Task Deleted',end='\n\n')

def display_task():
    if(task_count >0):
        print('Index\tTask\tStatus',end='\n')
        for i in range(task_count):
            print(i+1,'\t',task_list[i],'\t',task_status[i],end='\n')
    else:
        print('No Task Avaliable',end='\n\n')

def store_task_file():
    if(task_count> 0):
        file = open('TaskList.txt','w+')
        for i in range(task_count):
            file.write(f'{task_list[i]}\t{task_status[i]}')
        file.flush()
        file.close()
    else:
        print('No Task Avaliable',end='\n\n')