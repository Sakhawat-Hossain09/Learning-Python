def shoppingCart():
    items = []
    prices = []
    total = 0
    while True:
        item = input("What item would you like to buy [press 'Q' to quit]: ")
        if item.upper() != "Q":
            price = int(input("What is the price of the item: "))
            items.append(item)
            prices.append(price)
            total += price
        else:
            break
    print(f"You have bought {items} and the prices are {prices} and total is ${total}.")
