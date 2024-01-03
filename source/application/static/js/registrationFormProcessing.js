$(document).ready(function () {
	$('#myForm').submit(function (e) {
		e.preventDefault(); // Prevent form submission by default

		// Get form data
		var formData = new FormData(this);

		// Send data to server using AJAX
		$.ajax({
			type: 'POST',
			url: '/submit',
			data: formData,
			processData: false,
			contentType: false,
			success: function (data) {
				// Process response from server
				$('#result').html(data.message);
			},
			error: function (error) {
				console.error('Ошибка:', error);
			}
		});
	});
});