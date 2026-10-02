# Name: Deborah Amahirwe

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """Read two integers from the user and return them."""
    x = input("give me x: ")
# Convert the input from a string to an integer.
    x = int(x)

    y = input("give me y: ")
# Convert the input from a string to an integer.
    y = int(y)

    return x, y


# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """Calculate and return (a * b) / (a + b)."""
# Calculate the numerator of the expression.
    mult_result = a * b
    print("mult result:", mult_result)
# Calculate the denominator of the expression.   
    add_result = a + b
    print("add result:", add_result)
    
    return mult_result / add_result

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """Print the two numbers and their multadd result."""
    print("****************")
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print("================")
    

def main ():
    """Run the program and display the results."""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    
    x, y = read_two_ints()
    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    xy_multadd = compute_multadd(x, y)
    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy(x, y, xy_multadd)

    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()

