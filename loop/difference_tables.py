

def difference_of_tables(n1, n2):
    # Ensure n1 > n2 as given in the problem statement
    result = [(n1 * i) - (n2 * i) for i in range(1, 11)]
    print(" ".join(map(str, result)), end="")  # Print in a single line without a newline at the end

# Example usage
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

difference_of_tables(n1, n2)
