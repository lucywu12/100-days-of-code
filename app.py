# 12/27 Car Game

command = ''
started = False
stopped = False

while True:
    command = input('> ').upper()
    if command  == 'HELP':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif command == 'START':
        if started:
            print ("Car is already started!")
        else:
            started = True
            print('Car started...Ready to go!')
    elif command == 'STOP':
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print('Car stopped.')
    elif command == 'QUIT':
        break
    else:
        print("I don't understand that")
