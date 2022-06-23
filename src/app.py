from flask import Flask, jsonify, request
import json


app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    todo = jsonify(todos)
    return todo


@app.route('/todos', methods=['POST'])
def add_new_todo():

    request_body =  json.loads(request.data)
    todos.append(request_body)
    todo_json = jsonify(todos)

    return todo_json


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

    def delete(todo):

        if todos.index(todo) != position:
            return todos[todos.index(todo)]

    newTodos = list(filter(delete, todos))
    newTodos = jsonify(newTodos)
    
    print(newTodos)

    return newTodos




# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)