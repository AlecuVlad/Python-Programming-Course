# var = 'Ana are mere'
# for item, value in enumerate(var):
#     print(f'{item} -> {value}')

#==================================================

myList = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6 ]

#==================================================

ascendingList = list(myList)
ascendingList.sort()

descendingList = list(myList)
descendingList.sort(reverse=True)

print(f'Original list: {myList}')
print(f'Ascending order: {ascendingList}')
print(f'Descending order: {descendingList}')

#==================================================

print(f'Even numbers: {ascendingList[1::2]}')

print(f'Odd numbers: {ascendingList[::2]}')

#==================================================

result_multiple_of_3 = []
for val in myList:
    if val % 3 == 0:
        result_multiple_of_3.append(val)

print(f'Multiples of 3: {result_multiple_of_3}')

#==================================================
