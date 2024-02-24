import React, { useState } from 'react';
import { TodoList } from '../../Todo/components/TodoList';
import { AddTodo } from '../../Todo/components/children/AddTodo';
import './styles/App.scss';

export const App = () => {
  const [todos, setTodos] = useState([]);  // ToDo項目の状態

  const addTodo = (text: string) => {
    const newTodo = { id: Date.now(), text };
    setTodos([...todos, newTodo]);
  };

  const removeTodo = (id: number) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div>
      <h1>My ToDo App</h1>
      <AddTodo onAddTodo={addTodo} />
      <TodoList todos={todos} onRemoveTodo={removeTodo} />
    </div>
  );
};
