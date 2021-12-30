key_words = ("screen", "power", "wifi")
while True:
    user_input = input("Type: ")
    for word in user_input.split():
        if word in key_words and word == "screen":
            print("screen word found")
        elif word in key_words and word == "power":
            print("power word found")
