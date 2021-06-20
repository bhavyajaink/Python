#we have a college in that different department are there so all the student have a common suject that is english so copy the name of all the departnment students and make a new list of that students
# use the copy function at here.
#to count the no student in subject english
BCA=['bhvaya','komal','khushi','akshuni','divya']
BCOM=['depanshi','dikshika','saloni','purvi']
BA=['deepali','aradhana','kmala','oreo']
e_s=BCA.copy()+BCOM.copy()+BA.copy()
print("English student :-",e_s)
count=0
for i in e_s:
    count=count+1
print("The number of student in english are:-",count)
