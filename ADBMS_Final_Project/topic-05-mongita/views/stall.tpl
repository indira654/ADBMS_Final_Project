<h1>{{ food_stall.name }}</h1>
<ul>
{% for item in items %}
    <li>
        <input type="checkbox" name="items" value="{{ item.id }}"> {{ item.name }} - ${{ item.price }}
    </li>
{% endfor %}
<br>
<form action="{{ url_for('create_order') }}" method="POST">
    <input type="hidden" name="stall_id" value="{{ food_stall.id }}">
    <button type="submit">Place Order</button>
</form>
