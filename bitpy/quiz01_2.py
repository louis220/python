lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = lst[3:7]
print(lst2)
lst2.reverse()
lst[3:7] = lst2
print(lst)
