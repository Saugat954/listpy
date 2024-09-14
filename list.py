#list of numbers
number = [1,2,3,4,5,6]
print(number)
#it prints the whole list

#it prints the type of list
print(type(number))

#list can store any data type

newList=[True, 1,5,"Saugat", "Subedi"]
print(type(newList[0]))

print(newList)


#search in list
color=["RED","Blue", "Green","Purple","Yellow","SkyBlue","Orange","White"]
if "Blue" in color:
    print("Blue is present in color")
else:
    print("Blue is not Present")
#it prints from 1 to 7 skipping one after one
print(color[1:8:2])

number=[ i*i for i in range(10)]
print(number)
'''When i = 0, i * i results in 0 * 0 = 0
When i = 1, i * i results in 1 * 1 = 1
When i = 2, i * i results in 2 * 2 = 4
And so on, until i = 9, which results in 9 * 9 = 81.'''