from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# ToDoリストを格納する簡単なデータ構造
todos = [
    {"id": 1, "task": "牛乳を買う", "completed": False},
    {"id": 2, "task": "レポートを書く", "completed": False}
]

# Swagger UIの設定
SWAGGER_URL = '/swagger'
API_URL = '/static/openapi.yml'  # openapi.yaml ファイルへのパスを更新
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "ToDoアプリ"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/todos', methods=['GET'])
def get_todos():
    if not todos:
        return jsonify({'error': 'ToDoが見つかりません'}), 404
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = request.json
    new_todo['id'] = max(todo['id'] for todo in todos) + 1  # 新しいIDを割り当て
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'ToDoが見つかりません'}), 404

    todo.update(request.json)
    return jsonify(todo)

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'ToDoが見つかりません'}), 404

    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({'message': 'ToDoが削除されました'}), 200

if __name__ == '__main__':
    app.run(debug=True)
