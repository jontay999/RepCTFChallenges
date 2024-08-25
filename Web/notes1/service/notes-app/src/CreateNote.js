import React, { useState } from 'react';

const CreateNote = ({ onAddNote }) => {
    const [note, setNote] = useState('');

    const handleAddNote = () => {
        if (note) {
            onAddNote(note);
            setNote('');
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h2>Create a Note</h2>
            <input
                type="text"
                placeholder="Enter your note"
                value={note}
                onChange={(e) => setNote(e.target.value)}
            />
            <button onClick={handleAddNote}>Add Note</button>
        </div>
    );
}

export default CreateNote;