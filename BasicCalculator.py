import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="mysql",
  database="calc"
)
mycursor = mydb.cursor()

class calculator:
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def multiply(x,y):
        return x*y
    def divide(x,y):
        return x/y
    
    in_calc = True
    while in_calc:
        choice=input("What you want to do?\n1.Add (+)\n2.Sub (-)\n3.Multiply (*)\n4.Divide (/)\n")
        
        if choice == '+' or choice == '-' or choice == '*' or choice == '/':
            a=float(input("Please Enter Your 1st No: "))
            b=float(input("Please Enter Your 2nd No: "))
        if choice == '+':
            result = add(a,b)
            print("Addision of both no : ", result)
        elif choice == '-':
            result = sub(a,b)
            print("Subtraction of both no : ", result)    
        elif choice == '*':
            result = multiply(a,b)
            print("Multiplication of both no : ", result)   
        elif choice == '/':
            result = divide(a,b)
            print("Division of both no : ", result)  
        elif choice != '+' or choice != '-' or choice != '*' or choice != '/':
            in_calc = False
            print("Wrong input, Calc closed.")
            break
        insertValues = 'INSERT INTO calchistory (conditions, firstNo, secondNo, result) VALUES ("'+str(choice)+'","'+str(a)+'","'+str(b)+'","'+str(result)+'")'     
        mycursor.execute(insertValues)
        mydb.commit()
                
calculator()

