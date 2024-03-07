/*document.addEventListener("DOMContentLoaded", function() {
    var tableRows = document.querySelectorAll("#tableid tbody tr");

    tableRows.forEach(function(row) {
        row.addEventListener("click", function() {
            var vehicleId = this.getAttribute("data-vehicle-id");
            var vehicleCapacity = this.getAttribute("data-vehicle-capacity");
            var vehicleType = this.getAttribute("data-vehicle-type");
            var refrigerated = this.getAttribute("data-refrigerated");

            this.remove();

            alert("You selected:\nVehicle ID: " + vehicleId + "\nCapacity: " + vehicleCapacity + "\nType: " + vehicleType + "\nRefrigerated: " + refrigerated);
            // You can do further processing here, such as submitting the selected vehicle to a form
        });
    });
});*/

/*
document.addEventListener("DOMContentLoaded", function() {
    var chooseButtons = document.querySelectorAll(".book");

    chooseButtons.forEach(function(button,index) {
        button.addEventListener("click", function() {
            var row = this.parentNode.parentNode;
            //var tableBody = row.parentNode;
            this.style.display = 'none';
            

            // Remove the selected vehicle from the table
            row.remove();

            // Display a message to the user
            var vehicleId = row.getAttribute("data-vehicle-id");
            alert("You chose vehicle with ID: " + vehicleId);

            // You may want to perform additional actions here, such as updating the database or UI
        });
    });
});



document.addEventListener("DOMContentLoaded", function() {
    var returnButtons = document.querySelectorAll(".return");

    returnButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var row = this.parentNode.parentNode;
            var tableBody = row.parentNode;

            // Add the returned vehicle back to the table
            tableBody.appendChild(row);

            // Display a message to the user
            var vehicleId = row.getAttribute("data-vehicle-id");
            alert("You returned vehicle with ID: " + vehicleId);

            // You may want to perform additional actions here, such as updating the database or UI
        });
    });
});*/

//code ya pili

/*document.addEventListener("DOMContentLoaded", function() {
    var chooseButtons = document.querySelectorAll(".book");
    var returnButtons = document.querySelectorAll(".return");

    chooseButtons.forEach(function(button, index) {
        button.addEventListener("click", function() {
            var row = this.parentNode.parentNode;

            // Hide choose button and show return button
            this.style.display = "none";
            returnButtons[index].style.display = "inline";

            // Display a message to the user
            var vehicleId = row.getAttribute("data-vehicle-id");
            alert("You chose vehicle with ID: " + vehicleId);

            // You may want to perform additional actions here, such as updating the database or UI
        });
    });

    returnButtons.forEach(function(button, index) {
        button.addEventListener("click", function() {
            var row = this.parentNode.parentNode;
            

            // Check if the vehicle was previously chosen
            var chooseButton = row.querySelector(".book");
            if (chooseButton.style.display === "none") {
                // Show choose button and hide return button
                chooseButton.style.display = "inline";
                this.style.display = "none";

                // Display a message to the user
                var vehicleId = row.getAttribute("data-vehicle-id");
                alert("You returned vehicle with ID: " + vehicleId);

                // You may want to perform additional actions here, such as updating the database or UI
            } else {
                alert("You haven't chosen this vehicle yet.");
            }
        });
    });
});*/


//code ya tatu

document.addEventListener("DOMContentLoaded", function() {
    var bookButtons = document.querySelectorAll(".book");
    var returnButtons = document.querySelectorAll(".return");

    bookButtons.forEach(function(button, index) {
        button.addEventListener("click", function() {
            var row = this.parentNode.parentNode;

            // Hide book button and show return button
            this.style.display = "none";
            returnButtons[index].style.display = "inline";

            // Display a message to the user
            var vehicleId = row.getAttribute("data-vehicle-id");
            alert("You booked vehicle with ID: " + vehicleId);

            // You may want to perform additional actions here, such as updating the database or UI
        });
    });

    returnButtons.forEach(function(button, index) {
        button.addEventListener("click", function() {
            var row = this.parentNode.parentNode;

            // Hide return button and show book button
            this.style.display = "none";
            row.querySelector(".book").style.display = "inline";

            // Display a message to the user
            var vehicleId = row.getAttribute("data-vehicle-id");
            alert("You returned vehicle with ID: " + vehicleId);

            // You may want to perform additional actions here, such as updating the database or UI
        });
    });
});