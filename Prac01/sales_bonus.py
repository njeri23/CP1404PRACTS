while True:
    sales = float(input("Enter the sales: $"))
    if sales < 0:
        break
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
        print("The bonus is: $", bonus)
