# 12/29 Nested Loops + Lists
# This is my solution, which is not what Mosh wanted :(
numbers = [5, 2, 5, 2, 2]

for times in numbers:
    print('x'* times)

# This is the 'correct' solution
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#Greatest number calculator
numbers_list = [123, 67, 2, 942]
max = numbers_list[0]

for i in numbers_list:
    if i > max:
        max = i
print(max)
