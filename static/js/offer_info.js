
// The fallowing sorts out bidding and price set up 
const inputField = document.getElementById('offer-bid');
const submitButton = document.getElementById('bid-submit-btn');
if (inputField) {
    // this is a first time in my programing were "var" was usefull :)
    // I had thsi variable in the main scope but it coused a bug in some cases so if statment was needed
    var originalValue = parseInt(inputField.value.replace(/,/g, ""));
}
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


// bids accept button modification
const bidTable = document.getElementById('offer-bid-table');
let bidRow;

if (bidTable) {
    bidRow = bidTable.getElementsByClassName('offer-bid-row');

    for (let i = 0; i < bidRow.length; i++) {
        const row = bidRow[i];
        const bidButton = row.getElementsByClassName('bid-accept-button')[0];

        row.addEventListener('mouseenter', () => {
            bidButton.classList.remove('accept-hidden');
        });

        row.addEventListener('mouseleave', () => {
            bidButton.classList.add('accept-hidden');
        });
    }
}



// function adjust invisible form that trigers offer acceptence by owner of offer
function renderBidAcceptForm(button) {

    // Get the data attributes
    const user = button.getAttribute('data-user');
    const bid = button.getAttribute('data-bid');
    const trade = button.getAttribute('data-trade');


    // Get the input elements
    const userInput = document.getElementById('trade-user');
    const priceInput = document.getElementById('trade-price');
    const accepted = document.getElementById('trade-accepted');
    const tradeByOwner = document.getElementById('trade-by-owner');
    const tradeByBidder = document.getElementById('trade-by-bidder');


    let offerDetails;

    if (trade == "sale") {
        offerDetails = document.getElementById('offer-details');
        offerDetails.innerHTML = `<p class="bid-info"><a class="orange-color-text" href="/profile/${user}">${user}</a> offered <span class="orange-color-text">${bid}</span></p>`;

        // Set the values of the input elements
        userInput.value = user;
        priceInput.value = bid;
        accepted.value = "true";
    } else if (trade == "t-owner") {
        offerDetails = document.getElementById('trade-details');
        offerDetails.innerHTML = `<p class="bid-info">Traded with <a class="orange-color-text" href="/profile/${user}">${user}</a></p>`;
        tradeByOwner.value = "true";
    } else if (trade == "t-bidder") {
        offerDetails = document.getElementById('trade-details');
        const owner = button.getAttribute('data-owner');
        offerDetails.innerHTML = `<p class="bid-info">Traded with <a class="orange-color-text" href="/profile/${owner}">${owner}</a></p>`;
        tradeByBidder.value = "true";
    } else {
        return console.error("Neither of trades is found");
    }
}