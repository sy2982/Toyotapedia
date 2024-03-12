// car_details.js

document.addEventListener('DOMContentLoaded', function () {
    // Function to format number with commas
    function numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }

    // Get the price element
    var priceElement = document.getElementById('formattedPrice');

    // Get the unformatted price value
    var unformattedPrice = priceElement.textContent;

    // Format the price with commas
    var formattedPrice = numberWithCommas(unformattedPrice);

    // Update the price element with the formatted value
    priceElement.textContent = formattedPrice;
});
