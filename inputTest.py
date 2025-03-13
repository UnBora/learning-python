def print_variables(a, b, separator):
    # With space
    print(a, b)

    # Without newline
    print(a, b, end="")

    # With separator
    print(f"\n{a}{separator}{b}")

    # Without space
    print(a + b)

# Example usage
a = "Hello"
b = "World"
separator = "&"

print_variables(a, b, separator)
