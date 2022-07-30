quantity = int(input("Enter the no of quantity : "))
price = float(input("Enter price per item : "))
total_expense = price * quantity
if quantity > 1000:
    total_expense = price * quantity - (10/100)*price*quantity 
    print(total_expense)
else:
    print(total_expense)