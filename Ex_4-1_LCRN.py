def LCRN_generator(a, X, c, m):
    return (a*X+c)%m

def get_user_input():
    try:
        num1 = int(input("Enter the seed: "))
        num2 = int(input("Enter a: "))
        num3 = int(input("Enter c: "))
        num4 = int(input("Enter m: "))
        num5 = int(input("Enter range of sequence: "))
        return num1, num2, num3, num4, num5
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return get_user_input()

def main():
    num1, num2, num3, num4, num5 = get_user_input()
    sequence = [num1]
    for _ in range(num5):
        sequence.append(LCRN_generator(num2, sequence[-1],num3,num4))
    sequence.pop(0)
    print(f"The sequence is: {sequence}")

if __name__ == "__main__":
    main()


