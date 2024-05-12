import os
from PIL import Image
from manage import Manage
from menu import Product
from menu import BakedProduct
from menu import IceCream
from payment import  Payment
from costumerDetails import CostumerDetails


manager = Manage()
choice= input('what would you like: vafelBelgy, krep, iceCream, to exit enter off')
while choice!="off":
    if choice == "vafelBelgy" or choice == "krep" or choice == "iceCream":
        if not manager.ifExitst(choice):
            print('product not exists')
        else:
            if choice =="vafelBelgy" or choice =="krep":
                prod= BakedProduct(choice,manager.chooseAdds(choice))
            else:
                prod = IceCream(choice, manager.chooseAdds(choice))
        details=CostumerDetails()
        pay=Payment()
        details.writeToFile()
        prod.writeToFile()
        pay.writeToFile()
        print("the order is on the way")
        img = Image.open('images/קינוח-קרפ צרפתי.jpg')
        img.show()
    if choice == "manager":
        manager.manage()
    choice=input()