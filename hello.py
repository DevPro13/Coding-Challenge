
def add_stu_name_and_grade():
	lst=[]
	while True:
		stu_data=[]
		print('Please..enter q to quit!!!')
		name=input("Enter student name: ")
		if name=='q':
			break

		stu_data.append(name)
		mark=float(input('Enter student obtained marks: '))
		stu_data.append(mark)
		lst.append(stu_data)
	print("Inputted list of students name and their obtained marks are::{0}".format(lst))
	return lst

#-----------------------------------------------------------------------------------------
def order_marks():
	lst=add_stu_name_and_grade()
	"""sorting the list according to question and generating the output"""
	for i in range(len(lst)):
		for j in range(i+1,len(lst),1):
			if lst[i][1]>lst[j][1]:
				temp=lst[j]
				lst[j]=lst[i]
				lst[i]=temp
	print("sorted list:::{}".format(lst))
	print('----------------------------The required outputs:--------------------------------------------------')
	if lst[1][1]!=lst[2][1]:
		print(lst[1][0])
		print("Which is required name..")
	else:
		l=[lst[a][0] for a in range(1,len(lst)) if lst[1][1] in lst[a]]
		for m in range(len(l)):
			for n in range(m+1,len(l)):
				if l[m]>l[n]:
					temp=l[n]
					l[n]=l[m]
					l[m]=temp
		for i in l:
			print(i)
	    print("These are required names..")
		


order_marks()




