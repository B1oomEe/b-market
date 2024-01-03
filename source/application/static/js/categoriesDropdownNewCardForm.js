import categories from '../../utils/datasets/categoryChoiceStructure.json'
import stages from '../../utils/datasets/stageChoiceStructure.json'
import purposes from '../../utils/datasets/purposeChoiceStructure.json'


// Populate category dropdown
const categoryDropdown = document.getElementById("category");
for (const category in categories) {
	const optGroup = document.createElement("optgroup");
	optGroup.label = category;
	categories[category].forEach(subcategory => {
		const option = document.createElement("option");
		option.value = subcategory;
		option.textContent = subcategory;
		optGroup.appendChild(option);
	});
	categoryDropdown.appendChild(optGroup);
}

// Populate stage dropdown
const stageDropdown = document.getElementById("stage");
stages.forEach(stage => {
	const option = document.createElement("option");
	option.value = stage;
	option.textContent = stage;
	stageDropdown.appendChild(option);
});

// Populate purpose dropdown
const purposeDropdown = document.getElementById("purpose");
purposes.forEach(purpose => {
	const option = document.createElement("option");
	option.value = purpose;
	option.textContent = purpose;
	purposeDropdown.appendChild(option);
});