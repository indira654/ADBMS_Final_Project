<!-- orders_template.tpl -->
<html>
<body>
  <h2>Orders</h2>
  <hr/>
  <table>
    % for order in orders:
      <tr>
        <td>Stall: {{ order['stall_id'] }}</td>
        <td>Item: {{ order['item_id'] }}</td>
        <td>Price: {{ order['new_price'] }}</td>
      </tr>
    % end
  </table>
  <hr/>
</body>
</html>
