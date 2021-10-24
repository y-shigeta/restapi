from flask import Flask, request, json, jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

tasks = {
    '1': 'Buy something',
    '2': 'Watch Netflix'
}

@app.route('/tasks', methods=['GET'])
def list_all_tasks():
    json = {
        'message': tasks
    }
    return jsonify(json)

@app.route('/tasks/<int:taskid>', methods=['GET'])
def show_task(taskid):
    taskid = str(taskid)
    json = {
        'message': tasks[taskid]
    }
    return jsonify(json)

@app.route('/tasks/<int:taskid>', methods=['DELETE'])
def delete_task(taskid):
    taskid = str(taskid)
    if taskid in tasks:
        del tasks[taskid]
        msg = 'Task {} deleted'.format(taskid)
    else:
        msg = '{0} is not in tasks.'.format(taskid)
    json = {
        'message': msg
    }
    return jsonify(json)

@app.route('/tasks', methods=['POST'])
def create_task():
    taskid = str(int(max(tasks.keys())) + 1)
    posted = request.get_json()
    if 'task' in posted:
        tasks[taskid] = posted['task']
        msg = 'New task created'
    else:
        msg = 'No task created'
    json = {
        'message': msg
    }
    return jsonify(json)

@app.route('/tasks/<int:taskid>', methods=['PUT'])
def update_task(taskid):
    taskid = str(taskid)
    posted = request.get_json()
    if 'task' in posted and taskid in tasks:
        tasks[taskid] = posted['task']
        msg = 'Task {} updated'.format(taskid)
    else:
        msg = 'No task updated'
    json = {
        'message': msg
    }
    return jsonify(json)