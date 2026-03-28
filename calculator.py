
a1 = int(input("Enter the First number: "))
b1 =int(input("Enter the second Number: "))
def add(a ,b):
      return int(a +b)

def sub(a,b):
     return int(a -b)

def mul(a,b):
    return int(a*b)

def div(a,b):
    return int(a/b)

ask = input("Enter What do want to do + , / , * or -")
if ask == '+':
   print(add(a1,b1))
  
if ask== '-':
    print(sub(a1,b1))
       

if ask == '*':
   print(mul(a1,b1))
  
if ask== '/':
    print(div(a1,b1))
       

