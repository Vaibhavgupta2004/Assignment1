#Assignment 1

print("Question 1")

#Program to Calculate Average
print("Average Calculator")

#Taking input of three Numbers
num1 = float(input("1st Number :"))
num2 = float(input("2nd Number :"))
num3 = float(input("3rd Number :"))

#Calculating Average
Average=(num1+num2+num3)/3

#Printing The Average Value
print("\nThe Average of Three Number is:", Average)

print()


print("Question2\n")

#Program to Calculate Tax 
print("Income Tax Calculator")

#Taking the input of gross income and Number of dependents
Gross_income = int(input("Enter your Gross Income:"))
No_of_dependents = int(input("enter your Number of dependents:"))

#Calculating Taxable Income and Total Tax
taxable_income = Gross_income-10000-((No_of_dependents)*3000)
tax = taxable_income*20/100

#Printing Total Tax
print("\nYour total income tax is:",tax)

print("Question 3")

#Information of some students
student1_info = ['21104073' , 'Vaibhav Gupta' , 'M' , ' EE' , 9.8]
student2_info = ['21104101' , 'Sarthak Garg' , 'M' , 'EE' , 9.6 ]
student3_info = ['21104201' , 'Anushka' , 'F' , ' EE' , 9.4]

#Displaying student info in list form.
print(student1_info)
print(student2_info)
print(student3_info)

print("Question 4")

#Floating input from User
marks_1 =  float (input("Enter 1st marks: " ) )
marks_2 = float (input("Enter 2nd marks: ") )
marks_3 = float (input ("Enter 3rd marks: " ) )
marks_4 = float (input("Enter 4th marks: " ) )
marks_5 = float (input ("Enter 5th marks:" ) )

#Assigning marks into list and sorting them in increasing order.

listt = [marks_1 , marks_2 , marks_3, marks_4 ,marks_5]
print(sorted (listt))

print("Question 5")

colours = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Part a) Remove black string in list and display remaining list
colours.pop (3)
print("After deleting 4th colour, list is :" , colours)

#Part b Replacing 'pink' color by 'purple.
colours[3] = 'Purple'
print (colours)