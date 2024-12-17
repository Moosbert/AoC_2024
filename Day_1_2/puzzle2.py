list1 = []
list2 = []

def sort_list(list):
    return sorted(list)

with open('C:\Sandboxes\AoC_2024\Day_1_1\input1.txt') as f:
    for line in f:
        #append first 5 characters of the line to the list
        list1.append(int(line[:5]))
        #append last 5 characters of the line to the list
        list2.append(int(line[-6:]))

#sort the list
list1 = sort_list(list1)
list2 = sort_list(list2)

print(list1)
print(list2)

sum = 0

for val1 in list1:
    # find how often val1 is in list2
    count = list2.count(val1)
    sum += val1 * count

print(sum)
        