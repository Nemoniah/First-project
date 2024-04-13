import text

def first_puzzle():
    passed = False
    while not passed:
        answer = input("> ").lower()
        if answer == "a" or answer == "first":
            text.first_puzzle_won()
            passed = True
        elif answer == "b" or answer == "second":
            text.first_puzzle_lightning()
            exit()
        elif answer == "c" or answer == "third":
            text.first_puzzle_floor()
            exit()
        else:
            text.first_puzzle_stall()


def second_puzzle():
    passed = False
    while not passed:
        answer2 = input("> ")
        answer = answer2.lower()
        if answer == "a" or answer == "kolbert":
            text.second_puzzle_won()
            passed = True
        elif answer == "b" or answer == "wolfgang" or answer == "c" or answer == "chris":
            text.second_puzzle_lost()
            exit()
        else:
            print(f'''
"Who the hell is {answer2}?" The spellbalde image looks confused at first but then shrugs. "Eh, whatever. That's still
wrong. Damn, you're so stupid it's impressive!"
And just as it finishes a massive stone plate drops from the ceiling and covers the entire hall.
You'd say something about not being impressively stupid but that's pretty hard when you're flatter than a pancake.
You died.
GAME OVER
''')
            exit()


def third_puzzle():
    passed = False
    while not passed:
        answer = input("> ").lower()
        if answer == "c" or answer == "tiny blue bottle":
            text.third_puzzle_forward()
            direction = input("> ").lower()
            if direction == "forward" or direction == "a":
                text.third_puzzle_forward_alive()
                passed = True
            elif direction == "back" or direction == "b":
                text.third_puzzle_forward_dead()
                exit()
            else:
                text.third_puzzle_invalid_direction()
        elif answer == "g" or answer == "small purple bottle":
            text.third_puzzle_back()
            direction = input("> ").lower()
            if direction == "back" or direction == "b":
                text.third_puzzle_back_game_over()
                exit()
            if direction == "foward" or direction == "a":
                text.third_puzzle_back_dead()
                exit()
            else:
                text.third_puzzle_invalid_direction()
        elif answer == "b" or answer == "large red bottle" or answer == "f" or answer == "huge black bottle":
            text.third_puzzle_wine()
            exit()
        elif answer == "a" or answer == "d" or answer == "e" or answer == "small white bottle" or answer == "large yellow bottle" or answer == "small green bottle":
            text.third_puzzle_poison()
            exit()
        else:
            text.third_puzzle_stalling()


