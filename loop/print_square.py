
def print_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("* " * n)  # Print full row of stars
        else:
            print("* " + "  " * (n - 2) + "*")  # Print stars at the borders with spaces in between

# Example usage
n = int(input("Enter the size of the square: "))
print_square(n)
