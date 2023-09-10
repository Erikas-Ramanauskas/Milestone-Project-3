// Setting default choices and adjusting them later if player has preferences
let chosenClass = document.querySelector(".offer-class-button.active").dataset
    .class;
let chosenItem;

let itemData;

// takes jason data
fetch("/static/json/item_data.json")
    .then((response) => response.json())
    .then((json) => {
        itemData = json;
    });

const offerClassButtons = document.querySelectorAll(".offer-class-button");
const offerItemButtons = document.querySelectorAll(".offer-item-button");
const suffixesDiv = document.getElementById("suffixes");

window.addEventListener("load", function () {
    startListeners(offerClassButtons);
    startListeners(offerItemButtons);
    staticFormHTML();
});

function startListeners(buttons) {
    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            buttons.forEach((btn) => {
                btn.classList.remove("active");
            });
            button.classList.add("active");
            if (button.classList.contains("offer-class-button")) {
                chosenClass = button.dataset.class;
                staticFormHTML();
            } else if (button.classList.contains("offer-item-button")) {
                chosenItem = button.dataset.item;
                staticFormHTML();
                addSuffixHTML();
            } else if (button.classList.contains("suffix-button")) {
                addSuffixHTML();
            }
        });
        if (!button.classList.contains("suffix-button")) {
            button.addEventListener("click", createButtonsFromArray);

        }
    });
}



function createButtonsFromArray() {
    const affixes = document.getElementById("affixes");

    const lowerChosenItem = chosenItem.toLowerCase().replace(" ", "_");
    const lowerChosenClass = chosenClass.toLowerCase().replace(" ", "_");

    const newItemData = itemData[lowerChosenItem];

    creatSuffixesButtons(newItemData);

    let newButtonAffixes;

    // determines if user selected all classes so the individual classes affixes would not be included
    if (lowerChosenClass != "all_classes") {
        newButtonAffixes = [
            ...newItemData.affixes.all_classes,
            ...newItemData.affixes[lowerChosenClass],
        ];
    } else {
        newButtonAffixes = newItemData.affixes.all_classes;
    }

    let currentButtons = affixes.querySelectorAll(".affix-button");

    // Remove buttons that do not match
    currentButtons.forEach((button) => {
        const buttonAffix = button.dataset.affix;
        const buttonMinimum = button.dataset.minimum;
        const buttonMaximum = button.dataset.maximum;

        const matchingData = newButtonAffixes.find((item) => {
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
    currentButtons = affixes.querySelectorAll(".affix-button");

    // creates and affix data array of current buttons to prevent repeating buttons
    let currentButtonsArray = [];
    currentButtons.forEach((button) => {
        currentButtonsArray.push(button.dataset.affix);
    });

    // Loop through the array and create buttons
    newButtonAffixes.forEach((newButtonData) => {
        // Checks if new butons matches a current buttons and skips the loop if so
        const existingButton = currentButtonsArray.find(
            (affixName) => affixName === newButtonData.affix
        );

        // button creation that holds affix data
        if (!existingButton) {
            const button = document.createElement("button");
            button.classList.add(
                "waves-effect",
                "waves-light",
                "btn",
                "grey",
                "darken-3",
                "affix-button"
            );
            button.innerText = newButtonData.affix;
            button.setAttribute("data-affix", newButtonData.affix);
            button.setAttribute("data-percentage", newButtonData.percentage);
            button.setAttribute("data-minimum", newButtonData.minimum);
            button.setAttribute("data-maximum", newButtonData.maximum);
            button.addEventListener("click", () => {
                toggleActive(button);
            });
            affixes.appendChild(button);
        }
    });

    // call functions
    armorAndDamage(newItemData);
    removeAffixHTML(null, true);
}

// creates suffixes for the item type
function creatSuffixesButtons(itemData) {
    suffixesDiv.innerHTML = "";

    const suffixes = itemData.suffix;
    // Check if the array is empty
    if (suffixes.length === 0) {
        return null;
    }

    // Create a parent div to hold the buttons
    const parentDiv = document.createElement("div");
    parentDiv.classList.add("center-align", "col", "s12");

    // Loop through the array and create a button for each item
    suffixes.forEach((suffix, index) => {
        const button = document.createElement("button");
        button.classList.add(
            "waves-effect",
            "waves-light",
            "btn",
            "grey",
            "darken-3",
            "suffix-button"
        );
        button.setAttribute("data-suffix", suffix);
        if (index == 0) {
            button.classList.add("active");
        }
        button.textContent = suffix;
        parentDiv.appendChild(button);
    });

    suffixesDiv.appendChild(parentDiv);
    const suffixButtons = document.querySelectorAll(".suffix-button");
    startListeners(suffixButtons);
    addSuffixHTML();
}

function toggleActive(button) {
    // Count the active buttons
    const activeButtons = document.querySelectorAll(".affix-button.active");
    const submitButton = document.querySelector('#item-submit');

    // If active buttons exceed the maximum, find the first active button and remove its active class
    if (button.classList.contains("active")) {
        button.classList.remove("active");
        submitButton.disabled = true;
        removeAffixHTML(button, false);
    } else if (activeButtons.length < 4) {
        activeButtons.length < 3 ? M.toast({ html: `Please select ${3 - activeButtons.length} more Affix${activeButtons.length < 2 ? "es" : ""}` }) : "";
        submitButton.disabled = activeButtons.length < 3;
        button.classList.add("active");
        addAffixHTML(button);
    } else {
        submitButton.disabled = false;
        M.toast({ html: 'Maximum 4 affixes allowed' });
        button.classList.add("rejected");
        setTimeout(() => {
            button.classList.remove("rejected");
        }, 700);
    }
}

// Updating static info: class / item 
function staticFormHTML() {
    const playerClass = document.getElementById('class-data');
    const item = document.getElementById('item-data');

    playerClass.value = chosenClass;
    item.value = chosenItem;
}

// creating range element
function armorAndDamage(newItemData) {
    const aAndDDIV = document.getElementsByTagName("form")[0];
    const armorAndDamageInput = document.getElementById("armor-damage");

    // remove previous imput if it exist
    if (armorAndDamageInput != null) {
        aAndDDIV.removeChild(armorAndDamageInput);
    }

    const armor = JSON.parse(newItemData.armor);
    const damage = JSON.parse(newItemData.damage);

    if (armor || damage) {
        const details = {
            type: armor ? "fa-shield" : "fa-hand-fist",
            text: armor ? "Armor" : "Damage",
            id: armor ? "armor" : "damage",
            max: armor ? 1500 : 2500,
        };

        const mainDIV = document.createElement("div");
        mainDIV.id = "armor-damage";

        const topDIV = document.createElement("div");
        topDIV.classList.add("row", "space-between", "col", "s12");

        const elementP = document.createElement("p");
        elementP.classList.add("range-field", "input-field", "col", "s12");

        const elementI = document.createElement("i");
        elementI.classList.add(
            "fa-solid",
            details.type,
            "prefix",
            "teal-text",
            "text-accent-3",
            "col", "s9"
        );

        const span = document.createElement("span");
        span.innerHTML = details.text;

        const input = document.createElement("input");
        input.type = "range";
        input.id = details.id;
        input.name = details.id;
        input.min = "0";
        input.max = details.max;
        input.value = details.max / 2;

        const output = document.createElement("output");
        output.setAttribute("for", details.id);
        output.classList.add("teal-text", "text-accent-3", "col", "s3");
        output.value = details.max / 2;

        input.addEventListener("input", (e) => {
            output.textContent = e.target.value;
        });

        topDIV.appendChild(elementI);
        elementP.appendChild(input);
        topDIV.appendChild(output);
        mainDIV.appendChild(topDIV);
        mainDIV.appendChild(elementP);
        aAndDDIV.prepend(mainDIV);
    }
}

// creating suffix form info.
function addSuffixHTML() {
    const suffixHTML = document.querySelector("#suffix-data");

    //   clearing suffix data
    if (suffixHTML) {
        suffixHTML.innerHTML = "";
    }

    //   creating new data
    const suffix = document.querySelector(".suffix-button.active");

    if (suffix) {
        const midDIV = document.createElement("div");
        midDIV.classList.add("col", "s12");

        const input = document.createElement("input");
        input.classList.add("col", "s12", "teal-text", "text-accent-3", "center-align");
        input.type = "text";
        input.id = "suffix";
        input.name = "suffix";
        input.value = suffix.dataset.suffix;
        input.readOnly = true;

        midDIV.appendChild(input);
        suffixHTML.appendChild(midDIV);
    }
}

// creating Affix form imput
function addAffixHTML(button) {
    const data = {
        affix: button.dataset.affix,
        id: button.dataset.affix.toLowerCase().replaceAll(" ", "-"),
        percentage: button.dataset.percentage === "true" ? true : false,
        min: parseInt(button.dataset.minimum),
        max: parseInt(button.dataset.maximum),
        average: Math.ceil(
            (parseInt(button.dataset.minimum) + parseInt(button.dataset.maximum)) / 2
        ),
    };

    const form = document.getElementsByTagName("form")[0];
    const offerPrice = document.querySelector("#offer-price");

    const topDIV = document.createElement("div");
    topDIV.classList.add("row", "affix-input");
    topDIV.id = data.id + "-parent";

    const midDIV = document.createElement("div");
    midDIV.classList.add("col", "s12", "space-between");

    const affixValue = document.createElement("p");
    affixValue.classList.add("col", "s9", "teal-text", "text-accent-3");
    affixValue.innerText = data.affix;

    const input = document.createElement("input");
    input.classList.add("col", "s12");
    input.type = "range";
    input.id = data.id;
    input.name = data.id;
    input.min = data.min;
    input.max = data.max;
    input.step = data.percentage ? 0.1 : 1;
    input.value = data.average;

    const output = document.createElement("output");
    output.setAttribute("for", data.id);
    output.classList.add(
        "col",
        "s3",
        "teal-text",
        "text-accent-3",
        "right-align"
    );
    output.value = data.average + `${data.percentage ? "%" : ""}`;

    input.addEventListener("input", (e) => {
        output.textContent = e.target.value + `${data.percentage ? "%" : ""}`;
    });

    midDIV.appendChild(affixValue);
    midDIV.appendChild(output);
    topDIV.appendChild(midDIV);
    topDIV.appendChild(input);

    const elementToRemove = document.getElementById(`${data.id}-parent`);
    if (elementToRemove == null) {
        form.insertBefore(topDIV, offerPrice);
    }

}

function removeAffixHTML(button, all) {
    const formElement = document.getElementsByTagName("form")[0];
    if (all) {
        const allAffixInputs = document.querySelectorAll('.affix-input');
        allAffixInputs.forEach((input) => {
            formElement.removeChild(input);
        });
        const allAffixActiveButtons = document.querySelectorAll('.affix-button.active');
        allAffixActiveButtons.forEach((button) => {
            addAffixHTML(button);
        });
        return;
    }

    const affix = button.dataset.affix.toLowerCase().replaceAll(" ", "-");
    const elementToRemove = document.getElementById(`${affix}-parent`);
    if (elementToRemove) {

        formElement.removeChild(elementToRemove);
    }
}
