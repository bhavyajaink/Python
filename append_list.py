#write the program to take a number from user
#Append:- it is use to add the element in the list
l=list()
num=int(input("enter the number of input u want to given"))
for i in range(0,num+1):
    # nu take the input from user and add to the list
    nu=input("enter the number or string that u want to enter at position {}:-".format(i+1))
   l.append(nu)
print("the list of item are:-")
print(l)
