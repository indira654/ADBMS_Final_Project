<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kent Student Centre</title>
</head>
<body>
    <h1> Kent Student Centre Stalls and its Most Special Item</h1>
    <ul>
        % for stall in shopping_list:
            <li>
                <strong>ID:</strong> {{ stall["id"] }} <br>
                <strong>Name:</strong> {{ stall["name"] }} <br>
                <strong>Location:</strong> {{ stall["location"] }} <br>
                <strong>Items:</strong>
                <ul>
                    % for item in stall['items']:
                        <li>
                            {{ item['itemName'] }} - {{ item['price'] }}
                        </li>
                    % end
                </ul>
               <form action="/update/{{ stall['id'] }}" method="post">
    <strong>New Name:</strong>
    <input type="text" name="stallName" value="{{ stall['name'] }}" required>
    <br>
    <strong>New Location:</strong>
    <input type="text" name="stallLocation" value="{{ stall['location'] }}" required>
    <br>
    <strong>Update Items:</strong>
    <ul>
        % for item in stall['items']:
            <li>
                <input type="text" name="item_name[]" value="{{ item['itemName'] }}" required>
                -
                <input type="text" name="item_price[]" value="{{ item['price'] }}" required>
            </li>
        % end
    </ul>
    <input type="hidden" name="id" value="{{ stall['id'] }}">
    <input type="submit" value="Update">
</form>
                <form action="/delete/{{ stall['id'] }}" method="post">
                    <input type="submit" value="Delete">
                </form>
                
              
                
            </li>
        % end
    </ul>

    <!-- Form for creating a new stall -->
    <form action="/create" method="post">
        <h2>Create New Stall</h2>
        <label for="new_name">Name:</label>
        <input type="text" name="new_name" required>
        <br>
        <label for="new_location">Location:</label>
        <input type="text" name="new_location" required>
        <br>
        <label for="new_item_name">Item Name:</label>
        <input type="text" name="new_item_name" required>
        -
        <label for="new_item_price">Item Price:</label>
        <input type="text" name="new_item_price" required>
        <br>
        <input type="submit" value="Create Stall">
    </form>

    <!-- Existing code... -->

<!-- Form for creating a new order -->
<form action="/create_order" method="get">
    <h2>Create Order</h2>
    
    <!-- Dropdown to select a stall -->
    <label for="stall_select">Select Stall:</label>
    <select name="stall_select" id="stall_select" required>
        % for stall in shopping_list:
            <option value="{{ stall['id'] }}">{{ stall['name'] }}</option>
        % end
    </select>
    <br>

    <!-- Display stall details -->
    <div id="stall_details">
        <!-- The details for the selected stall will be displayed here -->
    </div>

    <!-- Dropdown to select the number of items -->
    <label for="item_quantity">Number of Items:</label>
    <select name="item_quantity" required>
        % for i in range(1, 11):
            <option value="{{ i }}">{{ i }}</option>
        % end
    </select>
    <br>

    <!-- Submit button to create the order -->
    <input type="submit" value="Create Order">
</form>

<!-- Script for updating stall details dynamically -->
<script>
    function updateStallDetails() {
        var stallId = document.getElementById("stall_select").value;

        // Make an AJAX request to get stall details
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/get_stall_details?id=" + stallId, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                var stallDetails = JSON.parse(xhr.responseText);
                formatStallDetails(stallDetails);
            }
        };
        xhr.send();
    }

    function formatStallDetails(data) {
        var stallDetailsDiv = document.getElementById("stall_details");
        stallDetailsDiv.innerHTML = "<strong>Location:</strong> " + data.location + "<br>";

        stallDetailsDiv.innerHTML += "<strong>Items:</strong><ul>";
        for (var i = 0; i < data.items.length; i++) {
            stallDetailsDiv.innerHTML += "<li>" + data.items[i].itemName + " - $" + data.items[i].price + "</li>";
        }
        stallDetailsDiv.innerHTML += "</ul>";
    }

    // Attach the updateStallDetails function to the change event of the stall_select dropdown
    document.getElementById("stall_select").addEventListener("change", updateStallDetails);
</script>
<!-- Link to view the list of orders -->
<a href="/orders">View Orders</a>

<!-- Existing code... -->

</body>
</html>
