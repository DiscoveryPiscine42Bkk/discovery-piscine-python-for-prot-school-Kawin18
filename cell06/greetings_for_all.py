def greetings(name="kawin Muechaiyapoomi"):

    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
