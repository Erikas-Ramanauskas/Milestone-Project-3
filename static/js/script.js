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
        // its important procentage symbosl to be added before loader disapears
        addPercentageSymbols();
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

// Caapture all affix-key/value created by flask, filter all that suposed to be with procentage not static number and add % at the end
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
    chatWindow.scrollTop = chatWindow.scrollHeight;
}
