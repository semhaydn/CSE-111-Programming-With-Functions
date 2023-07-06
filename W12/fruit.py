def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print('Original version of the list:')
        print(f"original: {fruit_list}")

        # Reverse and print fruit_list.
        print('\n Reversed version of the list:')
        fruit_list.reverse()    
        print(fruit_list)

        # Append "orange" to the end of fruit_list and print the list.
        print('\nAppend "Orange":')
        fruit_list.append('orange')
        print(fruit_list)

        # Find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
        print('\nInsert "Cherry":')
        i =  fruit_list.index('apple')
        fruit_list.insert(i ,'cheery')
        print(fruit_list)

        # Remove "banana" from fruit_list and print the list.

        fruit_list.remove('banana')
        print('\nRemoved item is banana:')
        print(fruit_list)

        # Pop the last element from fruit_list and print the popped element and the list.
        popped_item = fruit_list.pop()
        print(f'\nPopped item is {popped_item}')
        print(fruit_list)
        
        # Sort and print fruit_list.
        fruit_list.sort()
        print('\nSorted version of the list :')
        print(fruit_list)

        # Clear and print fruit_list.
        fruit_list.clear()
        print(f'\nCleared the list')
        print(fruit_list)

    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")


# Call main to start this program.
if __name__ == "__main__":
    main()