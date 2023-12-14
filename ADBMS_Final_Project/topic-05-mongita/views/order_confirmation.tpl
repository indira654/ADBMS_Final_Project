<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Confirmation</title>
</head>
<body>
    <h2>Order Confirmation</h2>
    <p>Order ID: {{ order_id }}</p>
    <p>Stall: {{ stall['name'] }}</p>
    <p>Item: {{ item['itemName'] }}</p>
    <p>Price: {{ item['price'] }}</p>
</body>
</html>
