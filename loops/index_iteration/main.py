prices = [29.99, 45.50, 12.75, 38.20]
discount1 = 0.10
discount2 = 0.20
discount3 = 0.15
discount4 = 0.05
for INDEX in range(len(prices)):
    if INDEX == 0:
        factor = discount1
    elif INDEX == 1:
        factor = discount2
    elif INDEX == 2:
        factor = discount3
    else:
        factor = discount4

    prices[INDEX] = prices[INDEX] * (1 - factor)
    print(f"Updated price for item {INDEX}: ${prices[INDEX]:.2f}")
    