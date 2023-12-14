<!-- Stall Details -->
<strong>Stall Name:</strong> {{ stall['name'] }} <br>
<strong>Location:</strong> {{ stall['location'] }} <br>
<strong>Items:</strong>
<ul>
    % for item in stall['items']:
        <li>{{ item['itemName'] }} - {{ item['price'] }}</li>
    % end
</ul>