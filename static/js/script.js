// materialise enablers
$(document).ready(function () {
    // mobile side nav activation
    $('.sidenav').sidenav();
    //Navigation Dropdown activation
    $(".dropdown-trigger").dropdown();
    // form check
    $('input#input_text, textarea#textarea2').characterCounter();
});

// Setting default choices and adjusting them later if player has preferences
let chosenClass = document.querySelector('.offer-class-button.active').dataset.class;
let chosenItem = "Amulet"; // I will leave amulet as permemnet default choice. 

let itemData;

// takes jason data
fetch('/static/json/item_data.json')
    .then((response) => response.json())
    .then((json) => {
        itemData = json;
    });

const offerClassButtons = document.querySelectorAll('.offer-class-button');
const offerItemButtons = document.querySelectorAll('.offer-item-button');
const suffixesDiv = document.getElementById('suffixes');

function startListeners(buttons) {
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            buttons.forEach(btn => {
                btn.classList.remove('active');
            });
            button.classList.add('active');
            if (button.classList.contains('offer-class-button')) {
                chosenClass = button.dataset.class;
            } else if (button.classList.contains('offer-item-button')) {
                chosenItem = button.dataset.item;
            } else if (button.classList.contains('suffix-button')) {
                createSuffixInfo();
            }
        });
        if (!button.classList.contains('suffix-button')) {
            button.addEventListener('click', createButtonsFromArray);
        }

    });
}


startListeners(offerClassButtons);
startListeners(offerItemButtons);

function createButtonsFromArray() {
    const affixes = document.getElementById('affixes');

    lowerChosenItem = chosenItem.toLowerCase().replace(" ", "_");
    lowerChosenClass = chosenClass.toLowerCase().replace(" ", "_");

    newItemData = itemData[lowerChosenItem];

    creatSuffixesButtons(newItemData);

    let newButtonAffixes;

    // determines if user selected all classes so the individual classes affixes would not be included
    if (lowerChosenClass != "all_classes") {
        newButtonAffixes = [...newItemData.affixes.all_classes, ...newItemData.affixes[lowerChosenClass]];
    } else {
        newButtonAffixes = newItemData.affixes.all_classes;
    }


    let currentButtons = affixes.querySelectorAll('.affix-button');

    // Remove buttons that do not match
    currentButtons.forEach(button => {
        const buttonAffix = button.dataset.affix;
        const buttonMinimum = button.dataset.minimum;
        const buttonMaximum = button.dataset.maximum;

        const matchingData = newButtonAffixes.find(item => {
            const affixMatch = item.affix === buttonAffix;
            const minimumMatch = item.minimum == buttonMinimum;
            const maximumMatch = item.maximum == buttonMaximum;

            return affixMatch && minimumMatch && maximumMatch;
        });

        if (!matchingData) {
            affixes.removeChild(button);
        }
    });

    // recaptures all buttons again so the ones that dont matched is removed
    currentButtons = affixes.querySelectorAll('.affix-button');

    // creates and affix data array of current buttons to prevent repeating buttons
    let currentButtonsArray = [];
    currentButtons.forEach((button) => {
        currentButtonsArray.push(button.dataset.affix);
    });

    // Loop through the array and create buttons
    newButtonAffixes.forEach(newButtonData => {
        // Checks if new butons matches a current buttons and skips the loop if so
        const existingButton = currentButtonsArray.find(affixName => affixName === newButtonData.affix);

        // button creation that holds affix data
        if (!existingButton) {
            const button = document.createElement('button');
            button.classList.add('waves-effect', 'waves-light', 'btn', 'grey', 'darken-3', 'affix-button');
            button.innerText = newButtonData.affix;
            button.setAttribute("data-affix", newButtonData.affix);
            button.setAttribute("data-procentage", newButtonData.procentage);
            button.setAttribute("data-minimum", newButtonData.minimum);
            button.setAttribute("data-maximum", newButtonData.maximum);
            button.addEventListener('click', () => {
                toggleActive(button);
            });
            affixes.appendChild(button);
        }
    });

    // call functions 
    armorAndDamage(newItemData);
}

// creates suffixes for the item type
function creatSuffixesButtons(itemData) {

    suffixesDiv.innerHTML = '';

    const suffixes = itemData.suffix;
    // Check if the array is empty
    if (suffixes.length === 0) {
        return null;
    }

    // Create a parent div to hold the buttons
    const parentDiv = document.createElement('div');
    parentDiv.classList.add('center-align', 'col', 's12');


    // Loop through the array and create a button for each item
    suffixes.forEach((suffix, index) => {
        const button = document.createElement('button');
        button.classList.add('waves-effect', 'waves-light', 'btn', 'grey', 'darken-3', 'suffix-button');
        if (index == 0) {
            button.classList.add('active');
        }
        button.textContent = suffix;
        parentDiv.appendChild(button);
    });

    suffixesDiv.appendChild(parentDiv);
    const suffixButtons = document.querySelectorAll('.suffix-button');
    startListeners(suffixButtons);
}

function createSuffixInfo() {
    return null;
}

function toggleActive(button) {
    // Count the active buttons
    const activeButtons = document.querySelectorAll('.affix-button.active');

    console.log(activeButtons.length);
    // If active buttons exceed the maximum, find the first active button and remove its active class
    if (activeButtons.length < 4) {
        button.classList.toggle('active');
    } else if (button.classList.contains('active')) {

        button.classList.remove('active');
    } else {
        button.classList.add('rejected');
        setTimeout(() => {
            button.classList.remove('rejected');
        }, 700);
    }

}


// creating range element
function armorAndDamage(newItemData) {
    const aAndDDIV = document.getElementsByTagName('form')[0];
    const armorAndDamageInput = document.getElementById('armor-damage');

    // remove previous imput if it exist
    if (armorAndDamageInput != null) {
        aAndDDIV.removeChild(armorAndDamageInput);
    }

    const armor = JSON.parse(newItemData.armor);
    const damage = JSON.parse(newItemData.damage);

    if (armor || damage) {
        const details = {
            "type": armor ? "fa-shield" : "fa-hand-fist",
            "id": armor ? "test5" : "test5",
            "max": armor ? "1500" : "2500",
        };

        const elementP = document.createElement('p');
        elementP.classList.add('range-field', 'input-field');
        elementP.id = "armor-damage";

        const elementI = document.createElement('i');
        elementI.classList.add('fa-solid', details.type, 'prefix', 'light-blue-text', 'text-darken-4');

        const input = document.createElement('input');
        input.type = "range";
        input.id = details.id;
        input.min = "0";
        input.max = armor.max;

        elementP.appendChild(elementI);
        elementP.appendChild(input);
        aAndDDIV.prepend(elementP);
    }
}

function addSuffixHTML() {

}

function removeSuffixHTML() {

}



