$(document).ready(function () {

    function save_car(event) {
        event.preventDefault();

        // Validate inputs before saving
        if (!validateInputs()) {
            // Validation failed
            return;
        }

        let dataToSave = {
            "image": $("#image").val(),
            "model": $("#model").val(),
            "year": $("#year").val(),
            "fuel_type": $("#fuel_type").val(),
            "price": $("#price").val(),
            "transmission": $("#transmission").val(),
            "engine": $("#engine").val(),
            "mpg_city": $("#mpg_city").val(),
            "mpg_highway": $("#mpg_highway").val(),
            "features": $("#features").val().split(',').map(item => item.trim()),
            "similar_cars": $("#similar_cars").val().split(',').map(item => item.trim()),
            "description": $("#description").val(),
            "car_type": $("#car_type").val(),
        };

        console.log("Data to save:", dataToSave);

        $.ajax({
            type: "POST",
            url: "/add",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(dataToSave),
            success: function (result) {
                console.log("Server response:", result);

                // Display success message and links
                $("#success-message").show();

                // Construct the URL for viewing the newly added item
                var viewItemUrl = "/view/" + result.new_car_id;

                // Update the "See it here" link with the correct URL
                $("#view-item-link").prop("href", viewItemUrl);

                // Clear input fields
                $(':input').val('');

                // Set focus on the first text box
                $("#image").focus();
            },
            error: function (request, status, error) {
                console.error("Error saving car:", error);
            },
        });
    }

    function validateInputs() {
        // Remove previous error styles
        $('input, textarea').removeClass('error');
    
        // Validate each input field
        let isValid = true;
    
        // Validation function for highlighting the field and setting focus
        function highlightField(selector) {
            $(selector).addClass('error');
            if (isValid) {
                $(selector).focus();
                isValid = false;  // Set isValid to false only once
            }
        }
    
        // Validate Image URL (not blank)
        let image = $("#image").val().trim();
        if (image === "") {
            highlightField("#image");
        }
    
        // Validate Model (not blank)
        let model = $("#model").val().trim();
        if (model === "") {
            highlightField("#model");
        }
    
        // Validate Year (numeric and not blank)
        let year = $("#year").val().trim();
        if (isNaN(year) || year === "") {
            highlightField("#year");
        }
    
        // Validate Fuel Type (not blank)
        let fuelType = $("#fuel_type").val().trim();
        if (fuelType === "") {
            highlightField("#fuel_type");
        }
    
        // Validate Price (numeric and not blank)
        let price = $("#price").val().trim();
        if (isNaN(price) || price === "") {
            highlightField("#price");
        }
    
        // Validate Transmission (not blank)
        let transmission = $("#transmission").val().trim();
        if (transmission === "") {
            highlightField("#transmission");
        }
    
        // Validate Engine (not blank)
        let engine = $("#engine").val().trim();
        if (engine === "") {
            highlightField("#engine");
        }
    
        // Validate MPG City (numeric and not blank)
        let mpgCity = $("#mpg_city").val().trim();
        if (isNaN(mpgCity) || mpgCity === "") {
            highlightField("#mpg_city");
        }
    
        // Validate MPG Highway (numeric and not blank)
        let mpgHighway = $("#mpg_highway").val().trim();
        if (isNaN(mpgHighway) || mpgHighway === "") {
            highlightField("#mpg_highway");
        }
    
        // Validate Features (comma-separated, not blank)
        let features = $("#features").val().trim();
        if (features === "") {
            highlightField("#features");
        }
    
        // Validate Similar Cars (comma-separated, not blank)
        let similarCars = $("#similar_cars").val().trim();
        if (similarCars === "") {
            highlightField("#similar_cars");
        }
    
        // Validate Car Type (not blank)
        let carType = $("#car_type").val().trim();
        if (carType === "") {
            highlightField("#car_type");
        }
    
        // Validate Description (not blank)
        let description = $("#description").val().trim();
        if (description === "") {
            highlightField("#description");
        }
    
        return isValid;
    }    
    
    $("#submit").on("click", save_car);
});