$(document).ready(function () {
    // Submit event for the search form
    $('#searchForm').submit(function (event) {
        // Prevent the default form submission
        event.preventDefault();

        // Get the search query from the input
        var query = $('.search-input').val().trim();

        // If the query is all whitespace, clear the input and maintain focus
        if (!query) {
            $('.search-input').val('').focus();
        } else {
            // Redirect to the search results page with the query parameter
            window.location.href = '/search?query=' + query;
        }
    });
});