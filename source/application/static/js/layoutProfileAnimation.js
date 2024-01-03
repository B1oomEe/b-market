document.addEventListener("DOMContentLoaded", function() {
	const profileIcon = document.getElementById("profile-icon");
	const profileMenu = document.getElementById("profile-menu");

	profileIcon.addEventListener("click", function() {
		if (profileMenu.style.display === "block") {
			profileMenu.style.display = "none";
		} else {
			profileMenu.style.display = "block";
		}
	});


	document.addEventListener("click", function(event) {
		if (event.target !== profileIcon && event.target !== profileMenu) {
			profileMenu.style.display = "none";
		}
	});
});
