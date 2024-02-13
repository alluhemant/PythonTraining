My_list = [1, "Hi", 3.4, [1, 2, 3, 4, 5]]
print(My_list[3][-1])

l = [1, 2, [3, 4, [5, 6]]]
print(l[2][1], l[2][2][-1])

l1 = [1, 2, 3, 4]
sum_of_list = 0
for i in range(len(l1)):
    sum_of_list += l1[i]
    i += 1
print("The sum of list: ", sum_of_list)

l2 = [1, 2, 3, 4]
print(f"Reverse of the list is: ", l2[::-1])
print(f"The maximum element of list is: ", max(l2))
print(f"The minimum element of list is: ", min(l2))

l3 = [5, 6, 10, 3, 2, 1]
sorted_list = l3.sort()
print("The sorted list: ", l3)