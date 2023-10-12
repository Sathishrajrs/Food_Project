from foodOperation import *
class main:
    def execute(self,choice,operation):
        if choice==1:
            operation.addFood()
        elif choice==2:
            operation.editFood()
        elif choice==3:
            operation.viewFood()
        elif choice==4:
            operation.removeFood()
        else:
            exit(1)
obj=main()
operation=foodOperation()

while True:
  choice=int(input("Enter: \n 1.AddFood \n 2.EditFood \n 3.ViewFood \n 4.RemoveFood \n Enter:"))
  obj.execute(choice,operation)


