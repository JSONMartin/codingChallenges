def mango(quantity, price):
    return (quantity - quantity//3) * price
    #return (quantity * price) - ((quantity // 3) * price)

print(mango(3, 3))