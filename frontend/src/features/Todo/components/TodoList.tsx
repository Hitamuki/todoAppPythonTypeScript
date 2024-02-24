import React from 'react';
import { TodoItem } from './children/TodoItem';

export const TodoList = ({ todos, onRemoveTodo }) => {
  return (
    <ul>
      {todos.map(todo => (
        <TodoItem key={todo.id} todo={todo} onRemove={onRemoveTodo} />
      ))}
    </ul>
  );
};
