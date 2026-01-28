# Concession stand program

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,      # fixed typo from 'pretezel'
    "lemonade": 4.25
}

cart = []
total = 0

print("----- MENU -----")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    item = input("Enter an item to add to your cart (or 'q' to quit): ")
    if item.lower() == 'q':
        break
    elif item in menu:
        cart.append(item)
        total += menu[item]
        print(f"Added {item} to cart. Total so far: ${total:.2f}")
    else:
        print("Sorry, we don't have that item.")

print("\n----- YOUR CART -----")
for item in cart:
    print(f"{item:10}: ${menu[item]:.2f}")
print(f"Total: ${total:.2f}")