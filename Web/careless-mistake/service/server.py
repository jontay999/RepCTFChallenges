from flask import Flask, request, redirect, url_for, render_template_string, render_template
import hmac
import hashlib
import os
import uuid

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_KEY')

class Database:
    def __init__(self):
        self.notes = []
        # My secret doesnt have to be too long, just 30 random bytes...
        self.secret = f"secret-{uuid.uuid4}"[:30]

    def create_note(self, data):
        note_id = len(self.notes)
        self.notes.append(data)
        return {
            'id': note_id,
            'token': self.generate_token(note_id)
        }

    def get_note(self, note_id, token):
        if token != self.generate_token(note_id):
            return {'error': 'invalid token'}
        if note_id >= len(self.notes):
            return {'error': 'note not found'}
        return {'data': self.notes[note_id]}

    
    def generate_token(self, note_id):
        return hmac.new(
            self.secret.encode(),
            str(note_id).encode(),
            hashlib.sha256
        ).hexdigest()

db = Database()
db.create_note(data=os.environ.get('FLAG', 'REP{fake_flag}'))

@app.route('/create', methods=['POST'])
def create():
    data = request.form.get('data')
    result = db.create_note(data=data)
    return redirect(url_for('note', id=result['id'], token=result['token']))

@app.route('/note')
def note():
    try:
        note_id = int(request.args.get('id'))
        token = request.args.get('token')
        note = db.get_note(note_id=note_id, token=token)
        if 'error' in note:
            return note['error']
        else:
            return render_template('view_note.html', note_content = note["data"])
    except: 
        return "`note_id` must be an integer and `token` must be provided"


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run( port = 3000)