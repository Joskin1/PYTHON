item = input("What item would you like to buy?: ")
price = float(input(f"What is the price of {item}?: "))
quantity = int(input(f"How many {item}s would you love to buy?: "))
total = price * quantity

print(f"You have bought {quantity} {item}s")
print(f"Your total is ${total:.2f}")
