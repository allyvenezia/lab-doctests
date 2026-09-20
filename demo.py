#score = 10
#score = score + 3
#print (score)


def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


colors = ["red", "green", "blue"]
for color in colors:
    print(color)


for i in range(1,101):
    print(i)

def factorial(n):
   result = 1
   for i in range (1, n + 1):
    print(i)
    result = result * i
    return result 

print("the result is:", factorial(1000))

#print all numbers between 1 and 1000
for i in range(1, 11):
    print(i)

#while loop 
n = 1 
while n <= 10:
    print(n)
    n += 1
