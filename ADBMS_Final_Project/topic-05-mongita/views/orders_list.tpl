<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Orders List</title>
</head>
<body>
    <h1>Orders List</h1>
    <ul>
        % for order in orders:
            <li>
                <strong>Order ID:</strong> {{ order["_id"] }} <br>
                <strong>Stall Name:</strong> {{ order.stall.name }} <br>
                <strong>Item Name:</strong> {{ order.item.itemName }} <br>
                <strong>Quantity:</strong> {{ order.quantity }} <br>
                <strong>Total Price:</strong> ${{ order.total_price }} <br>
                <a href="/order_receipt/{{ order["_id"] }}">View Receipt</a>
            </li>
        % end
    </ul>
    <a href="/list">Back to Main Page</a>
</body>
</html>
