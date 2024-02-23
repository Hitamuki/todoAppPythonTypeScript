# 役割：すべてのルート（エンドポイント）を定義。

from flask import Blueprint, jsonify, request
from .models import todos
from .utils import create_todo, update_todo

main = Blueprint("main", __name__)


@main.route("/todos", methods=["GET"])
def get_todos():
    if not todos:
        return jsonify({"error": "ToDoが見つかりません"}), 404
    return jsonify(todos), 200


@main.route("/todos", methods=["POST"])
def add_todo():
    if not request.is_json:
        return jsonify({"error": "リクエストはJSONでなければなりません"}), 400

    data = request.get_json()
    if "task" not in data or "completed" not in data:
        return jsonify({"error": "タスクと完了状態は必須です"}), 400

    new_todo = create_todo(data, todos)
    return jsonify(new_todo), 201


@main.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "ToDoが見つかりません"}), 404

    data = request.get_json()
    updated_todo = update_todo(todo, data)
    return jsonify(updated_todo), 200


@main.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'ToDoが見つかりません'}), 404

    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({'message': 'ToDoが削除されました'}), 200