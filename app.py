# 12/25 Arithmetic Rules + if statements + conditional operators
name = input("What is your name? ")

if len(name) < 2:
    print("Name must be at least 3 characters!")
elif len(name) > 49:
    print("Name can be a maximum of 50 characters!")
else:
    print("Name looks good!")
