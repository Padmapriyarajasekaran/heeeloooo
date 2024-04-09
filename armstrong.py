def is_armstrong(number):
    # Count the number of digits
    num_digits = len(str(number))

    # Calculate the sum of the digits raised to the power of the number of digits
    total = sum(int(digit) ** num_digits for digit in str(number))

    # Check if the total is equal to the original number
    return total == number


# Example usage
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")