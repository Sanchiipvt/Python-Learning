command = ""
while command.upper != "QUIT":
    command = input("> ")
    if command.upper() == "HELP":
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif command.upper() == "START":
        print('Car started...Ready to go!')
    elif command.upper() == "STOP":
        print('Car stopped.')
    elif command.upper() == "QUIT":
        break
    else:
        print("I don't understand.")
