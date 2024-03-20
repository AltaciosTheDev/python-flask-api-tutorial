from flask import Flask, jsonify, request #import functions from flask module
app = Flask(__name__) #Initialices app instance of the Flask class


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

#when user GETS todos, returns the jsonified todos list 
@app.route('/todos', methods=['GET'])
def hello_world():
    text = jsonify(todos) #method to convert data to json before sending 
    return text

#when user POST todos
@app.route('/todos', methods=['POST'])
def add_new_todo():
    # flask allows acces to the body and .json converts to python dictionaty 
    request_body = request.json 
    todos.append(request_body)
    return jsonify(todos)

#when user DELETE todo 
#<> anything inside will be an accesible variable sent automatically to the function as an argument when called
#parameter can be called whatever, has not effect on functionality.
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)
    

#Will only start the server if the script is executed directly, when this happens, __name__ == __main__
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)