#Write a program that converts and prints user given measurement in inches into
# 1. foot(12 inches)
# 2. yard(36 inches)
# 3. centimetres(2.54 inches)
# 4. meter(39.37 inches)

print("UNITS:-\n 1.Foot \n 2.Yard \n 3.Centimetre \n 4.Metre")
value = float(input("Enter measurement: "))
unit = input("Enter unit: ")

if unit == "foot":
    inches = value*12
elif unit == "yard":
    inches = value*36
elif unit == "centimetre":
    inches = value/2.54
elif unit == "metre":
    inches = value/0.0254
else:
    print("Invalid input ")

print(f"{value} {unit} = {inches} inches")

