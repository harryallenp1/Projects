# List - ordered collection of multiple values of same data type

classList = [] #empty list
people = ["Mohammed", "Arjun"]

print(f'classList : {classList}')
print(f'people : {people}')
print(f'type(people) : {type(people)}')

print(f'number of elements in classList : {len(classList)}')
print(f'number of elements in people : {len(people)}')

# for adding new element in the list - append()
people.append("Liam")

people.append(829)

print(f'people : {people}')
print(f'number of elements in people : {len(people)}')

for val in people:
    print(f'val = {val} type(val) : {type(val)}')

# numbers = [1, 2, 3, 4, 5, "anything", 6, 7, "One more", 8, 9]
numbers = [1, 2, 3, 4, 5]

sum = 0

for n in numbers:
    sum += n
    # sum = sum + n

print(f'sum of numbers : {sum}')

print(f'classList : {classList}')
print(f'people : {people}')

classList.append("Harry")
classList.append("Frederik")
classList.append("Aryana")
print(f'classList : {classList}')

#index

#    0         1           2
# ['Harry', 'Frederik', 'Aryana']
print(f'classList[2] : {classList[2]}') #aryana
print(f'classList[0] : {classList[0]}') #Harry
# print(f'classList[5] : {classList[5]}') #IndexError: list index out of range

# classList[3] = "Sekun" #IndexError
# print(f'classList[3] : {classList[3]}')

classList.append("SomeOne")
print(f'classList[3] : {classList[3]}')

classList[3] = "Sekun"
print(f'classList[3] : {classList[3]}')

#appends a new element at the end of list
classList.append("Patience")
classList.append("Robert")
classList.append("Essa")
classList.append("Hussain")
classList.append("Faseyi")

print(f'classList : {classList}')

#will only process starting index 2 and ending at 6 (exclude 7)
for name in classList[2:7]:
    print(f'{name} is present')

print("ClassList[5:14]-----------------")
for name in classList[5:14]:
    print(f'{name} is present')

print("ClassList[5:2]-----------------")
#for range, lower bound must be less than upperbound
for name in classList[5:2]:
    print(f'{name} is present')

print("ClassList[5:2:-1]-----------------")
#processes the list in reverse direction
for name in classList[5:2:-1]:
    print(f'{name} is present')

people.append("Digaant")
people.append("Jay")
people.append("Julius")

for idx in range(0, 6):
    print(f'idx : {idx} people[idx] : {people[idx]} --- classList[idx] : {classList[idx]}')

print(f'people : {len(people)}')
print("reverse range -----------------------------------------")
# range(lowerbound , upperbound, step)
# for idx in range(8, 2, -1):

# len(people) - 1 = 6
for idx in range(len(people)-1, 2, -1):
    print(f'idx : {idx} people[idx] : {people[idx]} --- classList[idx] : {classList[idx]}')

print(f'last element in classList : {classList[len(classList)-1]}')
print(f'last element in people : {people[len(people)-1]}')

# while True:
#     name = input("Enter the name to add to the list ['STOP' to finish] : ")

#     if name.upper() == "STOP":
#         break

#     classList.append(name)
#     print(f'within classList : {classList}')

# print(f'after loop classList : {classList}')

#task
#ask user to provide number, append the number to the list
#until user inputs 0 (zero)

numbers = [10, 20, 30]
print(f'numbers : {numbers}')

# while True:
#     num = int(input('enter number : [0 to stop] : '))

#     if num == 0:
#         break

#     numbers.append(num)

# print(f'numbers : {numbers}')

print(f'classList : {classList}')
print(f'people : {people}')

# classList.append(people)

for person in people:
    classList.append(person)

print(f'classList : {classList}')
print(f'classList length : {len(classList)}')

#remove element from list
classList.remove(829)

print(f'classList : {classList}')
print(f'classList length : {len(classList)}')

nameToDelete = "Puneet"

#check is the element is present in the list
# if nameToDelete in classList:
#     classList.remove(nameToDelete)
# else:
#     print(f'{nameToDelete} is not present in the list')

if nameToDelete not in classList:
    print(f'{nameToDelete} is not present in the list')
else:
    classList.remove(nameToDelete)

print(f'classList : {classList}')
print(f'classList length : {len(classList)}')

#insert() - to add the element at a specific index
classList.insert(2, "Puneet")
print(f'classList : {classList}')

classList.insert(0, "bright")
print(f'classList : {classList}')
print(f'classList length : {len(classList)}')

#remove the last element from list - pop()
classList.pop()
print(f'classList : {classList}')
print(f'classList length : {len(classList)}')

#remove the element from specified index list - pop(index)
classList.pop(5)
print(f'classList : {classList}')
print(f'classList length : {len(classList)}')

classList.sort()
print(f'classList : {classList}')

classList.insert(4, "pawan")
print(f'classList : {classList}')

classList.sort()
print(f'classList : {classList}')

classList.reverse()
print(f'classList.reverse() : {classList}')

numbers = [8, 2, -1, 66, -23, 54, 23, 7, -78]
numbers.sort()
print(f'numbers : {numbers}')

numbers.reverse()
print(f'numbers reverse : {numbers}')


print(f'max element of numbers : {max(numbers)}')
print(f'min element of numbers : {min(numbers)}')
print(f'max element of classList : {max(classList)}')
print(f'min element of classList : {min(classList)}')