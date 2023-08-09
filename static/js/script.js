// materialise enablers
$(document).ready(function () {
    // mobile side nav activation
    $('.sidenav').sidenav();
    //Navigation Dropdown activation
    $(".dropdown-trigger").dropdown();
    // form check
    $('input#input_text, textarea#textarea2').characterCounter();
});


fetch('/static/json/item_data.json')
    .then((response) => response.json())
    .then((json) => console.log(json));





const offerClassButtons = document.querySelectorAll('.offer-class-button');
const offerItemButtons = document.querySelectorAll('.offer-item-button');

// Setting default choices and adjusting them later if player has preferences
let chosenClass = "All Classes";
let chosenItem = "Amulet";

// Example array of button texts
const newButtonData = ['Button 1', 'Button 2', 'Button 3'];

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

    const suffixes = document.getElementById('suffixes');
    const currentButtons = suffixes.querySelectorAll('button');
    console.log(currentButtons);

    // // Remove buttons that do not match
    // currentButtons.forEach(button => {
    //     const buttonText = button.innerText;
    //     if (!newButtonData.includes(buttonText)) {
    //         suffixes.removeChild(button);
    //     }
    // });

    // Loop through the array and create buttons
    newButtonData.forEach(buttonText => {
        // Check if button with same text already exists
        const existingButton = Array.from(currentButtons).find(button => button.innerText === buttonText);
        console.log(existingButton);
        if (!existingButton) {
            const button = document.createElement('button');
            button.classList.add('waves-effect', 'waves-light', 'btn', 'grey', 'darken-3');
            button.innerText = buttonText;
            suffixes.appendChild(button);
        }
    });
}