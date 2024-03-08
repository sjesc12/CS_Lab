def calculate_e_mod(message, e, p):
    return (message**e)%p

def get_user_input():
    try:
        num1 = int(input("Enter the message: "))
        num2 = int(input("Enter the exponential: "))
        num3 = int(input("Enter the prime number: "))
        return num1, num2, num3
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return get_user_input()

def main():
    num1, num2, num3 = get_user_input()
    result = calculate_e_mod(num1, num2, num3)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()


