print('hello')
print("hello")
print("Hi, I don't 'have any prolem")
print('hi I dont" " have any problem')

#Indexing --- will be like 0,1,2,3....
a = "hello"
print(a[0])

#reversing index ---- will be like -5, -4, -3, -2, -1, 0
print(a[-1])


if(a[0]==a[-5]):
    print(True)


#Escape characters
print("hello\nworld") #newline
print("hello\\world") #escape character \
'''
print(""hello"") # results error   print(""hello"")
          ^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
'''
#the above example can be achieved like below
print("\"hello\"")

b ="hello \rworld"
print(b) # carriage return
print("hello\tworld") # tab
print("hello\bworld") #backspace prints hellworld
print("hello\vworld") #vertical tab
print("\0") #null vale

'''
 https://www.scaler.com/topics/escape-sequence-in-python/
'''


#String Slicing - syntax --- [start, stop, step]