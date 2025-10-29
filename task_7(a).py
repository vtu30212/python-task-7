def find_discount(qty):
    if qty <= 10:
        return 0
    elif 11 <= qty <= 20:
        return 15
    else:
        return 20

def buy():
    ICode = int(input("Enter Item Code: "))
    Item = input("Enter Item Name: ")
    Price = float(input("Enter Price: "))
    Qty = int(input("Enter Quantity: "))
    Discount = find_discount(Qty)
    Netprice = Price * Qty - Discount
    return ICode, Item, Price, Qty, Discount, Netprice

def show_all(ICode, Item, Price, Qty, Discount, Netprice):
    print("Item Code:", ICode)
    print("Item:", Item)
    print("Price:", Price)
    print("Quantity:", Qty)
    print("Discount:", Discount)
    print("Net Price:", Netprice)
