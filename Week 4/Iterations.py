#conditional loops

count = 0
# iteration variable
while count <= 5:
    #body of the loop
    print(count)
    count += 2

print("the loop is termiated")
print(f'count : {count}')

#infinite loop
# count = 1
# while count < 5:
#     print(f'count within Loop : {count}')
#     # count -= 1

#ctrl+ c to stop program execution

num1 = 10
num2 = 20

#write a conditional loop to execute 
# as long as the num1 is less than num2
# within loop, change the value of num2 to decrement by 2

while num1 < num2:
    num2 -= 2
    num1 += 2
    print(f'num1 = {num1} num2 = {num2}')

print("loop terminated")

#counted loops

#0, 1, 2, 3, 4
for n in range(5):
    #print("hello")
    print(f'n = {n}')

print("for loop 1 terminated")

for n in range(10):
    print(f' 4 * {n + 1} = {4 * (n + 1)}')

print("for loop 2 terminated")

#list
for name in ["James", "Jack", "Ken", "Mark", "Leo", "Nick"]:
    print(f'hey {name}')

print("for loop 3 terminated")

#list of integers
numbers = [12, 24, 35, 46, 57, 68, 79, 80]

for num in numbers:
    print(f' num * 2 = {num * 2}')

print("for loop 4 terminated")
print(f'numbers : {numbers}')

# for ch in "This is a hello message":
message = "This is a hello message"

# for ch in message:
for ch in message[6:18]:
    print(f'ch = {ch}')

print("for loop 5 terminated")

for n in range(5, 10):
    print(f'n = {n}')
    
print("for loop 6 terminated")

for n in range(15, 10, -2):
    print(f'n = {n}')
    
print("for loop 7 terminated")

for _ in range(4):
    print("hello")

print("for loop 8 terminated")

#0, 1, 2, 3, 4, 5, 6
for day in range(7):
    if day == 0:
        print(f'day {day} is holiday')
    elif day >= 1 and day <= 5:
        print(f'day {day} is a work/study day')
    else:
        #day = 6
        print(f'day {day} is a party day')

print("for loop 9 terminated")

#break
#continue

for n in range(10):
    print(f'n = {n}')
    
    if n > 5:
        break #terminates the loop and skips remaining statements in loop

    print("still within for loop")

print("for loop 10 terminated")

#loop to print only for even numbers between 0 to 9
#logical error
for n in range(10):
    if n % 2 != 0: #odd number
        continue
    #skips the remaining statements in the loop and 
    # jumps to next iteration

    print(f'n = {n}')
    # print("still within for loop")

print("for loop 11 terminated")

#nested loops
for row in range(5): #outer loop
    print(f'row = {row}')

    for col in range(3): #inner or nested loop
        print(f'col = {col}', end=" ")
        print("printing from inner loop")

    print("printing from outer loop")

print("after nested loops 1")

#nested loops 2
for n in range(5):
    print(f'n = {n}')

    x = n + 1
    while x < 10:
        print(f'{x}', end = " - ")
        x += 2

    print()

print("nested loop 2 ends")

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# num = 5
num = int(input("enter value for num : "))

for i in range(num):
    print()
    for j in range(i+1):
        print(f'{j+1}', end = " ")