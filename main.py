from TodoList import TodoList


newTask = TodoList()
newTask.AddTask("Washing the dishes")
newTask.AddTask("Going to the English class")
newTask.display_tasks()
newTask.complete_task(1)
newTask.display_tasks()