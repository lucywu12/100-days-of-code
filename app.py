# 1/8 Inheritance

numbers = [10, 3, 6, 2]

import utils

print(utils.find_max(numbers))

------------------------------

def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return (maximum)
