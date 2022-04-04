# Get user input
fizz = int(input("Please enter 'Fizz' number:  "))
buzz = int(input("Please enter 'Buzz' number:  "))
count = int(input("Please enter the amount of times you'd like the algorithm to repeat:  "))
# Output results
count += 1

for i in range (count):
    output = ''
    str1, str2, str3, str4 = '', '', '', ''

    if i%fizz == 0: str1 = 'Fizz'
    if i%buzz == 0: str2 = 'Buzz'
    output = f"{str1}{str2}"

    if output == '': output = i
    print(output)