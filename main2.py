from pyscript import document, display # type: ignore


def create_order(e):
    # Get input values
    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5")
    
    # Calculate total by multiplying value by checked status (1 or 0)
    total = (float(item1.value) * item1.checked + 
             float(item2.value) * item2.checked + 
             float(item3.value) * item3.checked + 
             float(item4.value) * item4.checked + 
             float(item5.value) * item5.checked)
    
    customer_name = document.getElementById("customer").value
    customer_address = document.getElementById("address").value
    contact_number = document.getElementById("contact_number").value
    
    display(f"Order for: {customer_name}", target="order_output1")
    display(f"Address: {customer_address}", target="order_output2")
    display(f"Contact number: {contact_number}", target="order_output3")
    display(f"Total: ₱ {total:.2f} ", target="show")

