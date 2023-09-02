let itemData;

// takes jason data
fetch("/static/json/item_data.json")
    .then((response) => response.json())
    .then((json) => {
        itemData = json;
    });

// filter form  modifications

const filterForm = document.getElementById(`filter-form`);

const classPreference = document.getElementById("class-preference");
const itemPreference = document.getElementById("item-preference");

classPreference.addEventListener("change", renderNewAffixes);
itemPreference.addEventListener("change", renderNewAffixes);

function renderNewAffixes() {
    const classValue = document.getElementById("class-preference").value.toLowerCase().replace(" ", "_");
    const itemValue = document.getElementById("item-preference").value.toLowerCase().replace(" ", "_");

    newItemData = itemData[itemValue];

    let newChoiceAffixes;

    // determines if user selected all classes so the individual classes affixes would not be included
    if (classValue != "all_classes") {
        newChoiceAffixes = [
            ...newItemData.affixes.all_classes,
            ...newItemData.affixes[classValue],
        ];
    } else {
        newChoiceAffixes = newItemData.affixes.all_classes;
    }

    rearrangedAffixes = newChoiceAffixes.sort((a, b) => {
        if (a.affix < b.affix) return -1;
        if (a.affix > b.affix) return 1;
        return 0;
    });


    const affixPreference = document.getElementById("affix-preference");

    // Clear any existing options in the select element
    affixPreference.innerHTML = "";

    // Create a default "Choose your option" option
    const defaultOption = document.createElement("option");
    defaultOption.id = "selected-affix-option";
    defaultOption.value = "";
    defaultOption.text = "Choose your option";
    defaultOption.disabled = true;
    defaultOption.selected = true;
    affixPreference.appendChild(defaultOption);

    // Loop through the array and create options
    for (const item of newChoiceAffixes) {

        const option = document.createElement("option");
        option.value = item.affix;
        option.text = item.affix;
        affixPreference.appendChild(option);
    }

    // calling materialise initiation
    const elems = document.getElementById('affix-preference');
    M.FormSelect.init(elems, { isMultiple: true });
}



const affixPreference = document.getElementById('affix-preference');
affixPreference.addEventListener('change', function () {
    selectedAffixOption = document.getElementById('selected-affix-option');
    selectedAffixOption.selected = false;
    const affixOptions = this.selectedOptions;
    if (affixOptions.length > 4) {
        M.toast({ html: `Maximum 4 affixes allowed` });
        affixOptions[affixOptions.length - 1].selected = false;
    }
    const filterSubmitBtn = document.getElementById("filter-submit-btn");
    if (affixOptions.length < 1) {
        filterSubmitBtn.disabled = true;
    } else {
        filterSubmitBtn.disabled = false;
    }
});