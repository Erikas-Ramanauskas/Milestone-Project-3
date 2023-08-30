// materialise enablers
$(document).ready(function () {
    // mobile side nav activation
    $(".sidenav").sidenav();
    //Navigation Dropdown activation
    $(".dropdown-trigger").dropdown();
    // form check
    $("input#input_text, textarea#textarea2").characterCounter();
    // Tooltip activation
    $('.tooltipped').tooltip(
        {
            enterDelay: 500,
            exitDelay: 100
        }
    );
    // Modal activation
    $('.modal').modal();
});

// Preloader fade out called together with json data load so the procentage change would not be vissable
const loader = document.querySelector(".loader");


// This solves % sing to required affix atributes
let affixPerc;

// takes json data
// also since it takes the most time also works as dom content fuction for the other actions
fetch("/static/json/affix.json")
    .then((response) => response.json())
    .then((json) => {
        affixPerc = json;
        // its important procentage symbols to be added before loader disapears
        addPercentageSymbols();
        // equalising the all cards to tallest.
        setEqualCardHeight();
        loader.classList.add("loader-hidden");
        chatWindowFocus();
    });


// confirms if affix taken is procentage or not
function findPercentageForAffix(targetAffix) {
    const matchingAffix = affixPerc.affixes.find(affix => affix.affix.toLowerCase().replace("-", " ").trim() == targetAffix);

    if (matchingAffix) {
        return matchingAffix.percentage === "true";
    } else {
        return null; // Affix not found
    }
}

// Capture all affix-key/value created by flask, filter all that suposed to be with procentage not static number and add % at the end
function addPercentageSymbols() {

    const affixKeys = document.querySelectorAll(".affix-key");

    affixKeys.forEach(affixKey => {
        const affixNameSpan = affixKey.querySelectorAll("span");
        const checkPerc = findPercentageForAffix(affixNameSpan[0].textContent.toLowerCase().replace(":", "").trim());

        if (checkPerc) {
            affixNameSpan[1].textContent = affixNameSpan[1].textContent + "%";
        }
    });

}


// Message chat window bottom focus
function chatWindowFocus() {
    const chatWindow = document.getElementById("chat-window");
    if (chatWindow) {
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
}

function shareContactID(button) {
    const contactID = button.getAttribute("data-contactID");
    const contactType = button.getAttribute("data-contact-type");

    const targetElement = document.getElementById("contact-id-field"); // Replace "targetElement" with the actual ID of the element
    targetElement.value = contactID;
    targetElement.setAttribute("name", contactType);
}


if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}


// setting all item cards to be same height
function setEqualCardHeight() {
    const cards = document.getElementsByClassName("offer-card");

    let maxHeight = 0;
    for (let i = 0; i < cards.length; i++) {
        const cardHeight = cards[i].clientHeight;
        maxHeight = Math.max(maxHeight, cardHeight);
    }

    for (let i = 0; i < cards.length; i++) {
        cards[i].style.height = `${maxHeight}px`;
    }
}

