from flask import Flask
from TodoList import TodoList

app=Flask(__name__)
my_list=TodoList()
@app.route("/tasks")
def show_tasks():
    html_output="<h1> My Todo-List</h1>"
    html_output+="<ul>"
    for task in my_list.tasks:
        html_output+=f"<li>{task}</li>"
    html_output+="</ul>"
    return html_output



if __name__=="__main__":
    app.run(debug=True)