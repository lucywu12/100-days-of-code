# 1/2 Dictionaries

Phone_number = input("Phone: ")

Number = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for num in Phone_number:
    output += Number.get(num, "!") + " "
print(output)
