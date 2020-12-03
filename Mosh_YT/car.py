started=False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started=True
            print("Car Started")
    elif command == "stop":
        if started == True:
            print("car stopped")
            started = False
        else:
             print("Car already stopped")
    elif command == "help":
        print("""1-START 
2-STOP
3-HELP""")
    elif command == "quit":
        break
    else:
        print("wrong input")
