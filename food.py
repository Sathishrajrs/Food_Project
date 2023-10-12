class Food:
    def __init__(self,foodId,foodName,foodQuantity,foodPrice,foodDiscount,foodStock):
        self.foodId=foodId
        self.foodName=foodName
        self.foodQuantity=foodQuantity
        self.foodPrice=foodPrice
        self.foodDiscount=foodDiscount
        self.foodStock=foodStock

    def __str__(self):
        return f"foodId:{self.foodId} \n foodName:{self.foodName} \n foodQuantity:{self.foodQuantity} \n foodPrice:{self.foodPrice} \n foodDiscount:{self.foodDiscount} \n foodStock:{self.foodStock}"

    def set_foodId(self,foodId):
     self.foodId=foodId

    def set_foodName(self,foodName):
     self.foodName=foodName

    def set_foodQuantity(self,foodQuantity):
     self.foodQuantity=foodQuantity

    def set_foodPrice(self,foodPrice):
     self.foodPrice=foodPrice

    def set_foodDiscount(self,foodDiscount):
     self.foodDiscount=foodDiscount

    def set_foodStock(self,foodStock):
     self.foodStock=foodStock
    
    def get_foodId(self):
     return self.foodId

    def get_foodName(self):
     return self.foodName

    def get_foodQuantity(self):
     return self.foodQuantity
    
    def get_foodPrice(self):
     return self.foodPrice

    def get_foodDiscount(self):
     return self.foodDiscount

    def get_foodStock(self):
     return self.foodStock