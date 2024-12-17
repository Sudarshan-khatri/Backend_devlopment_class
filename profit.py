# function to find the profit and loss then give the subsideory
def profit_loss(cp,sp):
    if sp>cp:
        profit=sp-cp
        sub=profit(0.05*cp)
        return sub
    elif sp<cp:
        loss=cp-sp
        sub=loss-(0.20*cp)
        return sub
    elif sp==cp:
        return (0.10*cp) 
# farmer data of cost price and sell price
Name=input("Enter name of Farmer:")
crop_name=input("Enter crop name:")
cost_price=int(input(f"Enter cost price:"))
sell_price=int(input(f"Enter sell price:"))
print(f"\nFarmer_Name:{Name}")
print(f"Crop_name:{crop_name}")
print(f"subsedory:{profit_loss(cost_price,sell_price)}")

        

