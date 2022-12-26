#exo1 
firstName = 'Mario'
print(firstName)

#exo2
age = 25
print(age)

#exo3
sentence = 'hello, i\'m Mario!'
print(sentence)

#exo4
amount = 1.3
print(float(amount))

#exo5
a= 1
b= 2-1
c= 10-9
bool(a==b==c)

#exo6
myfirst_Name = 'Mario'

#exo7
"Hi, my name is John Doe"
'python'

#exo8
a= 2
b= 3
c= 10
a + b
print(a,b,c)

#exo9
a = 12
b = 'Hello'
c= a
a=b
b=c
print(a, b)

#exo10
a= 'strong'
b= 'weak'
c= 'Algeria'
print(len(a))
print(len(b))
print(len(c))

#exo11
a = 'hello' #capitalize
print(a.capitalize())
b = 'tom' #uppercase
print(b.upper())
c = 'LAURA' #lowercase
print(c.lower())
question = 'How are you' #change o in e
print(question.replace('a','e'))
age_question = 'How old are you?' #use the correct method to create a string for each word
print(age_question.split(' '))
print(a, b, c, question, age_question)

#exo12
name= 'Amine'
age= '25'
hello = f'Hello, {name}. You are {age}'
print(hello)

#Operators
#exo 1
a = True
b= False
print(False and True) # Should print False

#exo 2
print(False or (0 != 0 or True)) # Should print True

#exo 3
5 % 2

#exo4
print(not ("testing" == "testing" and "Mario" == "Cool Guy")) # Should print True

#exo5
firstName = "Mario"
lastName = "Rossi"

sentence =  firstName + lastName

print(sentence) # Should print "Mario Rossi"

#exo6
brands = ["Adidas", "Nike"]

print("Nike" in brands) # Should print True

#exo7
brands = ["Adidas", "Nike"]

print("Reebok" not in brands) # Should print True

#methods
#exo1
print(type("Hello World"))
print(type(True))
print(type(False))
print(type(33))
print(type(24.5))
print(type(4+1j))
print(type(4j))
print(type(["lion", "monkey", "dog","fish"]))
print(type(("lion", "monkey", "dog","fish")))
print(type({"name" : "John", "surname" : "Doe", "age":22}))
print(type({"lion", "monkey", "dog","fish"}))
#exo2
num1 = 1.3
num1 = float(num1)
print(float(num1))
print(type(num1))
num2 = 2.3
num2 = int(num2)
print(int(num2))
print(type(num2))
num3 = 1j 
num3 = complex(num3)
print(complex(num3))
print(type(num3))
num4 = 1.4 
num4 = round(num4)
print(round(num4))
print(type(num4))
num5 = 1.5
num5 = round(num5)
print(round(num5))
print(type(num5))
#exo3
