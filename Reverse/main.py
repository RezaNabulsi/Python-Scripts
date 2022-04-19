def main():
    # Get user input
    textIn = input("What string would you like to turn backwards? \n"); text = textIn.lower()

    # Find vowel and consonant values
    array, vowels, consonants = list(text), 0, 0
    for char in array:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u': vowels += 1
        elif char != ' ': consonants += 1

    # Return results
    print(f"'{textIn}' backwards is '{textIn[::-1]}'")
    print(f"No. of vowels = {vowels}, No. of consonants = {consonants}.")

if __name__ == "__main__":
    main()