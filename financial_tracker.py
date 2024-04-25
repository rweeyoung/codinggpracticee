#this scripthas some error handling issues


from packaged_classes import Tracker, Trackertwo


first_input = None
second_input = None






while True:
    first_input = input("press 1 to make new tracker, press 2 to access existing tracker, press 3 to exit")
    try:
        first_input = int(first_input)
        if 1 > first_input or first_input > 3:
            print("input number within range")
            print("\n" * 3)
            continue
    except ValueError:
        print("input a number")
        print("\n" * 3)
        continue
    else:
        break


if first_input == 1:
    print("making new tracker for you now")
    x = input("what is the new name of your file: ").lower().strip()
    new_tracker = Tracker(x)
    new_tracker.pathtwo()


if first_input == 2:
    y = input("what is the existing name of your file").lower().strip()
    ytracked = Trackertwo(y)
    ytracked.pathtwo()



print("program finished running ")






