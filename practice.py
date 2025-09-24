#to check if triangle is valid or not
def triangle_validator(a, b, c):
    print("Checking if the triangle is valid, true if valid, false if not")
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
    """
    This function checks if the sum of any two sides is greater than the third side.
    If the condition is satisfied, it returns True, indicating a valid triangle.
    """
    
#main  function
def main():
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    print("true/false:", triangle_validator(a, b, c))
    """
    This function prompts the user to input the lengths of the three sides of a triangle.
    It then calls the triangle_validator function to check if the triangle is valid.
    """
main()