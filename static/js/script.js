// materialise enablers
$(document).ready(function () {
    // mobile side nav activation
    $('.sidenav').sidenav();
    //Navigation Dropdown activation
    $(".dropdown-trigger").dropdown();
    // form check
    $('input#input_text, textarea#textarea2').characterCounter();
});


const offerClassButtons = document.querySelectorAll('.offer-class-button');
const offerItemButtons = document.querySelectorAll('.offer-item-button');

// Setting default choices and adjusting them later if player has preferences
let chosenClass = "All Classes";
let chosenItem = "Amulet";

// Example array of button texts
const myButtonData = ['Button 1', 'Button 2', 'Button 3'];

function startListeners(buttons) {
    buttons.forEach(button => {
        button.addEventListener('click', createButtonsFromArray);
        button.addEventListener('click', () => {
            buttons.forEach(btn => {
                btn.classList.remove('active');
            });
            button.classList.add('active');
            if (button.classList.contains('offer-class-button')) {
                chosenClass = button.dataset.class;
            } else if (button.classList.contains('offer-item-button')) {
                chosenItem = button.dataset.item;
            }
        });

    });
}

startListeners(offerClassButtons);
startListeners(offerItemButtons);



function createButtonsFromArray() {
    console.log("test");
    const container = document.getElementById('suffixes');

    console.log(container);

    // Loop through the array and create buttons
    myButtonData.forEach((buttonText) => {
        const button = document.createElement('button');
        button.classList.add('grey', 'darken-3');
        button.innerText = buttonText;
        container.appendChild(button);
        console.log(button);
    });
}

