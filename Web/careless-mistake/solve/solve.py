import requests
import hmac 
import hashlib
import uuid


address = "http://127.0.0.1:3000/note"
secret = f"secret-key-{uuid.uuid4}"[:32]
note_id = 0
token = hmac.new(
    secret.encode(),
    str(note_id).encode(),
    hashlib.sha256
).hexdigest()


params = {
    'id': '0',
    'token': token
}

r = requests.get(address, params)
print(r.text)