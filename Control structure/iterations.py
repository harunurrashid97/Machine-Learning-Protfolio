# while loop
i = 0
while i < 5:
    print(i, end = ' ')
    i += 1

# For loop
fruits = ["Apple", "Orange", "Pineapple", "Grape"]
# Lets make juice with these fruits

for fruit in fruits:
    print(fruit + " Juice!")

# Range function 
for i in range(5, 10):
    print(i)

# Break & Continue statements 

for i in range(20):
    if i == 5:
        continue
    if i > 9:
        break
    print(i)

print("Printed first 10 numbers except 5!")