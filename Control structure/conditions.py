#if-else
x = int(input("Enter the value : "))
if x == 6:
    print('x is equal to 5')
else:
    print('x is not 5')

#if-elif-else
x = int(input("Enter the value : "))

if x == 1:
    print('x is 1')
    
elif x == 2:
    print('x is 2')
    
elif x == 3:
    print('x is 3')
    
else:
    print('x is not 1 nor 2 nor 3')

#nested if-else
x = int(input("Enter the value : "))
if x > 1:
    if x < 5:
        print('x is between 1 and 5')
    else:
        print('x is not between 1 and 5')