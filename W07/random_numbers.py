import random

def main():
    # Create a list named numbers
    numbers = [16.2, 75.1, 52.3]
    # Printing the numbers in the list
    print(numbers)

    # Creating a list of words
    words = ['apple','banana','orange','grape','kiwi']

    # Calling append_random_numbers function with only one argument
    append_random_numbers(numbers)
    # Printing the modified version of the list
    print(numbers)

    # Calling append_random_numbers function with three arguments
    append_random_numbers(numbers , 3)
    # Printing the modified version of the list
    print(numbers)

    # Calling append_random_words function with only one argument
    append_random_words(words)
    # Printing the modified version of the list
    print(words)



# Creating a fuction to append numbers to the "Numbers" list
def append_random_numbers( numbers_list ,quantity = 1):
    # Creating a loop to append "quantity" amount of number to the "numbers" list
    for _ in range (quantity):
        # Creating a random number between 0 and 100
        random_number = random.uniform(0 , 100)
        # Rounding the random number that we created one digit after the decimal
        random_number = round(random_number,1)
        # Adding the random number that we created to the list
        numbers_list.append(random_number)

# Creating a fuction to append random words to the "words" list
def append_random_words(word_list, quantity=1):
    word_pool = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'watermelon', 'strawberry']
    for _ in range(quantity):
        random_word = random.choice(word_pool)
        word_list.append(random_word)
        

# Call main to start this program.
if __name__ == "__main__":
    main()
