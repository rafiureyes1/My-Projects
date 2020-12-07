string = input("Enter a string:") #Input

rev_string = string[::-1] #Defining reversed string to a string that is being reversed with [start : end : step]

print("reversed string:", rev_string)

if string == rev_string:
    print("string is palindrome")
else:
    print("string is not palindrome")
