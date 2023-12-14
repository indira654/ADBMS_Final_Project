from mongita import MongitaClientDisk
from bson.objectid import ObjectId

client = MongitaClientDisk()

kentstate_student_centre_db = client.kentstate_student_centre

# Function to set up the initial database with sample data
def setup_database():
    # Clear stalls_collection
    kentstate_student_centre_db.drop_collection("stalls_collection")
    stalls_collection = kentstate_student_centre_db.stalls_collection

    # Clear orders_collection
    kentstate_student_centre_db.drop_collection("orders_collection")
    orders_collection = kentstate_student_centre_db.orders_collection

    # Add sample stalls to the stalls_collection
    sample_stalls = [
        {"name": "Stall 1", "location": "Location 1", "items": [{"itemName": "Item 1", "price": 10.99}]},
        {"name": "Stall 2", "location": "Location 2", "items": [{"itemName": "Item 2", "price": 5.99}]},
        # Add more stalls and items as needed
    ]
    stalls_collection.insert_many(sample_stalls)

    # Add sample orders to the orders_collection
    sample_orders = [
        {"stall_id": ObjectId("..."), "items": [{"itemName": "Item 1", "quantity": 2}]},
        # Add more orders as needed
    ]
    orders_collection.insert_many(sample_orders)

# Function to get stall items by stall_id
def get_stall_items(stall_id):
    stalls_collection = kentstate_student_centre_db.stalls_collection
    return stalls_collection.find_one({'_id': ObjectId(stall_id)}, projection={"items": 1})


# In database.py
def add_stall_item(stall_name, stall_location, item_name, item_price):
    stalls_collection = kentstate_student_centre_db.stalls_collection

    # Find the stall or create a new one if it doesn't exist
    stall = stalls_collection.find_one({"name": stall_name, "location": stall_location})
    if not stall:
        stall_id = stalls_collection.insert_one({
            "name": stall_name,
            "location": stall_location,
            "items": [{"itemName": item_name, "price": item_price}]
        }).inserted_id
    else:
        stall_id = stall["_id"]
        # Append the new item to the existing stall
        stalls_collection.update_one(
            {"_id": stall_id},
            {"$push": {"items": {"itemName": item_name, "price": item_price}}}
        )

    return stall_id


# Function to get all stalls or a specific stall by ID
def get_stalls(id=None):
    stalls_collection = kentstate_student_centre_db.stalls_collection
    if id is None:
        stalls = stalls_collection.find({})
    else:
        stalls = stalls_collection.find({"_id": ObjectId(id)})
    stalls = list(stalls)
    for stall in stalls:
        stall["id"] = str(stall["_id"])  # Change "name" to "id"
    return stalls

def add_stall(name, location, items):
    stalls_collection = kentstate_student_centre_db.stalls_collection
    stall_id = stalls_collection.insert_one({"name": name, "location": location, "items": items}).inserted_id
    return stall_id

# Function to update stall information
def update_stall(id, name, location, items):
    stalls_collection = kentstate_student_centre_db.stalls_collection
    where = {"_id": ObjectId(id)}
    updates = {"$set": {"name": name, "location": location, "items": items}}
    stalls_collection.update_one(where, updates)

# Function to delete a stall by ID
def delete_stall(id):
    stalls_collection = kentstate_student_centre_db.stalls_collection
    stalls_collection.delete_one({"_id": ObjectId(id)})

# Function to get a stall by ID
def get_stall(id):
    stalls_collection = kentstate_student_centre_db.stalls_collection
    stall = stalls_collection.find_one({"_id": ObjectId(id)})
    if stall:
        stall["id"] = str(stall["_id"])
    return stall
# Function to get item details by item_id
def get_stall_item(item_id):
    stalls_collection = kentstate_student_centre_db.stalls_collection
    return stalls_collection.find_one({'items._id': ObjectId(item_id)},
                                      projection={"items.$": 1})

def get_order(order_id):
    orders_collection = kentstate_student_centre_db.orders_collection
    order = orders_collection.find_one({"_id": ObjectId(order_id)})

    # Retrieve additional details (stall and item information) if needed
    if order:
        order["stall"] = get_stall(str(order["stall_id"]))
        order["item"] = get_stall_item(str(order["item_id"]))

    return order

# Function to get all orders
def get_orders():
    orders_collection = kentstate_student_centre_db.orders_collection
    # Fetch all fields including 'items'
    orders = list(orders_collection.find().sort("_id", 1))

    return orders

from datetime import datetime

def create_order(stall_id, item_id, quantity):
    orders_collection = kentstate_student_centre_db.orders_collection

    # Fetch stall and item details from the database
    stall_details = get_stall(stall_id)
    item_details = get_stall_item(item_id)

    # Calculate total price
    total_price = item_details['price'] * quantity

    order_data = {
        "stall_id": ObjectId(stall_id),
        "item_id": ObjectId(item_id),
        "timestamp": datetime.utcnow(),
        "stall_name": stall_details["name"],
        "item_name": item_details["itemName"],
        "item_price": item_details["price"],  # Include item price
        "quantity": quantity,
        "total_price": total_price  # Include total price
    }

    order_id = orders_collection.insert_one(order_data).inserted_id
    print(f"Order created with ID: {order_id}")

    return order_id





# Function to update the price of an order
def update_order_price(order_id, new_price):
    orders_collection = kentstate_student_centre_db.orders_collection
    where = {"_id": ObjectId(order_id)}
    updates = {"$set": {"new_price": new_price}}
    orders_collection.update_one(where, updates)

if __name__ == "__main__":
    # Call setup_database to initialize the database with sample data
    setup_database()
