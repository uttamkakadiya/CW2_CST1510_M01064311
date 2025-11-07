# Week 1 Topic: print() function
# Display a welcome message to the user
print("Welcome to the Simple Shopping Bill Calculator!")

# ---------- Take input for the first item ----------
# Week 1 Topic: input() function, string data type
item1_name = input("Enter the name of first item: ")

# Week 1 Topic: input() function, float data type, variables
item1_price = float(input("Enter the price of first item: "))

# Week 1 Topic: input() function, int data type, variables
item1_qty = int(input("Enter the quantity of first item: "))

# ---------- Take input for the second item ----------
item2_name = input("Enter the name of second item: ")
item2_price = float(input("Enter the price of second item: "))
item2_qty = int(input("Enter the quantity of second item: "))

# ---------- Calculate total cost for each item ----------
# Week 1 Topic: basic math operations (*), variables
item1_total = item1_price * item1_qty
item2_total = item2_price * item2_qty

# ---------- Calculate the total bill ----------
# Week 1 Topic: basic math operations (+), variables
total_bill = item1_total + item2_total

# ---------- Display the bill summary using f-strings ----------
print("\n----- Shopping Bill -----")  # Header

# Show first item details
print(f"{item1_name} x {item1_qty} = {item1_total}")

# Show second item details
print(f"{item2_name} x {item2_qty} = {item2_total}")

# Show the total bill
print(f"Total Bill = {total_bill}")
