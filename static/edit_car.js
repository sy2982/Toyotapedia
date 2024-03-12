document.addEventListener('DOMContentLoaded', function () {
    // Event listener for the Discard Changes button
    var discardBtn = document.getElementById('discardBtn');
    if (discardBtn) {
        discardBtn.addEventListener('click', function (event) {
            // Display a confirmation dialog
            var isSure = confirm('Are you sure you want to discard changes?');

            // Always prevent the form submission
            event.preventDefault();

            // If the user is sure, redirect to the view page
            if (isSure) {
                var carId = discardBtn.getAttribute('data-car-id');
                window.location.href = `/view/${carId}`;
            } else {
                // If the user is not sure, let them stay on the same page
            }
        });
    }
});
