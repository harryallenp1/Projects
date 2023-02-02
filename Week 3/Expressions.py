#variables
num1 = 10 #int
num2 = 20 #int

sum = num1 + num2
print("sum = ", sum)

#sum of 10 and 20 is 30
print("sum of ", num1, " and ", num2, " is ", sum)

# f-strings
print(f'sum of {num1} and {num2} is {sum}')

print(f'type of num1 : {type(num1)}')
print(f'type of num2 : {type(num2)}')
print(f'type of sum : {type(sum)}')

percentage = 75.49 #float
grade = 'A-' #string
result = "Pass" #string
promoted = True #boolean

print(f'type of percentage : {type(percentage)}')
print(f'type of grade : {type(grade)}')
print(f'type of result : {type(result)}')
print(f'type of promoted : {type(promoted)}')

#ask user to input values 

#input() always gives string values
# num1 = input("Enter number 1 : ")
# num2 = input("Enter number 2 : ")

# print(f'The sum of {num1} and {num2} is {num1 + num2}')
# print(f'type of num1 : {type(num1)}')
# print(f'type of num2 : {type(num2)}')

#type casting
# num1 = int("231")
# num1 = int("hello") #ValueError

# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))

print(f'The sum of {num1} and {num2} is {num1 + num2}')
print(f'type of num1 : {type(num1)}')
print(f'type of num2 : {type(num2)}')

# percentage = float(input("Enter percentage : "))
print(f'percentage : {percentage + 2.0}  type(percentage) : {type(percentage)}')

# result = input("Enter result : ")
print(f'result : {result} type(result) : {type(result)}')

result = 10 / 3
print(f'result : {result} type(result) : {type(result)}')

# integer division using //
result = 10 // 3
print(f'result : {result} type(result) : {type(result)}')

result = 10.75 / 3.89
print(f'result : {result} type(result) : {type(result)}')

#modulo - remainder of the division using %
result = 10 % 3
print(f'result : {result} type(result) : {type(result)}')

result = ((10 / 3) * 2 + (50 / 4 - 20))
print(f'result : {result} type(result) : {type(result)}')

result = 1 #asssignment

#21 # result = result + 20
#shorthand operators
result += 20 
print(f'result : {result} type(result) : {type(result)}')

result -= 5
print(f'result : {result} type(result) : {type(result)}')

result *= 2
print(f'result : {result} type(result) : {type(result)}')

result /= 4 
print(f'result : {result} type(result) : {type(result)}')

#logical operators
# AND, OR , NOT
b1 = True
b2 = False

print(f'b1 and b2 : {b1 and b2} b1 & b2 : {b1 & b2}') #Logical AND
print(f'b1 or b2 : {b1 or b2}  b1 | b2 : {b1 | b2}') #Logical OR
print(f'not b1 : {not b1} ~b1 : {~b1}') #Logical NOT using ~ tilde
print(f'not b2 : {not b2} ~b2 : {~b2}')

#represent binary number using 0b
num1 = 0b10011001 
print(f'num1 = {num1} type(num1) : {type(num1)}')
print(f'binary representation of 67 : {bin(67)}')

myNum = 0b0000111
print(f'myNum = {myNum} type(myNum) : {type(myNum)}')
print(f'number of bits to represent 67 in binary : {int(67).bit_length()}')
print(f'number of bits to represent 44 in binary : {int(44).bit_length()}')

#relational operators
num1 = 10
num2 = 35
myNum = 5

if num1 >= 10:
    print(f'{num1} is more than or equal to 10')

if myNum == 5:
    print(f'{myNum} and 5 are equal')

if num1 % 2 == 0:
    print(f'num1 is even number')

    if num1 > 10:
        print(f'num1 is more than 10')
    elif num1 < 10:
        print(f'num1 is less than 10')
    else:
        print(f'num1 is 10')
else:
    print(f'num1 is odd number')

course1 = "PROG10004"
course2 = "MATH10025"
# course2 = "INFO10025"
course3 = "SYST10082"
# day = "Thursday"
day = "Monday"
# day = "Wednesday"

if day == "Thursday" and course1 == "PROG10004":
    print("you have session today")
elif day == "Monday" and (course2 == "MATH10025" or course3 == "PROG10009"):
    print("No session")
else:
    print("No information")
