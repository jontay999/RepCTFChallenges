import requests
import hmac 
import hashlib
import uuid


address = "https://careless-mistake.ivan-and-keane-hard.work/note"
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
token = "9580b8231e4c87aa669bccf199b44a3abc14499fbf20472b11923ce909266eed"