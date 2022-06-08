#Python has 2 types of numbers - Integers and floating point

print(2 + 3) #add
print(2 - 3) #sub
print(2 * 3) #mul
print(10 / 5) #div - always results floating number
print(10 // 3) #floor div - results integer
print(10 % 3) #modulus

#...........................................................................................


#float stores values as binary or compute in binary. and 1/5 and 1/10 has a problem. Other float work fine
# For more understanding refer https://www.quora.com/Why-is-0-1+0-2-not-equal-to-0-3-in-most-programming-languages

print(0.1 + 0.2) #prints 0.30000000000000004
print(0.1 - 0.2) #works fine
print(0.1 * 0.2) #problem
print(0.1 * 0.3) #works fine
print(0.1 / 0.2) #works fine
print(2.11 // 0.3) #floating value
print(2.11 % 0.3) #prints 0.009999999999999953

#.............................................................................................
'''
  Rules for variable names
  1. Names cannot start with a number
  2. No spaces in the name. Use "_" instead
  3. Cant use any other special character other than "_"
  4. As per pep8 stds - names should be lowercase
  5. No special keywords like str, int etc
  
'''

# Python uses dynamic typing
my_dog = "juno"
print(my_dog)
print(type(my_dog)) #string type
my_dog = 1
print(my_dog)
print(type(my_dog)) #Integer type

#Python variable operations
number1 = 3.0
number2 = 10
number3 = number1 + number2
print(number3)
print(number1 * number2)
print(type(number3))
