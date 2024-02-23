interface ToDo {
  id: number;
  task: string;
  completed: boolean;
}

const apiUrl = 'http://localhost:5000/todos';

async function fetchToDos() {
  const response = await fetch(apiUrl);
  const todos: ToDo[] = await response.json();
  const listElement = document.getElementById('todo-list');
  listElement.innerHTML = todos.map(todo => `<div>${todo.task}</div>`).join('');
}

async function addToDo(task: string) {
  const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ task, completed: false })
  });

  if (response.ok) {
      fetchToDos();
  }
}

document.getElementById('todo-form').addEventListener('submit', event => {
  event.preventDefault();
  const inputElement = document.getElementById('todo-input') as HTMLInputElement;
  const task = inputElement.value;
  addToDo(task);
  inputElement.value = '';
});

fetchToDos();
