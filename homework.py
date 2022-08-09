#QUestion 1: Cube Number Test... Print out all cubed numbers up to the total value 1000. 
# Meaning that if the cubed number is over 1000 break the loop.

#Solution 1
def cubeNumbers ():
    range_1 = int(input("WHat is the first number of the range "))
    range_2 = int(input("What is the second number of the range"))

    for i in range(range_1, range_2 + 1):
        if i > 10:
            break
        else:
            print(i ** 3)

cubeNumbers()

#Solution 2
def cubeNumbers (num_1, num_2):
    l = []
    for i in range(num_1, num_2 + 1):
        l.append(i**3)
    return l
print(cubeNumbers(1,10))


#Question2: Get first prime numbers up to 100

num_1 = 1
num_2 = 100

for num in range(num_1, num_2 + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


#Question 3: Take in a users input for their age, if they are younger than 18 print kids, 
#if they're 18 to 65 print adults, else print seniors

def printAge():
    age = int(input("What is your age "))
    if age < 18:
        print("Kids")
    elif age >= 18 and age <= 65:
        print("Adults")
    else:
        print("Seniors")

printAge()
