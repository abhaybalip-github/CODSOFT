# python
# class to implement and manage task list
import tkinter as tk;

class TaskList:
    def __init__(self) -> None:
        self.task_count = 0
        self.task_list = []
        self.task_status = []
    def insert_task(self,task: str):
        self.task_list.insert(task)
        self.task_status.insert(1)
        self.task_count += 1
        print('Task Added',end='\n\n')

    def delete_task(self,key: int):
        self.task_list.pop(key)
        self.task_status.pop(key)
        self.task_count -= 1
        print('Task Deleted',end='\n\n')

    def display_task(self):
        if(self.task_count >0):
            print('Index\tTask\tStatus',end='\n')
            for i in range(self.task_count):
                print(i+1,'\t',self.task_list[i],'\t',self.task_status[i],end='\n')
        else:
            print('No Task Avaliable',end='\n\n')

    def store_task_file(self):
        if(self.task_count> 0):
            file = open('TaskList.txt','w+')
            for i in range(self.task_count):
                file.write(f'{self.task_list[i]}\t{self.task_status[i]}')
            file.flush()
            file.close()
        else:
            print('No Task Avaliable',end='\n\n')

# main_window = tk.Tk()