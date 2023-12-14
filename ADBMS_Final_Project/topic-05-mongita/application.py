from bottle import route, post, run, template, redirect, request
from bson.objectid import ObjectId
import database
from database import kentstate_student_centre_db
from bottle import get
from bottle import response


@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    stalls = database.get_stalls()
    print("list of stalls")
    print(stalls)
    return template("C:/Users/indir/Downloads/advanced-database-main/advanced-database-main/gamma/topic-05-mongita/views/list.tpl", shopping_list=stalls)

@route("/add")
def get_add():
    return template("C:/Users/indir/Downloads/advanced-database-main/advanced-database-main/gamma/topic-05-mongita/views/add_item.tpl")

@post("/add")
def post_add():
    # Get form data
    stall_name = request.forms.get("stallName")
    stall_location = request.forms.get("stallLocation")
    item_name = request.forms.get("itemName")
    item_price = float(request.forms.get("itemPrice"))  # Convert to float assuming price is a decimal

    # Validate form data (add your own validation logic as needed)

    # Add stall and item to the database
    database.add_stall_item(stall_name, stall_location, item_name, item_price)

    # Redirect to the list route
    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    print("Delete Operation")
    print(id)
    database.delete_stall(id)
    redirect("/list")

@post("/delete/<id>")
def post_delete(id):
    database.delete_stall(id)
    redirect("/list")

@route("/update/<id>")
def get_update(id):
    try:
        # Convert the string ID to ObjectId
        stall_id = ObjectId(id)
        stall = database.get_stall(stall_id)

        if not stall:
            return template("path/to/your/stall_not_found.tpl")

        # Retrieve existing items
        existing_items = stall.get('items', [])

        return template("path/to/your/update_item.tpl", id=id, stall_name=stall['name'], stall_location=stall['location'], existing_items=existing_items)
    except Exception as e:
        print(f"Error in get_update: {e}")
        return template("C:/Users/indir/Downloads/advanced-database-main/advanced-database-main/gamma/topic-05-mongita/views/error.tpl")

@post("/update/<id>")
def post_update(id):
    stall_name = request.forms.get("stallName")
    stall_location = request.forms.get("stallLocation")
    item_names = request.forms.getall("item_name[]")
    item_prices = request.forms.getall("item_price[]")

    items = [{"itemName": item_name, "price": float(item_price)} for item_name, item_price in zip(item_names, item_prices)]

    # Assuming you have an 'update_stall' function in your database.py
    database.update_stall(id, stall_name, stall_location, items)

    redirect("/list")

@route("/create")
def get_create():
    return template("C:/Users/indir/Downloads/advanced-database-main/advanced-database-main/gamma/topic-05-mongita/views/create_stall.tpl")


@post("/create")
def post_create():
    return create_stall()

def create_stall():
    # Print form data for debugging
    print(request.forms)
    name = request.forms.get('new_name')
    location = request.forms.get('new_location')
    item_names = request.forms.get('new_item_name')
    item_prices = request.forms.get('new_item_price')

    # Print items data
    print(f"Item Names: {item_names}")
    print(f"Item Prices: {item_prices}")

    items = [{"itemName": item_names, "price": float(item_prices)}]

    stall_id = database.add_stall(name, location, items)

    # Retrieve the details of the created stall
    created_stall = database.get_stall(stall_id)

    # Render a template with the details
    return template("views/created_stall_template.tpl", created_stall=created_stall)


@get('/get_stall_details')
def get_stall_details():
    stall_id = request.query.id
    
    # Use the stall_id to fetch details from the database
    stall_details = database.get_stall(stall_id)

    # Format the stall details for JSON response
    formatted_details = {
        "location": stall_details.get("location", ""),
        "items": [{"itemName": item["itemName"], "price": item["price"]} for item in stall_details.get("items", [])]
    }

    return json.dumps(formatted_details)



@route('/create_order')
def create_order():
    shopping_list = database.get_stalls()

    return template("views/list.tpl", shopping_list=shopping_list)

@route('/get_stall_details')
def get_stall_details():
    stall_id = request.query.id
    stall_details = database.get_stall(stall_id)

    return {"location": stall_details.get("location", "Unknown"), "items": stall_details.get("items", [])}


@route('/create_order', method='GET')
def create_order():
    try:
        stall_id = request.query.stall_select
        item_quantity = int(request.query.item_quantity)

        # Use stall_id to fetch details from the database
        stall_details = database.get_stall(stall_id)
       # Create the order in the database with quantity
        # Ensure the stall_details exist
        if not stall_details:
            return "Stall not found"

        # Extract stall information
        stall_name = stall_details['name']
        stall_location = stall_details['location']
        items = stall_details['items']

        # Ensure the items list is not empty
        if not items:
            return "No items available in the selected stall"

        # Extract the first item for simplicity (you might want to handle multiple items)
        selected_item = items[0]
        item_name = selected_item['itemName']
        item_price = selected_item['price']

        # Calculate total price
        total_price = item_price * item_quantity

     
        # Create an HTML order receipt
        order_receipt = f"""
        <html>
        <head>
            <title>Order Receipt</title>
        </head>
        <body>
            <h1>Order Receipt</h1>
            <p>Thank you for your order!</p>
            <h2>Stall Information:</h2>
            <p><strong>Stall Name:</strong> {stall_name}</p>
            <p><strong>Stall Location:</strong> {stall_location}</p>
            <h2>Ordered Item:</h2>
            <p><strong>Item Name:</strong> {item_name}</p>
            <p><strong>Unit Price:</strong> ${item_price}</p>
            <h2>Order Details:</h2>
            <p><strong>Quantity:</strong> {item_quantity}</p>
            <p><strong>Total Price:</strong> ${total_price}</p>
        </body>
        </html>
        """

        response.content_type = 'text/html'
        return order_receipt

    except Exception as e:
        print(f"Error in create_order: {e}")
        return "Error creating order"
    
@route('/orders')
def show_orders():
    orders = database.get_orders()
    print("Orders:", orders)  # Add this line for debugging
    return template("views/orders_list.tpl", orders=orders)

# Add a route to display the order receipt for a specific order
@route('/order_receipt/<order_id>')
def view_order_receipt(order_id):
    order = database.get_order(order_id)
    return template("views/order_receipt.tpl", order=order)


run(host='localhost', port=8080)
