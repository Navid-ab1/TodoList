from Todo import Task
class TodoList:
    def __init__(self):
        self.tasks=[]

    def AddTask(self,title):
        new_Task=Task
        self.tasks.append(new_Task(title))

    def display_tasks(self):
        for index,item in enumerate(self.tasks):
            print(index+1,item)
    
    def exist_task(self,task_number):
        exist =False
        index = task_number-1
        if  0<=index<len(self.tasks):
            exist=True
            return(exist,index)
        else:return exist

    def find_task(self,task_number):
        local_status,index = self.exist_task(task_number)
        if local_status :
            return(self.tasks[index])
        else:return None
    def complete_task(self,task_number):
        task_completed= self.find_task(task_number)
        if task_completed:
            task_completed.mark_as_completed()
            
        
            
                

