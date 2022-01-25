#QUESTION 1
'''PERFORMING OPERATIONS ON STRINGS'''

print("\nSTRING OPERATIONS\n")

string="PYTHON IS A CASE SENSITIVE LANGUAGE"
print("THE ORIGINAL STRING IS: \"{}\"".format(string))

#PART a
length=len(string)

print("\tLENGTH OF THE GIVEN STRING:",length)

#PART b
print("\tSTRING IN REVERSED ORDER IS:\"{}\"".format(string[::-1]))

#PART c
new_string=string[10:26]

print("\tNEW STRING:\"{}\"".format(new_string))

#PART d
print("\tSTRING AFTER THE CHANGES:\"{}\"".format(string.replace("a case sensitive","object orientted")))

#PART e
print("\tINDEX OF \"a\" IN THE GIVEN STRING :", string.find("a"))

#PART f
print("\tSTRING AFER REMOVING THE WHITE SPACES:\"{}\"".format(string.replace(" ","")))






#QUESTION 2
'''PROGRAM TO DO STRING FORMATTING'''

print("\nSTRING FORMATTING\n")

name=input("ENTER YOUR NAME:")
sid=int(input("ENTER YOUR SID:"))
dept_name=input("ENTER THE NAME OF YOUR DEPARTMENT:")
cgpa=float(input("ENTER YOUR CGPA:"))

print()

#STRING FORMATTING USING .format() command.
print("Hey {0} here!!\
       \nMY SID is {1}\
       \nI am from {2} Branch and my CGPA is {3}.".format(name,sid,dept_name,cgpa))





#QUESTION 3
'''PROGRAM TO USE BITWISE OPERATORS'''

print("\nBITWISE OPERATORS\n")

a=56
b=10
print("a:",a)
print("b:",b)

print()

  #PART a
print("a&b:",a&b)

  #PART b
print("a|b:",a|b)

  #PART c
print("a^b:",a^b)

  #PART d
  #left bit shifting
print("LEFT SHIFTING BOTH a and b BY 2 BITS: a-{0},b-{1}".format(a<<2,b<<2))

  #PART e
  #right bit shifting
print("RIGHT SHIFTING a BY 2 AND b BY 4 BITS: a-{0},b-{1}".format(a>>2,b>>4))




#QUESTION 4
'''PROGRAM TO FIND THE GREATEST NUMBER'''

print("\nGREATEST NUMBER CALCULATOR\n")

num1=float(input("ENTER YOUR FIRST NUMBER:"))
num2=float(input("ENTER YOUR SECOND NUMBER:"))
num3=float(input("ENTER YOUR THIRD NUMBER:"))

#USING CONDITIONAL STATEMENTS TO COMPARE THE NUMBERS.

if (num1>=num2) and (num1>=num3):
    greatest=num1

if (num2>=num1) and (num2>=num3):
   greatest=num2

else:
    greatest=num3

#PRINTING THE GREATEST NUMBER
print("THE GREATEST OF ALL THE THREE NUMBERS IS:",greatest)




#QUESTION 5
'''PROGRAM TO COMPARE STRINGS'''

print("\nSTRING COMPARISON\n")

user_input=input("ENTER THE STRING:")

#CONDITION TO CHECK IF "name" PRESENT IN user_input
if "name" in user_input:
    print("YES")

#CONDITION TO CHECK IF "name"is not present in user_input.
else:
        print("NO")




#QUESTION 6
'''PROGRAM TO CHECK THE VALIDITY OF A TRIANGE'''

print("\nTRIANGLE VALIDITY CHECKER\n")

side1=input("ENTER THE LENGTH OF FIRST SIDE:")
side2=input("ENTER THE LENGTH OF SECOND SIDE:")
side3=input("ENTER THE LENGTH OF THE THIRD SIDE:")


#CONDITION TO CHECK IF ANY OF THE THREE LENGTHS IS GREAER THANTHE SUM OF THE OTHER TWO.
if(side1>=side2+side3) or (side2>=side1+side3) or (side3>=side2+side1):
  print("NO,TRIANGLE CANNOT BE FORMED")
else:
  print("YES,TRIANGLE CAN BE FORMED")

