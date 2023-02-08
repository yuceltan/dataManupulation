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
        
# # #exo4
# list1 = ["lion", "monkey", "dog","fish"]
# tuple1 = ("lion", "monkey", "dog","fish")
# set1 = {"lion", "monkey", "dog","fish"}
# dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

# for i in list1, tuple, set1:
#     print(i)
# for i, j in dict1.items():
#     if j == 'land':
#         print(i)

# # exo5
# list1 = ["lion", "monkey", "dog","fish"]
# tuple1 = ("lion", "monkey", "dog","fish")
# set1 = {"lion", "monkey", "dog","fish"}
# dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}

# #1 
# print("Length of list1:", len(list1))
# print("Length of tuple1:", len(tuple1))
# print("Length of set1:", len(set1))
# print("Length of dict1:", len(dict1))
# #2
# print("First element of list1:", list1[0])
# print("First element of tuple1:", tuple1[0])
# #3
# print("Value of lion key in dict1:", dict1["lion"])
# # change the 2nd position element of list1 to "rabbit"
# list1[1] = "rabbit"
# print("Updated list1:", list1)
# # try to change the 2nd position element of the tuple to "rabbit" and explain what happened
# try:
#     tuple1[1] = "rabbit"
# except TypeError:
#     print("Tuples are immutable and cannot be changed once defined.")
# # add "monkey" to list1
# list1.append("monkey")
# print("Updated list1:", list1)
# # remove "rabbit" from list1
# list1.remove("rabbit")
# print("Updated list1:", list1)
# # in dict1 the number of feet is written as value to each animal the fish has wrong value just fix it.
# dict1["fish"] = 2
# print("Updated dict1:", dict1)
      
# #exo6
# def goodbye():
#     print('good bye')
# goodbye()

# #exo 7
# def goodbye(name):
#     print(f"Good bye {name}")
# goodbye('Adam')

# #exo8
# import os
# user = os.getlogin()
# print(user)

# #exo9
# def greet_family(name="John", surname="Doe", family=[]):
#     print(f"Hello {name} {surname}!")
#     for member in family:
#         print(f"Hello {member[0]} {member[1]}!")

# family_members = [("Tristram", "Mcbride"), ("Baldwin", "Preston"), ("Wally", "Collins")]
# greet_family(family=family_members)

# #exo10
# import random
# def random_list_summer(n=15, min_value=-100, max_value=100):
#     numbers = [random.randint(min_value, max_value) for i in range(n)]
#     print("List: ", numbers)
#     print("Sum: ", sum(numbers))
# random_list_summer()

# #exo11
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# for i in range(5):
#     print(fibonacci(i))

# #exo12
# numbers = [1, 2, 3, 4, 5, 6]
# result = list(map(lambda x: x**2 
#                   if x % 2 == 0 
#                   else x, numbers))
# print(result)

##OBBJECTS
#Exo1
# class Animal:
#     def __init__(self, legs):
#         self.legs = legs
#         print("Animal object was created")
        
#     def run(self):
#         print("Running started")

# animal = Animal(4)
# animal.run()


#exo2
# class Animal:
#     def __init__(self, legs):
#         self.legs = legs
#         print("Animal object was created")
        
#     def run(self):
#         print("Running started")
        
#     def count_legs(self):
#         print("Number of legs:", self.legs)
        
#     def return_legs(self):
#         return self.legs

# animal = Animal(4)
# animal.run()
# animal.count_legs()
# number_of_legs = animal.return_legs()
# print("Number of legs:", number_of_legs)

#exo3
class Animal:
    def __init__(self, leg_count):
        self._leg_count = leg_count
        print("Animal object was created.")

    def run(self):
        print("Running started.")

    def count_legs(self):
        print("Number of legs:", self._leg_count)

    def return_legs(self):
        return self._leg_count

    def get_leg_count(self):
        return self._leg_count

animal = Animal(4)
animal.run()
animal.count_legs()
legs = animal.return_legs()
print("Number of legs:", legs)
print("Number of legs (using get_leg_count method):", animal.get_leg_count())
