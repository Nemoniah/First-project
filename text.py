def intro():
    print("""
You are Lavender, a member of a mercenary band known as Stormcallers. Well, not really a member just yet.
Count Grimbald, the band's leader, gave you a test - to hunt down and defeat a certain spellblade.
It is but a test so the task isn't particularly dangerous and you've already tracked down your target to his lair.
From what you were told, the spellblade is fond of using puzzles to protect his property.
But one's puzzles can only be as challenging as one is intelligent and this particular isn't exactly the brightest light.
Puzzles most likely will not prove difficult.
It's quite interesting that your target is a spellblade - a mage uses spells as well as swords in combat.
You yourself are a spellblade, being able to use a sword and shock magic for offense and the same sword and mental magic
for defence.
You have a feeling you have everything you need to complete your task unscathed as all the enemy is known for is small-
time robbery and so he likely lacks the combat experience you have.
Enter?
""")


def intro_stalling():
    print("""
Standing around won't get the job done, you know.
Enter the lair and do what you gotta do?
    """)


def intro_try_leave():
    print("""
You consider leaving but getting here was a pain and you really dislike the idea of giving up now.
You're still standing in front of the entrance. Enter?
""")


def help_puzzle():
    print("To select an answer, type in either the answer or the corresponding letter.")


def help_fight():
    print("""
Finally, time to fight!
Type in attack to attack with Lavender's rapier.
Type in spell to use a lightning magic spell that shocks the enemy.
Type in parry to prepare to parry an incoming weapon attack.
Type in mental to interrupt an incoming spell cast using mental magic.
    """)


def first_puzzle_text():
    print("""
As soon as you enter, a spectral image of the spellblade appeared before you.
"Who dares enter the lair of the mighty Drago?!" it asked, trying to sound like a ghost. Or you guess trying to sound
like what its creator believed a ghost should sound.
"My name is Lavender. You got a bounty on your head for numerous armed robberies. Prepare to get your teeth kicked in."
"Oh, is that so?" laughed the image. "Well then, you're welcome to try to get past my riddles! I'll be waiting for you 
to kick YOUR teeth in!
The image disappeared, leaving you alone in a small hall with a door on the opposite end of it.
You walk up to the door and notice three small keyholes in it, a hanging from the handle key small enough to fit into the
keyholes and an inscription on the wall.

The inscription says:
"If you wish to enter you have to use the right keyhole!
One of them opens the door.
Another will make the earth swallow you whole.
And the last one will bring heaven's wrath upon you.
Here are tips to figure out which one does what but beware as all of them are lies!
The first one brings the wrath.
The keyholes that open the door and bring the gluttony are next to each other.
The third one will open the door."
You try bashing the door open but it's too sturdy. And it's covered with spell-reflecting runes. Not that you could
destroy it with shock spells to begin with. Looks like the key is your only option. So which keyhole will it be?
A. First
B. Second
C. Third
""")


def second_puzzle_text():
    print("""
You passed through the door into another hall. The spellblade's image once again appears before you.
"Well aren't you a smart one! But that was just the first puzzle!"
"Yeah yeah, whatever. Bring the second on already."
"Be careful what you wish for! Now listen up! There are three men: Kolbert, Wolfgang and Chris. One of them is a paladin,
another is a rogue and the last one's a bard! The paladin never lies, the rogue lies all the time and the bard just tells
whatever the hell he wants. Wolfgang says: "Chris is the rogue." Kolbert says: "Wolfgang is the paladin." Chris says:"I
am the bard." Who is the bard?"
So who's the bard?
A. Kolbert
B. Wolfgang
C. Chris
""")


def third_puzzle_text():
    print("""
You enter the third hall. This time there is a table with several bottles and a piece of paper in the middle of it. But 
before you make even a couple of steps toward the table a roaring wall of flame rose right behind you and quickly
encircled the whole hall, changing color as it reached the other end of it. That's definitely magical. And going into it
is likely a bad idea. You approach the table and pick up the paper. It says:

"Danger lies before you, while safety lies behind,
Two of us will help you, whichever you would find,
One among us seven will let you move ahead,
Another will transport the drinker back instead,
Two among our number hold only nettle wine,
Three of us are killers, waiting hidden in line.
Choose, unless you wish to stay here for evermore,
To help you in your choice, we give you these clues four:
First, however slyly the poison tries to hide
You will always find some on nettle wine's left side;
Second, different are those who stand at either end,
But if you would move onwards neither is your friend;
Third, as you see clearly, all are different size,
Neither dwarf nor giant holds death in their insides;
Fourth, the second left and the second on the right
Are twins once you taste them, though different at first sight."

You're getting a feeling you already read this in some book. Did the spellblade read it too and then recreate the puzzle?
Not that it would help you, since you definitely don't have it on you. You look at the potion bottles. So which one is it?
Going from left to right the bottles are:
A. Small white bottle
B. Large red bottle
C. Tiny blue bottle
D. Large yellow bottle
E. Small green bottle
F. Huge black bottle
G. Small purple bottle
""")


def meeting():
    print("""
Good news: it looks like you're in the final room. Bad news: you're met with a horryfying screech.
"How, how did you get past the last one?!"    
"Oh yeah, thanks for reminding me, I nearly forgot again. I have seveal question. Well, two, actually. First, did you
copy the last one from somewhere? Second, what's the deal with all the logic puzzles?"
You weren't really expecting your opponent to answer and he, indeed, didn't. Instead, he screeched again, this time
something not entirely intelligible, pulled out an estoc and rushed towards you.
You quikcly assess the situation. The opponent can use both magic and melee, as you were informed back at the Stormcaller
HQ, and wields an estoc. They're usually longer than rapiers but between this one being a bit on the shorter end and
your rapier being longer than normal, your weapons looked comparable. The estoc's heavier but judging by the spellblade's
movements he wasn't nearly as agile and trained as you are. Definitely winnable.
""")


def end():
    print("""
The spellblade's lying on the ground, unconscious. He was a bit more dangerous than you expected and didn't leave you in
the greatest shape but you should be right as rain after you slam down a few healing potions. More importantly, you've 
finally passed the test and are ready to join the Stormcallers!
CONGRATULATIONS!
All that's left is to either haul this guy all the way back or... 
""")
    quit()


def fight_lost():
    print("""
"Sho whose teeth got kicked in, huh?" laughs the spellblade.
You can't hear him though. You have died.
GAME OVER
""")


def first_puzzle_won():
    print("The door opens and you go in.")


def first_puzzle_lightning():
    print("""
As you're turning the key a lightning bolt shoots off the ceiling and hits you. You may be able to wield shock magic but
it doesn't come complete with shock resistance.
You have died.
GAME OVER
""")


def first_puzzle_floor():
    print("""
As you were turning the key the floor underneath you disappeared and you went falling... and falling... and falling...
Until you stopped.
You have died
GAME OVER
""")


def first_puzzle_stall():
    print("No matter how hard you look you can't find such a keyhole. It's gotta be one of those three")


def second_puzzle_won():
    print("""
The spellblade image makes an extremely displeased face and then disappears before you could tell it that this was way 
too similar to the previous puzzle. At the same time, the door at the end of this hall opens.
""")


def second_puzzle_lost():
    print("""
The spellbalde image starts to laugh manically.
"Ha! You imbecile! That is wrong!"
And as its laughing a massive stone plate drops from the ceiling and covers the entire hall.
You'd say something about not being an imbecile but that's pretty hard when you're flatter than a pancake.
You have died.
GAME OVER
""")


def third_puzzle_forward():
    print("""
You drank the potion. You're not dead so you assume it wasn't poison. Unless it kicks in slowly. Already good.
Which way to go?
A. Forward
B. Back
""")


def third_puzzle_forward_alive():
    print("You go forward and to your relief safely pass through the flame, leaving this hellscape.")


def third_puzzle_forward_dead():
    print("""
You go back and step into the flame. The look of a pile of ash does not suit you.
You have died.
GAME OVER
""")


def third_puzzle_invalid_direction():
    print(f"""
There are no doors in that direction and unfortunately you can't go through walls so you only have two options.
A. Forward
B. Back
""")


def third_puzzle_back():
    print("""
You drank the potion. You're not dead so you assume it wasn't poison. Unless it kicks in slowly. Already good.
Which way to go?
A. Forward
B. Back
""")


def third_puzzle_back_game_over():
    print("""
You safely pass through the flame at the door you just walked through. After you do that the flame there changes color
to the color of the flame at the other end of the hall. You can't go back and so you either have failed the test or will
have to wait in hopes the fire goes away someday.
GAME OVER
But hey, you got a game over without dying! Good job! Consider it an achievement or something.
""")


def third_puzzle_back_dead():
    print("""
You go forward and step into the flame. The look of a pile of ash does not suit you.
You have died.
GAME OVER
""")


def third_puzzle_wine():
    print("""
You drank the potion. You're not dead so you assume it wasn't poison. Unless it kicks in slowly. Already good.
You go forward and step into the flame. The look of a pile of ash does not suit you.
You have died.
GAME OVER
""")


def third_puzzle_poison():
    print("""
You drank the potion. More like the potion with an "s" and its third and fourth letters swapped. And a strong one at that.
You have died.
GAME OVER
""")


def third_puzzle_stalling():
    print("No matter how hard you look you can't find such a bottle. It's gotta be one of these seven.")