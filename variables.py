def variables_practice():
    my_age = 18
    year = 365 
    pet_name = "ginger"
    pi = 3.14

    print("Age: ", my_age)
    print("Days: ", year)
    print("Pet: ", pet_name)
    print("Pi: ", pi)
variables_practice()

def prompt_and_print():
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a number: "))
    print("Addition: ",number1 + number2)
    print("Subtraction: ", number1 - number2)
    print("Multiplication: ", number1 * number2)
    print("Division: ",number1/number2)
prompt_and_print()

def circle_area(radius):
    return 3.14 * radius ** 2

def main():
    area = circle_area(10) #Function call
    print(area) #radius = 10
main()

def triangle_area(base, height):
    return 1/2 * base * height
def main():
    area = triangle_area(20,10)
    print(area)
main()

def square_area(length):
    return length * length
def main():
    area = square_area(5)
    print(area)
main()

def rectangle_area(length, width):
    return length * width
def main():
    area = rectangle_area(10,15)
    print(area)
main()




          
        



