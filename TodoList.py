from Todo import Task
import json
class TodoList:
    def __init__(self,filename='test.json'):
        self.tasks=[]
        self.filename=filename
        self.load_tasks_from_file()

    def AddTask(self,title):
        new_Task=Task
        self.tasks.append(new_Task(title))

    def display_tasks(self):
        for index,item in enumerate(self.tasks):
            print(index+1,item)


    def find_task(self,task_number):
        index = task_number-1
        if  0<=index<len(self.tasks):   return self.tasks[index]
        else:return None


    def complete_task(self,task_number):
        task_completed= self.find_task(task_number)
        if task_completed:
            task_completed.mark_as_completed()
            
        
            
                
    def  save_tasks_to_file(self, filename):
        tasks_json=[]
        for task in self.tasks:
            data={
                "title":task.title,
                "creation_date":str(task.creation_date),
                "is_completed":task.is_completed,
                "is_pinned":task.is_pinned
            }
            tasks_json.append(data)

        with open(filename,'w',encoding='utf-8') as f:
            json.dump(tasks_json,f,indent=4,ensure_ascii=False)
        print("Task Is successfully stored")
                    
    def load_tasks_from_file(self):
        with open(self.filename,'r',encoding='utf-8') as f:
            list_load_to_OBJ = json.load(f)
        print(type(list))
        for lis in list_load_to_OBJ:
            new_task=Task(lis['title'])
            new_task.is_completed=lis['is_completed']
            new_task.is_pinned=lis['is_pinned']
            self.tasks.append(new_task)
        print(f"تسک‌ها با موفقیت از فایل {self.filename} بارگذاری شدند.")