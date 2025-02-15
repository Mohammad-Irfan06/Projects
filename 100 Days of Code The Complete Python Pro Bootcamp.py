print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure. ")
choice1 = input('you\'re at a crossroad, where do you want to go? Type "left" or "right".')
if choice1 == "left":
    choice2 = input('you\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.')
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "One yellow and blue. "
                        "Which colour do you choose?")
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. you Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")

elif choice1 == "right":
    choice2 = input('You carefully walk down the right path and see an old bridge. Do you "cross" it or "turn back"?')
    if choice2 == "cross":
        choice3 = input("You discover a hidden library filled with ancient knowledge. You Win!")
    else:
        print("You get lost trying to leave. Game Over.")
else:
    print("Invalid choice. Game Over.")