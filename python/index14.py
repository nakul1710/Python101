#Shopping cart Program


foods = []
prices = []
total = 0

while True:
    food = input("Enter the food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        try:
            price = float(input(f"Enter the price of {food} : $"))
        except ValueError:
            print("Please enter a valid number for the price.")
            continue
        foods.append(food)
        prices.append(price)

print("-------YOUR CART------")

for food in foods:
    print(food, end=" ")

for price in prices :
    total += price

print(f"Your total is : ${total:.2f}")