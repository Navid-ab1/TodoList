from flask import Flask,jsonify,request
from TodoList import TodoList

app=Flask(__name__)
my_list=TodoList()
@app.route("/tasks/")
def show_tasksJson():
    tasks_Json=[task.to_dict() for task in my_list.tasks]
    return jsonify(tasks_Json)


@app.route("/tasks/<int:task_id>")
def specific_task(task_id):
   
    task =my_list.find_task(task_id)
    if(task):
        return task.to_dict()       
    else:
        return jsonify({"error":"Task not found "}),404


@app.route("/tasks",methods=['POST'])
def create_task():
    request_data=request.get_json()
    if not request_data or 'title' not in request_data:
        return jsonify({"error":"Missing title"}),400
    new_title=request_data['title']
    my_list.AddTask(new_title)
    my_list.save_tasks_to_file()
    return jsonify({"message":"Task created successfully"}),201



@app.route("/tasks/<int:task_id>",methods=['PUT'])
def update_task(task_id):
    task_to_update =my_list.find_task(task_id)
    if not task_to_update:
        return jsonify({"error":"Task not found "}),404
    
    request_data=request.get_json()
    task_to_update.title=request_data.get('title',task_to_update.title)
    task_to_update.is_completed=request_data.get('is_completed',task_to_update.is_completed)
    task_to_update.is_pinned=request_data.get('is_pinned',task_to_update.is_pinned)

    my_list.save_tasks_to_file()
    return jsonify(task_to_update.to_dict())


@app.route("/tasks/<int:task_id>",methods=["DELETE"])
def delete_task(task_id):
    task_to_delete=my_list.find_task(task_id)
    if not task_to_delete:
        return jsonify({"error":"Task not found"}),404
    
    my_list.tasks.remove(task_to_delete)
    my_list.save_tasks_to_file()
    return jsonify({"message": "Task deleted successfully"})


if __name__=="__main__":
    app.run(debug=True)
