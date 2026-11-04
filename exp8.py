
# Temperature Converter using Functions

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(c):
    return c + 273.15


# Main program
while True:
    print("TEMPERATURE CONVERTER")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(c)
        print("Temperature in Fahrenheit:", result, "°F")
    elif choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(f)
        print("Temperature in Celsius:", result, "°C")
    elif choice == 3:
        c = float(input("Enter temperature in Celsius: "))
        result = celsius_to_kelvin(c)
        print("Temperature in Kelvin:", result, "K")
    elif choice == 4:
        print("Thank you for using Temperature Converter!")
        break
    else:
        print("Invalid")
