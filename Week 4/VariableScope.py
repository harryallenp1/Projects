x = 10

for i in range(5):
    y = i * 2
    print(f'i = {i}')
    print(f' x = {x} y = {y}')

print("after for loop")
print(f'i = {i}')
print(f' x = {x}  y = {y}')

x = 10 #global variable - available throughout program execution

def printNumber():
    z = x * 3 
    #local variable - only available during function execution
    #only available within the block(scope) they are declared in
    print(f'x = {x} z = {z}')

#call the function
printNumber()

print("after calling function")
# print(f'x = {x} z = {z}') 
#NameError as z is local variable within function; 
# not available outside function

print(f'x = {x}')