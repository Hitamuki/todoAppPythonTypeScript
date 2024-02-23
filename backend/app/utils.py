# 役割： ヘルパー関数やユーティリティ関数を定義。

# app/utils.py

def create_todo(data, todos):
    """新しい ToDo を作成し、リストに追加する"""
    new_todo = {
        'id': max([todo['id'] for todo in todos], default=0) + 1,
        'task': data['task'],
        'completed': data['completed']
    }
    todos.append(new_todo)
    return new_todo

def update_todo(todo, data):
    """既存の ToDo を更新する"""
    todo['task'] = data.get('task', todo['task'])
    todo['completed'] = data.get('completed', todo['completed'])
    return todo
