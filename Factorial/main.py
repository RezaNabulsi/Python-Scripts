def main():
    # Get user input
    num = int(input("Insert number to find factorial of:  "))

    # Print answer
    answer = 1
    while num > 0:
        answer = answer*num
        num = num - 1

    print(f"Your answer is : {answer:,}")

if __name__ == "__main__":
    main()