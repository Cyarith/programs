#Objective 6: challenges
#fizzbuzz challenge
#program that outputs the numbers 1 - 100, for multiples of 3 print fizz, for multiples of 5 print buzz, for both print fizzbuzz
for i in range(101):
    if i/15 == i//15:
        print("FizzBuzz")
    elif i/3 == i//3:
        print("Fizz")
    elif i/5 == i//5:
        print("Buzz")
    else:
        print(i)
    
