def interface():
    print("Blood calculator")
    keep_running = True
    while keep_running: 
        print("Make a choice")
        print("9 - Quit")
        choice = input("Make a choice: ")
        if int(choice) == 9:
            keep_running = False
    print(choice)
    return choice

interface()
