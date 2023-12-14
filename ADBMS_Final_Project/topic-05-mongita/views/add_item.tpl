<<!DOCTYPE html>
<html>
<head>
  <title>Add Item</title>
</head>
<body>
  <h2>Add Item to Stall</h2>
  <hr/>

  <form action="/add" method="post">
    <!-- Stall Information -->
    <p>Stall Name: <input name="stallName" required/></p>
    <p>Location: <input name="stallLocation" required/></p>

    <!-- Item Information -->
    <p>New Item: <input name="itemName" required/></p>
    <p>Price: <input name="itemPrice" type="number" step="0.01" required/></p>

    <!-- Submit Button -->
    <p><button type="submit">Submit</button></p>
  </form>

  <hr/>
</body>
</html>
