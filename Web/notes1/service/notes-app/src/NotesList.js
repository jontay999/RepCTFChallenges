import React from 'react';

const NotesList = ({ notes }) => {
    return (
        <div style={{ padding: '20px' }}>
            <h2>Your Notes</h2>
            <ul>
                {notes.map((note, index) => (
                    <li key={index}>{note}</li>
                ))}
            </ul>
        </div>
    );
}

export default NotesList;