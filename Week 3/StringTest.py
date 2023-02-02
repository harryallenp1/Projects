day = "Thursday"
print(f'day : {day}')

day += " not a weekend"
print(f'day : {day}')

day = "Wednesday" + " Adams"
print(f'day : {day}')

cheers = "-~*" * 20
print(f'cheers : {cheers}')

cheers = "Hey, ThatS PRetty coOL !"
print(f'cheers : {cheers}')
print(f'cheers.upper() : {cheers.upper()}')
print(f'cheers.lower() : {cheers.lower()}')
print(f'cheers.capitalize() : {cheers.capitalize()}')
print(f'cheers.swapcase() : {cheers.swapcase()}')

print(f'number of characters in cheers : {len(cheers)}')

for ch in cheers:
    print(ch)

print(f'number of time letter t occurs : {cheers.count("t")} ')
print(f'number of time letter o occurs : {cheers.count("o")} ')

cheers = "Hey, thats pretty cool !"
#find() returns the index/position of the word/search string if found in the string
#if not found, returns -1
print(f'cheers contains word cool or not ? {cheers.find("cool")}') 
print(f'cheers contains word cold or not ? {cheers.find("cold")}')
print(f'cheers contains word Hey or not ? {cheers.find("Hey")}')

searchString = "cold"
index = cheers.find(searchString)

if index == -1:
    print(f'{searchString} is not present in string cheers')
else:
    print(f'{searchString} is present in string cheers at index {index}')

searchString = "cool"
if searchString in cheers:
    print(f'{searchString} is present in string cheers')
else:
    print(f'{searchString} is not present in string cheers')

cheers = "Hey, thats pretty cool !"
words = cheers.split()

print(f'words : {words}')
print(f'len(words) : {len(words)}')
print(f'type(words) : {type(words)}')

for ch in cheers:
    print(f'ch : {ch} isupper : {ch.isupper()} isdigit : {ch.isdigit()} isalnum : {ch.isalnum()}')

password = "Its&26"

#task: ask the user to enter a string for password 
#check and display if the given password is valid as per the following constraints or not
# more than 5 characters
# at least 1 uppercase letter
# at least 1 lowecase letter
# at least 1 special character
# at least 1 digit