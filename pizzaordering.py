print("welcome to the sip pizza store")
orderpizza = input (" what type of pizza u want ? small, medium , large ")
pepperoni = input (" do u want to add a pepperoni in ur pizza? y or n : ")
extra_cheese = input (" do u want extra cheese? y or n: ")
bill = 0 
small = 15
medium = 20
large = 25 
if orderpizza == small : 
      bill += 15 
elif orderpizza == medium :
      bill += 20
elif orderpizza == large :
    bill += 25
else:
     print (" u type the wrong input ")

# adding some extra 

if pepperoni == "y":
     if orderpizza == "small":
          bill +=2
     else:
          bill += 3

if extra_cheese == "y":
         bill += 1 

print (f"your final bill is {bill}")