# 12/30 Remove Duplicates
# My method but this still leads to duplicates :(
numbers = [3, 754, 12, 7, 2, 2, 2, 2, 7, 754]
i = ''
for i in numbers:
    duplicate = numbers.count(i)
    if duplicate > 1:
        numbers.remove(i)
print(numbers)

# Mosh's Solution
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number no in uniques:
        uniques.append(number)
print(uniques)
