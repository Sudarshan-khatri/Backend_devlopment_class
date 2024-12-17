# function to find the profit and loss then give the subsideory
def profit_loss(cp,sp):
    if sp>cp:
        profit=sp-cp
        sub=profit+(0.05*cp)
        return sub
    else:
        loss=cp-sp
        sub=loss+(0.20*cp)
        return sub
# farmer data of cost price and sell price
cost_price=int(input(f"Enter cost price:"))
sell_price=int(input(f"Enter sell price:"))
print(f"subsedory:{profit_loss(cost_price,sell_price)}")

        

