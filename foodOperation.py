import random
from food import Food

class foodOperation:
    Food_List=[]
    def addFood(self):
        print("******Add Book*******")
        foodId=random.randint(1,200)
        foodName=input("Enter food name:")
        foodQuantity=input("Enter food Quantity:")
        foodPrice=float(input("Enter food Price:"))
        foodDiscount=float(input("Enter food Discount:"))
        foodStock=int(input("Enter food Stock:"))
        food_obj=Food(foodId,foodName,foodQuantity,foodPrice,foodDiscount,foodStock)
        foodOperation.Food_List.append(food_obj)
        print("Added Successfully")
    
    def editFood(self):
         print("******Edit Food*******")
         EnterId=int(input("Enter FoodId:"))
         for id in foodOperation.Food_List:
             if id.get_foodId()==EnterId:
                 foodName=input("Enter food name:")
                 foodQuantity=input("Enter food Quantity:")
                 foodPrice=float(input("Enter food Price:"))
                 foodDiscount=float(input("Enter food Discount:"))
                 foodStock=int(input("Enter food Stock:"))

                 id.set_foodName(foodName)
                 id.set_foodQuantity(foodQuantity)
                 id.set_foodPrice(foodPrice)
                 id.set_foodDiscount(foodDiscount)
                 id.set_foodStock(foodStock)
                 break
         else:
            print("foodId is not matching")
        
    def viewFood(self):
         print("******View Food*******")
         for i in foodOperation.Food_List:
           print(i)

    def removeFood(self):
         print("******Remove Food*******")
         EnterId=int(input("Enter FoodId:"))
         for id in foodOperation.Food_List:
             if id.get_foodId()==EnterId:
                 foodOperation.Food_List.remove(id)
                 print("***Removed Successfully***")
                 break
         else:
             print("foodId is not matching")
                 
        


