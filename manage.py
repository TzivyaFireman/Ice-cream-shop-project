
class Manage:
    INGREDIENTS={
        "blila":{
            "krep":6,
            "vafelBelgy":20
        },
        "iceCream":{
            "strawberry":5,
            "moka":10,
            "chokolate":14,
            "fistuk":6
        },
        "add":{
            "chocolate":10,
            "whiteChocolate":10,
            "coolies":10,
            "pekan":10,
            "mekupelet":10
        }
    }

    def ifExitst(self,prod):
        """מחזירה האם נתן לקנות את המוצר"""
        if Manage.INGREDIENTS["blila"][prod]>0:
            Manage.INGREDIENTS["blila"][prod] -=1
            return True
        return False
    def relevantOptions(self,prod):
        """מחזיר מלאי של הבחירות:גלידה או תוספות"""
        arr=(k for k,v in Manage.INGREDIENTS[prod].items()if v>0)
        return arr
    def chooseAdds(self,name):
        category=""
        if name=="iceCream":
            category=IceCream
            print('choose 3 tastes')
        else:
            category="add"
            print('choose 3 adds')
        print(f'the relevant tastes are: ')
        print(list(self.relevantOptions(category)))
        arr = [3]
        relevant = list(self.relevantOptions(category))
        for i in range(3):
            arr.append(input())
            while not (arr[i]) in relevant:
                arr[i] = input('not correct input try again')
            self.subFromIngredients(category,arr[i])
        return arr

    def subFromIngredients(self,category,subCategory):
        """מפחית את המוצר מהמלאי"""
        self.INGREDIENTS[category][subCategory] -= 1

    def addToIngredients(self,category,subCategory,quantity):
        """מוסיף כמות למלאי"""
        try:
            Manage.INGREDIENTS[category][subCategory]+=int(quantity)
            print("the add sucsseded")
        except:
            print("the add feld")
    def showQuantity(self):
        """מדפיס את הכמויות"""
        for category,ingredientDict in Manage.INGREDIENTS.items():
            print(category)
            for name,count in ingredientDict.items():
                print(f"    {name}:{count}")

    def report(self):
        """מדפיס את הקניות שארעו ביום זה"""

        myFile = open("C:/Users/1/Desktop/יד/פייתון/iceCREAM/report.txt", 'r')
        print(myFile.read())
        myFile.close()

    def manage(self):
        choose=input("ptress quantity or report for exit press exit")
        while choose!="exit":
            if choose=="quantity":
                self.showQuantity()
                category=input("insert what to add for ending press end")
                while category!="end":
                    subCategory=input()
                    quantity=input()
                    self.addToIngredients(category,subCategory,quantity)
                    category=input()
            if choose=="report":
                self.report()
            choose = input("ptress quantity or report for exit press exit")