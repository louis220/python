

str = "Life is too short, You need Python".lower()
str2 = str.replace(" ", "")
str3 = str2.replace(",", "")
print(str3)
lst = list(str3)
chars = set(lst)

print(chars)
lst = list(chars)
lst.sort()
print(len(lst))
