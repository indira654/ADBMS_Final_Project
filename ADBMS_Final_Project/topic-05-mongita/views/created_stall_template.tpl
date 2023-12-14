<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Created Stall Details</title>
</head>
<body>
    <h2>Stall Created Successfully</h2>
    <strong>ID:</strong> {{ created_stall["id"] }} <br>
    <strong>Name:</strong> {{ created_stall["name"] }} <br>
    <strong>Location:</strong> {{ created_stall["location"] }} <br>
    <strong>Items:</strong>
    <ul>
        % for item in created_stall['items']:
            <li>{{ item['itemName'] }} - {{ item['price'] }}</li>
        % end
    </ul>
</body>
</html>
