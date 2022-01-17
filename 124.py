from flask import Flask,jsonify,request
# app is an object and flask is a class
app = Flask(__name__)

# Creating a array of tasks
tasks = [
    {
        'id': 1,
        'title': 'rahul',
        'description': 4085521132 
    },
    {
        'id': 2,
        'title': 'mikal',
        'description': 3412589635
    }
]

# Decorator
@app.route("/")
def hello_World():
    return "Numbers"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 
   
if(__name__ == "__main__"):
    app.run(debug=True)