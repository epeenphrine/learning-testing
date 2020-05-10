import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Test from './components/Test'

function App() {
  const [todos, setTodos] = useState([
    {
      text: 'learn about React',
      isCompleeted: false
    },
    {
      text: 'meet friend for lunch',
      isCompleeted: false
    },
    {
      text: 'build really cool todo app',
      isCompleeted: false
    },
  ])
  return (
    <div className="App">
      <div className='testing'>
        {todos.map((todo, index) => (
          <Test key={index} index={index} todo={todo} />
        ))}
      </div>
    </div>
  );
}

export default App;
