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

    console.log(rearrangedAffixes);

    const affixPreference = document.getElementById("affix-preference");

    // Clear any existing options in the select element
    affixPreference.innerHTML = "";

    // Create a default "Choose your option" option
    const defaultOption = document.createElement("option");
    defaultOption.value = "";
    defaultOption.text = "Choose your option";
    defaultOption.disabled = true;
    defaultOption.selected = true;
    affixPreference.appendChild(defaultOption);

    // Loop through the array and create options
    for (const item of newChoiceAffixes) {

        console.log(item);
        const option = document.createElement("option");
        option.value = item.affix;
        option.text = item.affix;
        affixPreference.appendChild(option);
    }

    // calling materialise initiation
    const elems = document.getElementById('affix-preference');
    M.FormSelect.init(elems, { isMultiple: true });
}
