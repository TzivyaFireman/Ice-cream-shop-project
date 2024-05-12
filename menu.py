class Product:
    """מחלקה לתיאור מופשט של מוצר"""
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def writeToFile(self):
        myFile = open("C:/Users/1/Desktop/יד/פייתון/iceCREAM/report.txt", 'a')
        myFile.write('order:\n')
        myFile.write(f'name: {self.name} price:{self.price}\n')
        myFile.close()

class BakedProduct(Product):
    """מתארת וופל בלגי או קרפ צרפתי"""
    def __init__(self,name,adds):
        super(BakedProduct,self).__init__(name,20)
        self.adds=adds
    def writeToFile(self):
        super(BakedProduct, self).writeToFile()
        myFile = open("C:/Users/1/Desktop/יד/פייתון/iceCREAM/report.txt", 'a')
        myFile.write('adds:')
        myFile.write(f'adds: {self.adds}')
        myFile.close()





class IceCream(Product):
    """מתארת גלידה"""
    def __init__(self,name,tastes):
        super(IceCream,self).__init__(name,18)
        self.tastes=tastes
    def writeToFile(self):
        super(IceCream, self).writeToFile()
        myFile = open("C:/Users/1/Desktop/iceCREAM/report.txt", 'a')
        myFile.write('adds:')
        myFile.write(f'tastes: {tastes}')
        myFile.close()





