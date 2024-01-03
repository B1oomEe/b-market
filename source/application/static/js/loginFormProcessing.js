function validateForm() {
	var username = $("#username").val();

	$.ajax({
		type: "POST",
		url: "/validate",
		data: JSON.stringify({ "username": username }),
		contentType: "application/json;charset=UTF-8",
		success: function (response) {
			$("#result").html(response.message);
		},
		error: function (error) {
			console.log(error);
		}
	});
}