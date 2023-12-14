<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Order</title>
</head>
<body>
    <h2>Create Order</h2>
    <form action="/create_order" method="post">
        <label for="stall">Select Stall:</label>
        <select name="stall" required>
            % for stall in stalls:
                <option value="{{ stall['id'] }}">{{ stall['name'] }}</option>
            % end
        </select>
        <br>
        <label for="item">Select Item:</label>
        <select name="item" required>
            % for item in items_by_stall.get(stall['id'], []):
                <option value="{{ item['id'] }}">{{ item['itemName'] }} - {{ item['price'] }}</option>
            % end
        </select>
        <br>
        <input type="submit" value="Create Order">
    </form>
</body>
</html>
