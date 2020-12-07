#Create a game that will determine if a number is prime or not simply by imput
#define 'num' as an input that will be a string that can become an integer to apply if and else statements determing if a number is prime or not
num = int(input("Enter any positive number to determine if it prime or not:"))
#Use an if loop to determine if a number is prime or not
if num>1:
    for i in range(2, num):
        if (num%i) ==0:
            print(num, "is not prime!")
            break
    else:
        print(num, "is a prime number!")
else:
    print(num, "is not a prime number!")
