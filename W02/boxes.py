# https://byui-cse.github.io/cse111-course/lesson02/check.html#problem

# 02 Checkpoint: Calling Functions

# https://github.com/semhaydn

import math

# Receiving the inputs from the user

items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

# calculating the boxes that we need
boxes_needed = items / items_per_box

# using math.ceil function to round up the float number that we have
boxes_needed = math.ceil(boxes_needed)

# display the result to the user
print(f"\nFor {items} items, packing {items_per_box} items in each box, you will need {boxes_needed} boxes.")








