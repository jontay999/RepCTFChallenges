const SERVER_URL = "http://127.0.0.1:3000"
function fancy_schmancy_effect() {
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let interval = null;
    document.querySelector("h1").onmouseover = event => {
        let iteration = 0;
        clearInterval(interval);
        interval = setInterval(() => {
            event.target.innerText = event.target.innerText
                .split("")
                .map((letter, index) => {
                    if (index < iteration) {
                        return event.target.dataset.value[index];
                    }

                    return letters[Math.floor(Math.random() * 26)]
                })
                .join("");

            if (iteration >= event.target.dataset.value.length) {
                clearInterval(interval);
            }

            iteration += 1 / 3;
        }, 30);
    }
}


const toggle_show_password = (toggler, elements) => {
    toggler.addEventListener('change', e => {
        elements.forEach(element => {
            element.setAttribute('type', e.target.checked ? 'text' : 'password');
        });
    });
};

document.addEventListener('DOMContentLoaded', () => {
    fancy_schmancy_effect()
    toggle_show_password(form.showPassword, [form.password]);
    document.getElementById("form").addEventListener('submit', async (e) => {
        e.preventDefault()
        const { username, password } = e.target
        const data = JSON.stringify({
            username: username.value,
            password: password.value
        })
        const response = await fetch(SERVER_URL + "/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: data
        })
        const response_text = await response.text()
        alert(response_text)
    })

});