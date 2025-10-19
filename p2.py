#Given three numbers find the maximum of three numbers using the ternary operator.

a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

#nested
max_num = "a is greatest" if a>b and a>c else ("b is greatest" if b>a and b>c else "c is greatest" )
print(max_num)