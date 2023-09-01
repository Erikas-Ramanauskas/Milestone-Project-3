let itemData;

// takes jason data
fetch("/static/json/item_data.json")
    .then((response) => response.json())
    .then((json) => {
        itemData = json;
    });

// filter form  modifications

const filterForm = document.getElementById(`filter-form`);

const classPreference = filterForm.getElementById("class-preference");
const itemPreference = filterForm.getElementById("item-preference");

classPreference.addEventListener("change", renderNewAffixes);
itemPreference.addEventListener("change", renderNewAffixes);

function renderNewAffixes() {
    const classValue = filterForm.getElementById("class-preference").value.toLowerCase().replace(" ", "_");
    const itemValue = filterForm.getElementById("item-preference").value.toLowerCase().replace(" ", "_");

    newItemData = itemData[itemValue];

    let newChoiceAffixes;

    // determines if user selected all classes so the individual classes affixes would not be included
    if (lowerChosenClass != "all_classes") {
        newChoiceAffixes = [
            ...newItemData.affixes.all_classes,
            ...newItemData.affixes[classValue],
        ];
    } else {
        newChoiceAffixes = newItemData.affixes.all_classes;
    }
    console.log(newChoiceAffixes);
}
