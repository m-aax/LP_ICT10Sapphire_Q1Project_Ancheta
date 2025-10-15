from pyscript import document, display #type: ignore

contact_us = "Contact Us!"
subtitle = "We'd love to hear from you!"

opening_days = ("9:00 AM", "9:30 PM")


display(f"{contact_us}", target="contact_us")
display(f"{subtitle}", target="subtitle")

display(f"Open: {opening_days[0]} - {opening_days[1]}", target="opening_days")
