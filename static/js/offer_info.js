
// THe fallowing sorts out bidding and price set up 
const inputField = document.getElementById('offer-bid');
const submitButton = document.getElementById('bid-submit-btn');
const originalValue = parseInt(inputField.value.replace(/,/g, ""));
let currentValue = originalValue;

function changeValue(value, change) {
    if (change) {
        currentValue += value;
    } else {
        currentValue -= value;
    }

    inputField.classList.add("changed");
    setTimeout(() => {
        inputField.classList.remove("changed");
    }, 700);

    if (currentValue < originalValue) {
        currentValue = originalValue;
    }

    if (submitButton) {
        submitButton.disabled = currentValue <= originalValue;
    }

    inputField.value = currentValue.toLocaleString();
}
