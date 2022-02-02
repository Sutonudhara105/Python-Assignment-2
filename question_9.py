x=input("Enter one number : ")
y=input("Enter another number : ")
z=input("Enter another number : ")

if x>y and x>z:
    maximum=x
elif y>x and y>z:
    maximum=y
else:
    maximum=z

if x<y and x<z:
    minimum=x
elif y<x and y<z:
    minimum=y
else:
    minimum=z

if (x>y and x<z) or (x>z and x<y):
    middle=x
elif (y>x and y<z) or (y>z and y<x):
    middle=y
elif (z>x and z<y) or (z>y and z<x):
    middle=z

print("the sorted numbers : ",maximum,middle,minimum)
