#Program to check if a number is even or odd
number = int(input("Enter a number: "))
def question():
    if number % 2 == 0:
        print("The number is even. ")
    elif number % 2 != 0:
        print("The number is odd. ")

#Program to print square and cube of a number
def main():
    print(number*number)
    print(number*number*number)
    """
    this is to find square and cube using function
    """
    question()

main()

a_string = "S 11 2 3 R"
tokens = a_string.split(" ")
print(tokens[1])
for i in tokens:
    print(i)

def split_string(s, delimiter):
    tokens = s.split(delimiter)
    for token in tokens:
        print(token)

print("Test 1:")
split_string("Thats my house,\" I said.", " ")
print("\nTest 2:")
split_string("one two, \tthree\nfour five", " ")
print("\nTest 3:")
split_string("My name is \"Donald Trump.\"", " ")


    