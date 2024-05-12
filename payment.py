#from datetime import date
class Payment:
    """תשלום אשראי"""
    def __init__(self):
        flag = False
        self.name=input('enter your name')
        while not flag:
            try:
                self.cardNumber=int(input('enter card number'))
                if len(str(self.cardNumber))==16:
                    flag=True
            except:
                flag = False
        flag = False
        while not flag:
            try:
                self.date=int(input('enter date of card'))
                if self.date/100<13 and self.date%100<32:
                    flag=True
            except:
                flag=False
        self.cvv=input('enter cvv')
        while len(self.cvv)!=3:
            self.cvv = input('enter cvv')
    def writeToFile(self):
        myFile =open("C:/Users/1/Desktop/יד/פייתון/iceCREAM/report.txt",'a')
        myFile.write(f'credit card number: **** **** **** {self.cardNumber%10000}\n')
        myFile.close()