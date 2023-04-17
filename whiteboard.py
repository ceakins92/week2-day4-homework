# Write a function that takes two inputted lists of equal length and combines them into a single list by alternating elements. For example:
# Given list1 = [1, 2, 3] and list2 = ['a', 'b', 'c']
# The function should  return exactly this --->  [1, 'a', 2, 'b', 3, 'c'].


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']


def comb_list(l1, l2):
    list3 = []
    for i in range(len(l1)):
        print(i)
        list3.append(l1[i])
        list3.append(l2[i])

    return list3


print(comb_list([1, 2, 3], ['a', 'b', 'c']))
print(comb_list([10, 11], [13, 14]))
