# exo1
i = 1
while i < 6:
    print("*"*i)
    i= i + 1

#exo2
for i in range(1,6):
    if i%2 == 0:
        print('')
    else:
        print(i*'*')

#exo3
todo = ["exercise1", "exercise2", "exercise3","coffee break", "exercise4","exercise5","exercise6"]
for x in todo:
    if x.lower == "COFFEE BREAK":
        break
    print(x)
        
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

# exo5
list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}

#1 
print("Length of list1:", len(list1))
print("Length of tuple1:", len(tuple1))
print("Length of set1:", len(set1))
print("Length of dict1:", len(dict1))
#2
print("First element of list1:", list1[0])
print("First element of tuple1:", tuple1[0])
#3
print("Value of lion key in dict1:", dict1["lion"])
# change the 2nd position element of list1 to "rabbit"
list1[1] = "rabbit"
print("Updated list1:", list1)
# try to change the 2nd position element of the tuple to "rabbit" and explain what happened
try:
    tuple1[1] = "rabbit"
except TypeError:
    print("Tuples are immutable and cannot be changed once defined.")
# add "monkey" to list1
list1.append("monkey")
print("Updated list1:", list1)
# remove "rabbit" from list1
list1.remove("rabbit")
print("Updated list1:", list1)
# in dict1 the number of feet is written as value to each animal the fish has wrong value just fix it.
dict1["fish"] = 2
print("Updated dict1:", dict1)
      
#exo6
def goodbye():
    print('good bye')
goodbye()

#exo 7
def goodbye(name):
    print(f"Good bye {name}")
goodbye('Adam')

#exo8
import os
user = os.getlogin()
print(user)

#exo9
def greet_family(name="John", surname="Doe", family=[]):
    print(f"Hello {name} {surname}!")
    for member in family:
        print(f"Hello {member[0]} {member[1]}!")

family_members = [("Tristram", "Mcbride"), ("Baldwin", "Preston"), ("Wally", "Collins")]
greet_family(family=family_members)

#exo10
import random
def random_list_summer(n=15, min_value=-100, max_value=100):
    numbers = [random.randint(min_value, max_value) for i in range(n)]
    print("List: ", numbers)
    print("Sum: ", sum(numbers))
random_list_summer()