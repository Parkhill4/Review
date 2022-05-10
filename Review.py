"""
        Review Code
"""
#Question 1:: Only using “for” loop print the following (Do not use decision structure in the loop):
#1. All even numbers from 2 to 50 including 2 and 50
#2. All odd number from 1 to 49 including 1 and 49
"""
list = []
listEven = []
listOdd = []
num = 0
for i in range(1, 51):
    list.append(i)

for num in range (0, len(list)):
    if list[num] % 2 == 0:
        listEven.append(list[num])
    else:
        listOdd.append(list[num])

print(list)
print(listEven)
print(listOdd)
"""

#Question 2:Using random, generate a list for 20 numbers.
#2. Sort the list, and reverse the list generated in Question 2, part 1.
#3. Using random create a three-dimensional list. No specific dimension is required.
#[Hint: Use Try/except when ever required]
"""
import random
list = []
for i in range(0,20):
    num = random.randint(1, 21)
    list.append(num)
    list.sort()
print(list)
"""

#Question 3:
"""
Using dictionary create three student, and store six course points of range [0,100].
Use any random name, and any random number between 0 to 100 for the course. Please
remember each student should have six courses.
[Hint: Use name as key and courses points as values]
[Hint: Use Try/except when ever required]
class clothes():
    def __init__(self, Desc, Units, Price):
        self.__Desc = Desc
        self.__Units = Units
        self.__Price = Price

    def set_Desc(self, color):
        self.__Desc = Desc


    def set_Units(self, Units):
        self.__Units = Units


    def set_Price(self, Price):
        self.__Price = Price
        print(self.__Price)

    def get_Desc(self):
        return self.__Desc

    def get_Units(self):
        return self.__Units
    def get_Price(self):
        return self.__Price

j = clothes("Jacket", 40, 59.95)
d = clothes("Designer Jeans", 100, 34.95)
s = clothes("Shirt", 200, 24.95)

j.set_Desc("Jacket")
j.set_Units("40")
j.set_Price("59.95")
d.set_Desc("Designer Jeans")
d.set_Units("100")
d.set_Price("34.95")
s.set_Desc("Shirt")
s.set_Units("200")
s.set_Price("24.95")

print(j.get_Desc())
print(j.get_Units())
print(j.get_Price())
"""
#Question 4:: There are three seating categories at a stadium. Type A seats cost $20, Type B seats
#cost $15, Type C seats costs $10. Write a method that asks how many tickets for each type of
#seats were sold, then display the amount of income generated from ticket sales. Use try/except
#block when required. Except should have exception, generic exception will not be accepted.
"""
A = 20
B = 15
C = 10
try:
    def main():
        aSold = int(input("How many Type A seats were sold?:"))
        bSold = int(input("How many Type B seats were sold?:"))
        cSold = int(input("How many Type C seats were sold?:"))
        aRev = A * aSold
        bRev = B * bSold
        cRev = C * cSold
        total = aRev + bRev + cRev
        print("The total revenue from tickets is $", total)
    main()
except ValueError:
    print('Please enter an integer value')
"""
#Question 5:Design a function that accepts a list as an argument and returns the second-largest
#value in the list. The function should use recursion to find the second-largest number. The list
#does not have repetitive number.
#[Hint: check for all test cases that may occur]
"""
def main():
    list = []
    num = 0
    for i in range(1, 50):
        list.append(i)
    print("The second largest value is", list[len(list) - 1])
main()
"""
#Question 6:Write a class to hold following information. All the attributes should be private. Print all
#the information or data.

class Clothes(object):
    def __init__(self, name):
        self.name = name

    def isEmployed(self):
        return False

#Question 7:: Request the user to provide an input
#1. If only integer number are entered, save the number to a variable and print the variable
#out.
#2. If only alphabets or characters (including spaces) are entered:
#a. Remove any empty space at the start of the string
#b. Remove any empty space at the end of the string.
#c. Convert the string to upper case.
#d. Count number of ‘t’ or ‘T’ entered in the string.
#[Hint: Use Try/except when ever required]

"""
def main():
    user = (input("Please enter an input: "))
    if(user.isdigit() == True):
        print(user)
    else:
        count = 0
        for i in range(len(user)):
            if(user[i] == 't' or user[i] == 'T'):
                count = count + 1
        print(user.upper())
        print("The number of T's is:", count)
main()
"""
#Question 8:: Create two sets, first set holds [1, 2, 3, 4, 5] and second set will hold [ 3, 4, 5, 6, 7, 8].
#Find the following:
#1. Union of set 1 with set 2
#2. Intersection of set 2 with set 1
#[Hint: Use Try/except when ever required]
"""
set_1 = set([1,2,3,4,5])
set_2 = set([3,4,5,6,7,8])
set_3 = set_1.union(set_2)
set_4 = set_1.intersection(set_2)
print(set_3)
print(set_4)
"""


###Assignment 1 Questions###

#Question 1
"""
Personal Information Write a program that displays the following information: Your
name Your address, with city, state, and ZIP Your telephone number Your college major

name = "Ethan Parkhill"
city = "Beeville, TX 78102"
phone = "254-315-1012"
major = "Cyber Security"

print(name, city, phone, major)
"""

#Question 2
"""
Land Calculation One acre of land is equivalent to 43,560 square feet. Write a program
that asks the user to enter the total square feet in a tract of land and calculates the
number of acres in the tract. Hint: Divide the amount entered by 43,560 to get the
number of acres.

Acre = 43560
userInput = int(input("Enter the total square feet of a tract of land: "))
calcAcres = userInput/Acre
print("There are:", calcAcres, "acres")
"""

#Question 3
"""
Distance Traveled Assuming there are no accidents or delays, the distance that a car
travels down the interstate can be calculated with the following formula:
Distance=Speed × Time
A car is traveling at 70 miles per hour. Write a program that displays the following:
a. The distance the car will travel in 6 hours
b. The distance the car will travel in 10 hours
c. The distance the car will travel in 15 hours

mph = 70
print("A. The distance the car travels in 6 hours is:", mph*6, "miles")
print("B. The distance the car travels in 10 hours is:", mph*10, "miles")
print("C. The distance the car travels in 15 hours is:", mph*15, "miles")

"""

#Question 4
"""
Age Classifier
Write a program that asks the user to enter a person’s age. The program should display
a message indicating whether the person is an infant, a child, a teenager, or an adult.
Following are the guidelines:
• If the person is 1 year old or less, he or she is an infant.
• If the person is older than 1 year, but younger than 13 years, he or she is a child.
• If the person is at least 13 years old, but less than 20 years old, he or she is a
teenager.
• If the person is at least 20 years old, he or she is an adult.

userAge = int(input("Enter your age: "))
if userAge <= 1:
    print("You are an infant")
if userAge > 1 and userAge < 13:
    print("You are a child")
if userAge >= 13 and userAge < 20:
    print("You are a teenager")
if userAge >= 20:
    print("You are an adult")
"""

#Question 5
"""
Create a change-counting game that gets the user to enter the number of coins required
to make exactly one dollar. The program should prompt the user to enter the number of
pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to
one dollar, the program should congratulate the user for winning the game. Otherwise,
the program should display a message indicating whether the amount entered was more
than or less than one dollar.

#Each letter corresponds to the first letter of the coin
q = 25
d = 10
n = 5
p = 1

print("In this game you will enter the number of coins to equal 1 dollar")
quarters = int(input("Enter the number of quarters: "))
dimes = int(input("Enter the number of dimes: "))
nickels = int(input("Enter the number of nickels: "))
pennies = int(input("Enter the number of pennies: "))
#We take the number entered by the user and multiply it by the coins amount
quarters = quarters * q
dimes = dimes * d
nickels = nickels * n
pennies = pennies * p
#Adding all of the coins together
total = quarters + dimes + nickels + pennies
#Displaying the outcome to the user depending on their result
if total == 100:
    print("*********CONGRATULATIONS THE TOTAL EQUALED 1 DOLLAR*********")
if total < 100:
    print("The total was",total, "which is less than 100")
if total > 100:
    print("The total was",total, "which is greater than 100")
"""

#Question 6
"""
6. The month of February normally has 28 days. But if it is a leap year, February has 29
days. Write a program that asks the user to enter a year. The program should then
display the number of days in February that year. Use the following criteria to identify
leap years:
a. Determine whether the year is divisible by 100. If it is, then it is a leap year if and
only if it is also divisible by 400. For example, 2000 is a leap year, but 2100 is not.
b. If the year is not divisible by 100, then it is a leap year if and only if it is divisible
by 4. For example, 2008 is a leap year, but 2009 is not.

userInput = int(input("Enter a year to check if it is a leap year: "))
#Checking the remainder for the year after dividing it multiple times
if userInput %100 == 0 and userInput %400 == 0:
    print("The number of days in february in",userInput,"is 29")
if userInput %100 != 0 and userInput %4 == 0:
    print("The number of days in february in",userInput,"is 29")
if userInput %100 > 0 or userInput %4 > 0 or userInput %400 > 0:
    print("The number of day in February in",userInput,"is 28")
"""

#Question 7
"""
Write a program that calculates and displays a person’s body mass index (BMI). The
BMI is often used to determine whether a person is overweight or underweight for his
or her height. A person’s BMI is calculated with the following formula:
BMI=weight×703/height2
where weight is measured in pounds and height is measured in inches. The program
should ask the user to enter his or her weight and height, then display the user’s BMI. The
program should also display a message indicating whether the person has optimal weight, is
underweight, or is overweight. A person’s weight is considered to be optimal if his or her BMI
is between 18.5 and 25. If the BMI is less than 18.5, the person is considered to be underweight.
If the BMI value is greater than 25, the person is considered to be overweight.

weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))
#Calculatng the BMI
BMI = (weight*703)/(height**2)
#FInding where the users BMI falls
if BMI < 18.5:
    print("Your BMI is less than 18.5, you are underweight")
if BMI > 25:
    print("Your BMI is greater than 25, you are overweight")
if BMI >= 18.5 and BMI <= 25:
    print("Your BMI is between 18.5 and 25, your BMI is optimal")
"""

#Question 8

"""
Stock Transaction Program
Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the
purchase:
• The number of shares that Joe purchased was 2,000.
• When Joe purchased the stock, he paid $40.00 per share.
• Joe paid his stockbroker a commission that amounted to 3 percent of the amount
he paid for the stock.
Two weeks later, Joe sold the stock. Here are the details of the sale:
• The number of shares that Joe sold was 2,000.
• He sold the stock for $42.75 per share.
• He paid his stockbroker another commission that amounted to 3 percent of the
amount he received for the stock.
Write a program that displays the following information:
• The amount of money Joe paid for the stock.
• The amount of commission Joe paid his broker when he bought the stock.
• The amount for which Joe sold the stock.
• The amount of commission Joe paid his broker when he sold the stock.
• Display the amount of money that Joe had left when he sold the stock and paid
his broker (both times). If this amount is positive, then Joe made a profit. If the
amount is negative, then Joe lost money.

joeShares = 2000
paidShares = 40.00
soldShares = 42.75
bought = joeShares * paidShares
sold = joeShares * soldShares
paidBroker1 = (bought * 0.03)
paidBroker2 = (sold * 0.03)
#Calculate whether the money he has left is positive or negative
moneyLeft = bought - sold - paidBroker1 - paidBroker2
#Display all the information to the user after all calculations
print("Joe paid $", bought, "for 2000 shares")
print("Joe paid $", paidBroker1, "to his broker after he bought the shares the first time")
print("Joe sold his stock for $", sold)
print("Joe paid $", paidBroker2, "to his broker after he sold his shares")
#Displaying whether the money left was a profit or not
if moneyLeft > 0:
    print("Joe earned $",moneyLeft)
if moneyLeft < 0:
    print("Joe lost $",moneyLeft)
"""

###Assignment 2 Questions###

#Question 1
"""
Print following patterns:
i)
*
* *
* * *
* * * *
* * * * *
ii)
        *
      * *
    * * *
  * * * *
* * * * *

def pattern1():
    for i in range(0, 5):
        for j in range(0, i + 1):
            print("* ", end = "")
        print("\n")
pattern1()

def pattern2():
    for i in range(0, 5):
        for j in range(1 , 5 - i):
            print(" ", end=" ")
        for n in range(0, i + 1):
            print("* ", end = "")
        print("\n")
pattern2()
"""

#Question 2
"""
. Execute following steps:
i) Take two integer inputs from users (one number is n, other number is r)
ii) 𝑛!/𝑟!(𝑛−𝑟)!
iii) 𝑛!/(𝑛−𝑟)!

def calculations():
    n = int(input("Enter a number n: "))
    counter_n = 1
    result_n = 1
    while counter_n  <= n:
        result_n = result_n * counter_n
        counter_n += 1
    print(result_n)

    r = int(input("Enter a number r: "))
    counter_r = 1
    result_r = 1
    while counter_r  <= r:
        result_r = result_r * counter_r
        counter_r += 1
    print(result_r)

    j = n - r
    counter_j = 1
    result_j = 1
    while counter_j  <= j:
        result_j = result_j * counter_j
        counter_j += 1
    calculation1 = result_n/(result_r*(n-r))
    print("The result of n!/(r!*(n-r)): ")
    print(calculation1)

calculations()
"""

#Question 3
"""
Given a list, sort them using loop and print the new list. List = [20, 68, 41, 88, 16,
40, 65, 97, 85]

List = [20, 68, 41, 88, 16, 40, 65, 97, 85]
Sorted = []

while List:
    min = List[0]
    for num in List:
        if num < min:
            min = num
    Sorted.append(min)
    List.remove(min)

print(Sorted)
"""

#Question 4
"""
Given a list do the following:
i) Find the sum of all elements in list
Assignment 2 Introduction to Scripting
ii) Create a new list which contain even number. Print the list. Find the sum of
all elements in the list.
iii) Create a new list which contain odd number. Print the list. Find the sum of all
elements in the list.

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
listEven = []
listOdd = []
num = 0
sum = 0
sumEven = 0
sumOdd = 0
for i in range (0, len(list)):
    sum = sum + list[i]
for num in range (0, len(list)):
    if list[num] % 2 == 0:
        listEven.append(list[num])
    else:
        listOdd.append(list[num])

for i in range (0, len(listEven)):
    sumEven = sumEven + listEven[i]

for i in range (0, len(listOdd)):
    sumOdd = sumOdd + listOdd[i]
print(list, "Sum of full array =",sum)
print(listEven, "Sum of even array =",sumEven)
print(listOdd, "Sum of odd array =",sumOdd)
"""

#Question 5
"""
Find all the prime numbers between [2 50] and print them. Use loops

def findAllPrimes(start, end):
    for num in range (start, end + 1):
        if num > 1:
            for i in range(2, num+1):
                if(num ==2):
                    print(num)
                    break
                elif (num % i) == 0:
                    break
                else:
                    print(num)
                    break
findAllPrimes(2, 50)
"""
for i in range(2, 51):
    prime = True
    for j in range(2, i):
        if (i % j) == 0:
            prime = False
        if prime:
            print(i)
"""

#Question 6
"""


"""


###Assignment 3 Questions###

#Question 1
"""
"""
        Question 1: This program creates a car class and will use an object to
                    call the accelerate and brake members to increase and decrease
                    the speed variable

#Creating the class car that will initialize 3 members
class Car():
    def __init__(self, make, year_model):
        self.__make = make
        self.__year_model = year_model
        self.__speed = 0
#This function will increase variable speed by 5
    def accelerate(self):
        self.__speed += 5
#This function will decrease variable speed by 5
    def brake(self):
        self.__speed -= 5
#Return the speed value
    def get_speed(self):
        return self.__speed
#Return the make of the car
    def get_make(self):
        return self.__make
#Return the year and model of the car
    def get_year_model(self):
        return self.__year_model
#Printing the make year and model
my_car = Car("Hyundai", "Kona 2020")
print(my_car.get_make(), my_car.get_year_model())
#Using the accelerate and brake functions in loops will call them multiple times
#to change the speed value
for i in range(5):
    my_car.accelerate()
    print(my_car.get_speed())
for i in range(5):
    my_car.brake()
    print(my_car.get_speed())
"""
"""

#Question 2&3

"""
"""
        Question 2&3: This program will create multiple members that will hold
                        different information for the employees including their
                        name and title. It will then print out all the information

class Employee():
    def __init__(self, firstName, lastName, ID_Number, department, title):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = self.firstName+' '+self.lastName
        self.email = self.firstName.lower()+'.'+self.lastName.lower()+'@company.com'
        self.ID_Number = ID_Number
        self.department = department
        self.title = title

    def __str__(self):
        return 'Name:{self.firstName} {self.lastName} ''ID:{self.ID_Number} ''Department:{self.department} ' 'Title:{self.title} ''Email:{self.email}'.format(self=self)

emp1 = Employee('Susan', 'Meyers','47899','Accounting','Vice President')
print(emp1)
emp2 = Employee('Mark', 'Jones', '39119','IT','Programmer')
print(emp2)
emp3 = Employee('Joy', 'Rogers','81774','Manufacturing','Engineering')
print(emp3)
"""

#Question 4
"""

        Question 4: In this question we will be taking the grades of 25 Students
                    in 6 different classes while averaging them and sorting them
                    in descending order

#Defining StudentInfo class
class StudentInfo():
#Defining the name and different classes
    def __init__(self, name, math, english, history, science, writing, gym):
        self.name = name
        self.math = math
        self.english = english
        self.history = history
        self.science = science
        self.writing = writing
        self.gym = gym
#Calculating the average of all classes
    def avg(self):
        self.average = (self.math + self.english + self.history + self.science + self.writing + self.gym)/6
        return self.average

#Defining the students array and putting in all the grades for each student
Students = []
Students.append(StudentInfo("Ethan",90 ,85 ,85 ,75 ,97 ,80))
Students.append(StudentInfo("Jam  ",70 ,65 ,70 ,78 ,56 ,87))
Students.append(StudentInfo("Tam  ",60 ,85 ,90 ,73 ,78 ,68))
Students.append(StudentInfo("Ham  ",80 ,82 ,89 ,90 ,87 ,82))
Students.append(StudentInfo("Ram  ",89 ,96 ,94 ,93 ,95 ,90))
Students.append(StudentInfo("Cam  ",80 ,81 ,89 ,80 ,90 ,90))
Students.append(StudentInfo("Bam  ",72 ,74 ,79 ,66 ,86 ,82))
Students.append(StudentInfo("Lam  ",82 ,85 ,86 ,90 ,95 ,80))
Students.append(StudentInfo("Jar  ",90 ,88 ,94 ,65 ,90 ,76))
Students.append(StudentInfo("Dar  ",93 ,84 ,79 ,93 ,84 ,86))
Students.append(StudentInfo("Bar  ",96 ,80 ,67 ,78 ,73 ,82))
Students.append(StudentInfo("Blam ",97 ,79 ,92 ,79 ,86 ,87))
Students.append(StudentInfo("Clam ",60 ,65 ,67 ,70 ,63 ,68))
Students.append(StudentInfo("Wam  ",96 ,90 ,94 ,92 ,90 ,87))
Students.append(StudentInfo("Slam ",90 ,85 ,84 ,75 ,78 ,80))
Students.append(StudentInfo("Man  ",80 ,83 ,94 ,89 ,84 ,88))
Students.append(StudentInfo("Jet  ",82 ,80 ,79 ,75 ,74 ,75))
Students.append(StudentInfo("Bert ",96 ,93 ,92 ,98 ,91 ,83))
Students.append(StudentInfo("Cod  ",89 ,85 ,83 ,88 ,82 ,85))
Students.append(StudentInfo("Dod  ",69 ,67 ,73 ,75 ,74 ,80))
Students.append(StudentInfo("Day  ",90 ,95 ,92 ,98 ,89 ,90))
Students.append(StudentInfo("Way  ",97 ,94 ,98 ,99 ,94 ,93))
Students.append(StudentInfo("Hay  ",92 ,90 ,82 ,73 ,92 ,83))
Students.append(StudentInfo("Slay ",92 ,80 ,84 ,85 ,90 ,81))
Students.append(StudentInfo("Bay  ",82 ,83 ,89 ,89 ,90 ,76))
Students.append(StudentInfo("John ",95 ,85 ,81 ,84 ,80 ,87))
Students.sort(key = lambda x: x.avg(), reverse = True)

print("Name", " M", " E", " H", " S", " W", " G", " AVG")
#Displaying the grades and average to the user
for j in Students:
    print(j.name, j.math,j.english,j.history,j.science,j.writing,j.gym, '%.2f' % j.avg())
#Calculating the averages for different classes and printing them
def printAvgs():
    mathAvg = 0
    for i in Students:
        mathAvg = mathAvg + i.math
    mathAvg = mathAvg/25

    engAvg = 0
    for i in Students:
        engAvg = engAvg + i.english
    engAvg = engAvg/25

    histAvg = 0
    for i in Students:
        histAvg = histAvg + i.history
    histAvg = histAvg/25

    scienceAvg = 0
    for i in Students:
        scienceAvg = scienceAvg + i.science
    scienceAvg = scienceAvg/25

    writingAvg = 0
    for i in Students:
        writingAvg = writingAvg + i.writing
    writingAvg = writingAvg/25

    gymAvg = 0
    for i in Students:
        gymAvg = gymAvg + i.gym
    gymAvg = gymAvg/25
    print("Averages for every class:")
    print("Math:",mathAvg, "English:", engAvg, "History:", histAvg, "Science:", scienceAvg, "Writing:", writingAvg, "Gym:", gymAvg)
printAvgs()

"""

###Assignment 4 Questions###

#Question 1
"""
#name_dict = {"name":{"first_name":"adarsh","last_name":"kesireddy"},"office_hours":"10 to 11"}
#print(name_dict)
method_dict = dict({1:"class",2:"on",3:"dictionary"})
print(method_dict)

list_dict = dict([(1,"class"),(2,"list"),(3,"into"),(4,"dictionary")])
print(list_dict)

class Employee():
    def __init__(self, firstName, lastName, ID_Number, department, title):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = self.firstName+' '+self.lastName
        self.email = self.firstName.lower()+'.'+self.lastName.lower()+'@company.com'
        self.ID_Number = ID_Number
        self.department = department
        self.title = title

    def __str__(self):
        return 'Name:{self.firstName} {self.lastName} ''ID:{self.ID_Number} ''Department:{self.department} ' 'Title:{self.title} ''Email:{self.email}'.format(self=self)

emp1 =
{
self.ID_Number : '47899'
'Katie' : '231-451',
'Joanne' : '234-124'
}

emp1 = Employee('Susan', 'Meyers','47899','Accounting','Vice President')
print(emp1)
emp2 = Employee('Mark', 'Jones', '39119','IT','Programmer')
print(emp2)
emp3 = Employee('Joy', 'Rogers','81774','Manufacturing','Engineering')
print(emp3)
"""

#Question 2
"""
Design a program that asks the user to enter a series of 20 numbers. the program
should store the numbers in a list then display the following data

def getTotal():
    total = 0
    for i in range(len(numList)):
        total = total + numList[i]
    return total

def getSmallest():
    numList.sort()
    print("The smallest value in the list is:", numList[0])

def getLargest():
    numList.sort()
    print("The largest value in the list is:", numList[19])

numList = []
for i in range(20):
    number = (int(input("Enter a random number:")))
    numList.append(number)
getSmallest()
getLargest()
print("The total of the list is", getTotal())
print("The average of the list is:",getTotal()/20)
"""

#Question 3
"""
Write a Python script to generate and print a dictionary that contains a number
(between 1 and n) in the form (x, x*x)

number = int(input("Enter any number: "))
dict = dict()

for i in range(1, number + 1):
    dict[i] = i * i
print(dict)
"""

#Question 4
"""
1. Generate a random list of size 100 using for loop. The range is [0 to 20]
2. Write a function to find the second largest numbers in the list without sorting the
list
3. Remove repeating elements in the list

import random
list = []
for i in range(0,100):
    num = random.randint(0, 20)
    list.append(num)
print(list)
noRepeat = []
for i in list:
    if i not in noRepeat:
        noRepeat.append(i)
print(noRepeat)

"""

###Assignment 5###

#Question 1
"""
Morse Code

def strToMorse(string):
    morseDict = {' ': '|', 'A': '.-', 'B': '-...','C': '-.-.',
    'D': '-..','E': '.','F': '..-.','G': '--.','H': '....',
    'I': '..','J': '.---','K': '-.-','L': '.-..',
    'M': '--','N': '-.','O': '---','P': '.--.',
    'Q': '--.-','R': '.-.','S': '...','T': '-',
    'U': '..-','V': '...-','W': '.--','X': '-..-',
    'Y': '-.--','Z': '--..', '0': '-----', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..'}

    morse_code = ""

    for i in string:
        morse_code += morseDict[i.upper()]

    return morse_code

string = input("Enter text to be converted: ")
print(strToMorse(string))
"""

#Question 2
"""
Write a program with a function that accepts a string as an argument and returns
the number of vowels that the string contains. The application shoukd have another
function that accepts a string as an argument and returns the number of consanants
that the string contains. The application should let the user enter a string and
should display the number of vowels and the number of consanants it contains

def numVowels(string):
    count = 0
    for i in range(len(string)):
        if(string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u'):
            count = count + 1
    return count
def numConsonants(string):
    count = 0
    for i in range(len(string)):
        if(string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u'):
            count = count + 0
        else:
            count = count + 1
    return count
string = input("Enter a string:")
print("The number of vowels is:",numVowels(string))
print("The number of consonants is:",numConsonants(string))
"""

#Question 3
"""
1. Count all letters, digits and symbols in: str1 = "P@#yn26at^&i5ve"
2. Remove special symbols and punctuation from string: str1 = "/*Jon is
@developer & musician"
3. Remove ‘-‘and replace with space in : str1 = Emma-is-a-data-scientist
4. Write a program to remove all consonants from “Hello, have a good day

str1 = "P@#yn26at^&i5ve"
str1Length = len(str1)
print("The length of str1 is: ", str1Length)

str2 = "/*Jon is @developer & musician"
str2fixed = ""
for i in str2:
    if i.isalnum():
        str2fixed += i
print(str2fixed)

str3 = "Emma-is-a-data-scientist"
str3fixed = str3.replace("-"," ")
print(str3fixed)

str4 = "Hello, have a good day"
for i in range(len(str4)):
    if(str4[i] == 'a' or str4[i] == 'e' or str4[i] == 'i' or str4[i] == 'o' or str4[i] == 'u'):
        print(str4[i], end = "")
"""

#Question 4
"""
1. Ask ‘n’ number of integer inputs from user, create a list with the inputs. Inputs
will be from range of 0 to 100 including boundary values. Find the average,
median, standard deviation of the numbers. (n >10)
2. From the above list, create a new list which holds division of elements (use try
block for any type of exception). First element of new list will be division of first
element with second element from the first list.
Example: list_part_1 = [3, 4, 5, 6, 7]; list_part_2 = [3/4, 4/5, 5/6, 6/7]

n = int(input("Enter the number of integers to be in the list:"))
import random
list = []
for i in range(0,n):
    num = random.randint(0, 100)
    list.append(num)

def getAverage():
    total = 0
    for i in range(len(list)):
        total = total + list[i]
    avg = total/n
    print(avg)

def getMedian():
    median = list[n//2]
    print(median)

def getStdD():

getAverage()
getMedian()
"""

#Question 5
"""
Given a string “this is the string for the class”
1. Convert the above string to “This Is The String For The Class” using a loop
2. Convert the above string to “ThisIsTheStringForTheClass” using a loop
3. Convert the above string to “Thi$ I$ $tring for the Cla$$” using a loop
4. Convert the above string to “This is the String for the Class” using a loop

"""

###Assignment 6###

#Question 1
"""
1. Create a class “student” which holds firstname(string), lastname(string), email(string),
all_course(list of numbers)
2. Use regular expression to extract firstname (without spaces), lastname (without spaces),
email (without spaces), and all_courses from the file provided (students.txt).
3. Create an object for each student and save the data.
4. From previous assignment, take the list of 25 students and append to the file.
5. After appending sort all the students (25 students from previous assignment + 10 students
from students.txt file) on first name and save it a new file.
"""

#Question 2
"""

    Question 2:

class Student:
    def __init__(self, firstName, lastName, email, allGrades):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.allGrades = allGrades

def main():
    allStudents = []
    with open("students.txt", "r")
        next(studentsFile)
        for line in studentsFile:
            student = Student(splitLine[0], splitLine[1], splitLine[2], splitGrades)
            allStudents.append(student)
    for s in allStudents:
        print(s.firstname)

    allStudents.sort(key = lambda x: x.firstName)
    print("Sorted: \n")
    for s in allStudents:
        print(s.firstName)
main()
"""
