const question_keys = ["math", "chemical_eng", "eee"]
const num_qns = question_keys.length
const open_ended = "materials_eng"

const submit_form = () => {
    const answers = {}
    for (let qn_key of question_keys) {
        answers[qn_key] = document.querySelector(`input[name="${qn_key}"]:checked`)?.value;
    }
    answers[open_ended] = document.querySelector('textarea').value
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(answers)
    })
        .then(response => {
            if (response.redirected) {
                alert("Answers submitted! I'll get an admin to check those answers soon...")
                window.location.href = response.url;
            }
        })
        .catch(error => console.error('Error:', error));
}


document.addEventListener('DOMContentLoaded', () => {
    document.getElementById("form").addEventListener('submit', async (e) => {
        e.preventDefault();
        submit_form();
    })
});