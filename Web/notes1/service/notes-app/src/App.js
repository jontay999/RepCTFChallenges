import React, { useState } from 'react';
import Login from './Login';
import NotesList from './NotesList';
import CreateNote from './CreateNote';

const App = () => {
  const [user, setUser] = useState(null);
  const [notes, setNotes] = useState([]);

  const handleLogin = (username) => {
    setUser(username);
  };

  const handleAddNote = (note) => {
    setNotes([...notes, note]);
  };

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', textAlign: 'center' }}>
      {!user ? (
        <Login onLogin={handleLogin} />
      ) : (
        <div>
          <h1>Welcome, {user}</h1>
          <CreateNote onAddNote={handleAddNote} />
          <NotesList notes={notes} />
        </div>
      )}
    </div>
  );
}

export default App;