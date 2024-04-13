import text
import puzzles
import combat

command = ""
game_won = False
text.intro()
text.help_puzzle()
while True:
    command = input("> ").lower()
    if command == "yes" or command == "enter":
        text.first_puzzle_text()
        puzzles.first_puzzle()
        text.second_puzzle_text()
        puzzles.second_puzzle()
        text.third_puzzle_text()
        puzzles.third_puzzle()
        text.meeting()
        text.help_fight()
        combat.fighting()
        text.end()
    elif command == "no" or command == "leave":
        text.intro_try_leave()
    else:
        text.intro_stalling()
