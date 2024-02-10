selling_price = float(input("enter the selling_price : "))
cost_price = float(input("enter the cost_price : "))
if selling_price > cost_price : 
    print("the retailer has made the profit of Rs.",selling_price - cost_price )
elif selling_price < cost_price : 
    print("the retailer has suffered loss of Rs.",cost_price - selling_price)
else:
    print("the retailer hasn't made any profit")