def calculate_gcd(a, b):
    return a if b == 0 else calculate_gcd(b, a % b)

def get_user_input():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return get_user_input()

def main():
    num1, num2 = get_user_input()
    gcd_result = calculate_gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {gcd_result}")

if __name__ == "__main__":
    main()


