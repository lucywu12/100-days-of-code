# 12/26 Weight Convertor + While Loops

weight = input('Weight: ')
type = input('(L)bs or (K)g: ')
weight = int(weight)

if type.upper() == "L":
    weight *= 0.45
    type = 'kilos'

elif type.upper() == "K":
    weight /= 0.45
    type = 'pounds'
else:
    print('Enter a valid type!')

print(f'You are {weight} {type}')
#--------------------------------------
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry! You failed!')
