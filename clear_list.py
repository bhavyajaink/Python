#write the program to take a number from user and ask that they added the data is correct or they want to do changes?
#clear:- it is use to add the element in the list
l=list()
while True:
    num=int(input("enter the number of input u want to given:-"))
    for i in range(0,num+1):
    # nu take the input from user and add to the list
       nu=input("enter the number or string that u want to enter at position {}:-".format(i+1))
       l.append(nu)
    print("the list of item are:-")
    print(l)
   #To check wheather a enter data by user is correct or not
    a=int(input("if enter data by you is not correct then press 1....if enter the data by you is correct than press any number"))
    if a==1:
       print("the data by you enter is not correct so u again enter the data")
       #clear function is at here to clear the data by user
       l.clear()
       continue
    else:
       print("The data is enter by you is correct")
       break
       

