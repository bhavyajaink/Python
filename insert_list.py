#to take index values from user and insert the new element at that place
fr=['bhvaya','komal','khushi','akshuni','divya']
print('before the insert operation of fr value are:=',fr)
i,e=input('enter the index value and element of that place that you want to insert').split()
i=int(i)
fr[i]=e
print('after the insert opertion of fr value are:=',fr)
