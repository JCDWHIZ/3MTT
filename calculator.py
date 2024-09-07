def calculation():
    value1 = int(input("Insert first Number "))
    value2 = int(input("Insert first Number "))
    action = input("what will you like to do with the numbers ")

    if action == "add":
        print(f"The addition of {value1} and {value2} is {value1 + value2}")
    elif action == "subtract":
        print(f"The subtraction of {value1} from {value2} is {value1 - value2}")
    elif action == "divide":
        print(f"The addition of {value1} and {value2} is {value1 / value2}")
    elif action == "multiply":
        print(f"The multiplication of {value1} and {value2} is {value1 * value2}")
    else:
        print("Insert a correct action")


calculation()