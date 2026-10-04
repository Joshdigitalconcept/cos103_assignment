#  Write program that converts temperatures between Celsius and Fahrenheit
cal_celcius = int(input("Enter temperature in celcius: "))
fahrenheit = (cal_celcius * 9/5) + 32

print(f"{cal_celcius}°C is equal to {fahrenheit}°F")

cal_fahrenheit = int(input("Enter temperature in fahrenheit: "))
celcius = (cal_fahrenheit - 32) * 5/9

print(f"{cal_fahrenheit}°F is equal to {celcius}°C")

# Create a program that calculates the area of different shapes (circle, square, rectangle, triangle) based on user input.
shape = input("Enter shape (circle, square, rectangle, triangle): ")

if shape.lower() == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius ** 2
    print(f"The area of the circle is: {area}")
elif shape.lower() == "square":
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    print(f"The area of the square is: {area}")
elif shape.lower() == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")
elif shape.lower() == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
else:
    print("Invalid shape. Please enter circle, square, rectangle, or triangle.")