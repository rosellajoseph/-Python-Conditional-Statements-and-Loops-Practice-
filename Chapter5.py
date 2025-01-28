cars = ['audi', 'BMw', 'subaru', 'toyota']
for car in cars:
  if car == 'BMw':
    print(car.lower())
  else:
    print(car.title())
#tests for equal
  print("Is car == 'subaru'? I predict True.")
  print(car == 'subaru'+ "\n")
#Numerical tests for equality
numbers= [1,2,3,4,5]
for number in numbers:
  if number == 3:
    print(number)
#Multiple Conditions
age_0= 18
age_1= 21
print(age_0>18 and age_1>18)
# SIMPLE IF STATMENTS
age = 19
if age >= 18:
  print("You are old enough to vote!")
  print("Have you registered to vote yet?")
  #If else Statements
age = 17
if age >= 18:
  print("You are old enough to vote!")
  print("Have you registered to vote yet?")
else:
  print("Sorry, you are too young to vote.")
  print("Please register to vote as soon as you turn 18!")


