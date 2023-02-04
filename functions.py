# # exo1
# i = 1
# while i < 6:
#     print("*"*i)
#     i= i + 1

# #exo2
# for i in range(1,6):
#     if i%2 == 0:
#         print('')
#     else:
#         print(i*'*')

# #exo3
# todo = ["exercise1", "exercise2", "exercise3","coffee break", "exercise4","exercise5","exercise6"]
# for x in todo:
#     if x.lower == "COFFEE BREAK":
#         break
#     print(x)
        
# #exo4
list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for i in list1, tuple, set1:
    print(i)
for i, j in dict1.items():
    if j == 'land':
        print(i)


