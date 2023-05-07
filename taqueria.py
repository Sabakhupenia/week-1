# Define a dictionary that maps menu item names to their prices
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# Initialize a variable to keep track of the total cost of the order
total_cost = 0
# Start an infinite loop that will continue until the user enters an end-of-file character
while True:
    try:
       # Prompt the user to enter an item from the menu
       item = input("Item: ").title()
       # If the item is in the menu, add its price to the total cost of the order
       if item in menu:
            total_cost = total_cost + menu[item]
        # Print the updated total cost of the order
       print(f"Total: ${total_cost:.2f}")
    # If the user enters an end-of-file character, print a newline character and break out of the loop
    except EOFError:
        print("\n",end="")
        break


