# data source
# can replace this with a CSV file later

import datetime as dt
import os

from dotenv import load_dotenv

load_dotenv() 

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# Function for formatting currency
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


#User Input section
#define subtotal price variable
subtotal_price = 0
checkout_start_at = dt.datetime.now() # current date and time, see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/datetime.md


# capture product ids until we're done
# creating a set of all of the unique IDs
# so we can compare our selected IDs against this set
# courtsey of some pair programming with Tanner T. 

all_ids = {str(p["id"]) for p in products}

selected_ids = []
while True:
    selected_id = input("Please select / scan a valid product id, or 'DONE' when complete ")
    if selected_id.upper() == "DONE":
        break
    elif selected_id in all_ids:
        # id is valid!
        selected_ids.append(selected_id)
    else:
        # id is not valid!
        print("Invalid ID, please try again")

# Helper file from prof. Repo: https://github.com/s2t2/shopping-cart-screencast/blob/master/shopping_cart.py#L31


# NB: all inputs end up as strings


# Formatted receipt 

print("-------------------")
print("Green Valley Book Fair")
print("https://gobookfair.com/")
print("800-385-0099")
print("-------------------")
print("Checkout Date & Time: " + checkout_start_at.strftime("%Y-%m-%d %I:%M %p"))
print("-------------------")
print("Your Items:")

# Perform product lookups to determine what the product's name and price are

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal_price = subtotal_price + matching_product["price"]
    print(" + " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")


print("-------------------")
print("Subtotal: " + to_usd(subtotal_price))

# TAX_RATE (all caps) = ENV variable
# tax_rate (lower case) is variable within this script

tax_rate = float(os.getenv("TAX_RATE"))

Sales_Tax = subtotal_price* tax_rate
print(f"Sales Tax ({tax_rate:.2%}):", to_usd(Sales_Tax))

Grand_Total = subtotal_price+Sales_Tax
print("Total:", to_usd(Grand_Total)) #add subtotal + sales tax

print("-------------------")
print("Thank you for your business. Please come again!")
# Receipt generation section

