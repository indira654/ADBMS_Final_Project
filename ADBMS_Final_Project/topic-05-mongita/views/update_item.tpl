<!-- update_item.tpl -->
<!DOCTYPE html>
<html>
<head>
    <title>Update Stall</title>
</head>
<body>
    <h2>Update Stall</h2>
    <form action="/update" method="post">
        <input type="hidden" name="id" value="{{ id }}">
        <label for="stallName">Name:</label>
        <input type="text" name="stallName" value="{{ stall_name }}" required><br>
        <label for="stallLocation">Location:</label>
        <input type="text" name="stallLocation" value="{{ stall_location }}" required><br>
        <!-- Add fields for updating items if needed -->
        <input type="submit" value="Update">
    </form>
    <a href="/list">Back to List</a>
</body>
</html>
