class CostumerDetails:
    """פרטי לקוח"""
    def __init__(self):
        self.name=input('enter your name')

        self.phone=input('enter your phone')
        while len(self.phone) != 9 and len(self.phone) != 10:
            self.phone = input('enter your phone')
        self.city = input('enter your city')
        self.street = input('enter your street')
        self.houseNumber = input('enter your house number')

    def writeToFile(self):
        myFile = open("C:/Users/1/Desktop/יד/פייתון/iceCREAM/report.txt", 'a')
        myFile.write('------------------------------------------------------------------')
        myFile.write('costumer details:')
        myFile.write(f'name:{self.name}, phone number:{self.phone}')
        myFile.write(f'address: {self.city},{self.street},{self.houseNumber}')
        myFile.close()