# Get user input
repeat = int(input("Please enter the number of times you want the Fibonacci Sequence to repeat:  "))

last, current = 0, 1

# Find value
repeatCount = repeat
while repeatCount > 0:
    last = current
    current = current + last
    repeat = repeatCount - 1  # Counter

print(f"The {repeat}th number in the Fibonacci Sequence is: {last:,}")