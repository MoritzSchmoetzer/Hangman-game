import random

letters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
word_list = ("python", "java", "kotlin", "javascript")

while True:
    print("H A N G M A N\n")
    menu_input = input('Type "play" to play the game, "exit" to quit: ')
    if menu_input == "play":
        entered_letters = []
        i = 0
        number_letters = []
        random_word = random.choice(word_list)
        random_word_set = set(random_word)
        hint = "-" * len(random_word)
        print()
        while i <= 8:
                # If the word is exposed the program ends
                if "-" not in hint:
                    print()
                    print(hint)
                    print("You guessed the word!")
                    print("You survived!")
                    print()
                    break

                print(hint)
                guess_letter = input("Input a letter: ")

                # Error query
                if len(guess_letter) > 1:
                    print("You should input a single letter")
                    # If the user used up his attempts the program ends
                    if i == 8:
                        print("You are hanged!")
                        print()
                        break
                    print()
                    continue
                elif guess_letter not in letters:
                    print("It is not an ASCII lowercase letter")
                    # If the user used up his attempts the program ends
                    if i == 8:
                        print("You are hanged!")
                        print()
                        break
                    print()
                    continue
                elif guess_letter in entered_letters:
                    print("You already typed this letter")
                    # If the user used up his attempts the program ends
                    if i == 8:
                        print("You are hanged!")
                        print()
                        break
                    print()
                    continue
                elif guess_letter not in random_word_set:
                    print("No such letter in the word")
                    i += 1
                    entered_letters.append(guess_letter)
                    # If the user used up his attempts the program ends
                    if i == 8:
                        print("You are hanged!")
                        print()
                        break
                    print()
                    continue

                # Main part
                if guess_letter in random_word_set:
                    index = 0
                    for letter in random_word:
                        if letter == guess_letter:
                            number_letters.append(index)
                        index += 1
                    for digit in number_letters:
                        # "-" gets replaced by guess_letter
                        hint = hint[:digit] + guess_letter + hint[digit + 1:]
                    number_letters.clear()
                print()
                entered_letters.append(guess_letter)
    elif menu_input == "exit":
        break