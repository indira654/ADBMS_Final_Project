<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Receipt</title>
</head>
<body>
    <h1>Order Receipt</h1>
    <p>Thank you for your order!</p>
    <h2>Stall Information:</h2>
    <p><strong>Stall Name:</strong> {{ order.stall.name }}</p>
    <p><strong>Stall Location:</strong> {{ order.stall.location }}</p>
    <h2>Ordered Item:</h2>
    <p><strong>Item Name:</strong> {{ order.item.itemName }}</p>
    <p><strong>Unit Price:</strong> ${{ order.item.price }}</p>
    <h2>Order Details:</h2>
    <p><strong>Quantity:</strong> {{ order.quantity }}</p>
    <p><strong>Total Price:</strong> ${{ order.total_price }}</p>
    <a href="/orders">Back to Orders List</a>
</body>
</html>
