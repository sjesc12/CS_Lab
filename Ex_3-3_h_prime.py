def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_user_input():
    try:
        num1 = int(input("Enter the range: "))
        return num1
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return get_user_input()

def main():
    num1 = get_user_input()
    h_num = []
    for i in range(num1+1):
        if is_prime(i):
            h_num.append(i)

    print(f"The highest prime in range from 0 to {num1} is: {max(h_num)}")

if __name__ == "__main__":
    main()