import math

while True:
    calculation_type = str.lower(input("Would you like the area or the circumference of a circle? "))
    if calculation_type == "area" or calculation_type == "circumference":
        break
    else:
        print("Invalid input. Please enter a either area or circumference.")

while True:
    try:
        radius = float(input("Enter the radius of the circle: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

if calculation_type == "area":
    area = math.pi * radius * radius
    print(f"The area of your circle is {round(area, 2)}")

else:
    circumference = 2 * math.pi * radius
    print(f"The circumference of your circle is {round(circumference, 2)}")