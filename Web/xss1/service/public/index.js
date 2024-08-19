(function () {
    function emc(settings) {
        let quizItems = document.querySelectorAll('[data-quiz-item]');
        let choices = document.querySelectorAll('[data-choices]');
        let itemCount = quizItems.length;
        let chosen = [];

        emcInit();

        function emcInit() {
            quizItems.forEach(function (item, index) {
                console.log(item, index)
                let choiceEl = item.querySelector('.choices');
                let choicesData = choiceEl.dataset.choices.split(',');
                choicesData.forEach(function (choice, i) {
                    let option = document.createElement('input');
                    option.name = index;
                    option.id = index + '_' + i;
                    option.type = 'radio';

                    let label = document.createElement('label');
                    label.htmlFor = index + '_' + i;
                    label.textContent = choice;

                    choiceEl.appendChild(option);
                    choiceEl.appendChild(label);

                    option.addEventListener('change', getChosen);
                });
            });
        }

        function getChosen() {
            chosen = [];
            choices.forEach(function (choiceGroup) {
                let inputs = choiceGroup.querySelectorAll('input[type="radio"]');
                inputs.forEach(function (input, index) {
                    if (input.checked) {
                        chosen.push(index + 1);
                    }
                });
            });

        }
        function scoreNormal() {
            let wrong = [];
            let scoreEl = document.getElementById('emc-score');
            quizItems.forEach(function (item, index) {
                if (chosen[index] != settings.key[index]) {
                    wrong.push(index);
                }
            });

            quizItems.forEach(function (item, index) {
                if (wrong.includes(index)) {
                    item.classList.remove('item-correct');
                    item.classList.add('item-incorrect');
                } else {
                    item.classList.remove('item-incorrect');
                    item.classList.add('item-correct');
                }
            });

            let score = ((itemCount - wrong.length) / itemCount).toFixed(2) * 100 + "%";
            scoreEl.textContent = "You scored a " + score;
            scoreEl.classList.add('new-score');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    }

    // Initialize the quiz
    document.addEventListener('DOMContentLoaded', function () {
        emc({
            key: ["2", "1", "2", "2", "2", "2", "1", "1"]
        });
    });
})();
