const submit_form = () => {
    const answers = {}
    for (let i = 0; i < 3; i++) {
        answers[i] = document.querySelector(`input[name="${i}"]:checked`)?.value;
    }
    answers[3] = document.querySelector('textarea').value
    const query_string = new URLSearchParams(answers).toString();
    console.log(query_string)
    alert(query_string)

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(answers)
    })
        .then(response => response.json())
        .then(data => console.log('Success:', data))
        .catch(error => console.error('Error:', error));
}


document.addEventListener('DOMContentLoaded', () => {
    document.getElementById("emc-submit").addEventListener('click', submit_form)
});