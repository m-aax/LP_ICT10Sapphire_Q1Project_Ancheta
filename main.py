from pyscript import display # type: ignore
#Restaurant Order System Python Data Types

#string data type
restaurant_name = "Maximus PRIME"
owner_name = "Anchemus Prime"

#integers
year_Since = 1418

#Float
tax_rate = 0.08

#boolean
has_delivery = True 
is_dine_in = True
is_takeout = False

#list
product_name = ["Tortang Talong", 
                "Fried Chicken Platter", 
                "Double Hamburger",
                "Biryani"
                ]

beverages = ["Water",
            "Iced Tea", 
            "Bottomless Lemonade"
            ]

#Tuple
business_hours = ("9:00 AM", "9:30 PM")

#dictonary
menu = {
    "Tortang Talong": 129.99,
    "Fried Chicken Platter": 229.00,
    "Double Hamburger": 299.99,
    "Biryani": 425.00,
    "Water": 19.69,
    "Iced Tea":49.99,
    "Bottomless Lemonade": 99.59
}

#Set
common_allergens = ("gluten","dairy","nuts","shellfish")

#display resto information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_Since}", target="since")
display(f"Menu Pricelist", target="heading1")

#displaying Menu items:
display(product_name[0], target="prod1")
display(f"P{menu['Tortang Talong']:.2f}", target="price1")

display(product_name[1], target="prod2")
display(f"P{menu['Fried Chicken Platter']:.2f}", target="price2")

display(product_name[2], target="prod3")
display(f"P{menu['Double Hamburger']:.2f}", target="price3")

display(product_name[3], target="prod4")
display(f"P{menu['Biryani']:.2f}", target="price4")

#BEVERAGE prices, it goes back to 0 because we have another list
display(beverages[0], target="prod5")
display(f"P{menu['Water']:.2f}", target="price5")

display(beverages[1], target="prod6")
display(f"P{menu['Iced Tea']:.2f}", target="price6")

display(beverages[2], target="prod7")
display(f"P{menu['Bottomless Lemonade']:.2f}", target="price7")

#display additional Information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

#display order type
display(f"Dine In and Take Out Available at Maximus PRIME! Quality food for you.", target="orderType")
