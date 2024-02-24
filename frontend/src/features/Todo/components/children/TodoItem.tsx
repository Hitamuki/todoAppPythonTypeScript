import React from 'react';

export const TodoItem = ({ todo, onRemove }) => {
  return (
    <li>
      {todo.text}
      <button onClick={() => onRemove(todo.id)}>Delete</button>
    </li>
  );
};
