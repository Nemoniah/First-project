import text

class Character:

    def __init__(self, name, hp, damage, spell_damage):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.damage = damage
        self.spell_damage = spell_damage
        self.turn_count = 0
        self.is_parrying = False
        self.is_interrupting = False
        self.is_preparing_attack = False
        self.is_preparing_spell = False

    def attack(self, target):
        if not target.is_parrying:
            target.hp -= self.damage
            target.hp = max(target.hp, 0)
            self.is_parrying = False
            self.is_interrupting = False
            print(f'{self.name} dealt {self.damage} damage with his weapon.')
            if target.is_interrupting:
                target.is_interrupting = False
                print(f"{target.name} lost concentration on the counter-spell!")
        else:
            print(f"{target.name} parried {self.name}'s attack.")
        self.turn_count += 1

    def spell(self, target):
        if not target.is_interrupting:
            target.hp -= self.spell_damage
            target.hp = max(target.hp, 0)
            self.is_parrying = False
            self.is_interrupting = False
            print(f"{self.name} dealt {self.spell_damage} damage with his spell.")
            if target.is_parrying:
                target.is_parrying = False
                print(f"{target.name} dropped his guard down!")
        else:
            print(f"{target.name} interrupted {self.name} spell.")
        self.turn_count += 1

    def charging_attack(self):
        print(f"{self.name} is looking for an opening.")
        self.is_preparing_attack = True
        self.is_parrying = False
        self.is_interrupting = False
        self.turn_count += 1

    def charged_attack(self, target):
        if not target.is_parrying:
            target.hp -= self.damage * 3
            target.hp = max(target.hp, 0)
            print(f"{self.name} dealt {self.damage * 3} damage with a charged attack.")
        else:
            print(f"{target.name} parried {self.name}'s charged attack.")
        self.is_preparing_attack = False
        self.turn_count += 1

    def charging_spell(self):
        print(f"{self.name} is looking focused.")
        self.is_preparing_spell = True
        self.is_parrying = False
        self.is_interrupting = False
        self.turn_count += 1


    def charged_spell(self, target):
        if not target.is_interrupting:
            target.hp -= self.spell_damage * 3
            target.hp = max(target.hp, 0)
            print(f"{self.name} dealt {self.spell_damage * 3} with a charged spell.")
        else:
            print(f"{target.name} interrupted {self.name}'s charged spell.")
        self.is_preparing_spell = False
        self.turn_count += 1

    def parry(self) -> None:
        self.is_parrying = True
        self.is_interrupting = False
        print(f"{self.name} is on the defensive.")
        self.turn_count += 1

    def counterspell(self):
        self.is_interrupting = True
        self.is_parrying = False
        print(f"{self.name} is looking out for the enemy spells.")
        self.turn_count =+ 1

def fighting():
    lavender = Character(name="Lavender", hp=100, damage=10, spell_damage=10)
    spellblade = Character(name="Spellblade", hp=150, damage=7, spell_damage=11)
    won = False
    while not won:
        if spellblade.hp < (spellblade.hp_max * 0.25):
            print("The spellblade looks scared and is focused on defence.")
            if spellblade.turn_count % 3 == 0:
                spellblade.counterspell()
            else:
                spellblade.parry()
        elif spellblade.is_preparing_attack:
            spellblade.charged_attack(lavender)
        elif spellblade.is_preparing_spell:
            spellblade.charged_spell(lavender)
        elif spellblade.turn_count % 4 == 0:
            spellblade.charging_spell()
        elif spellblade.turn_count % 5 == 0:
            spellblade.charging_attack()
        elif spellblade.turn_count % 2 == 0:
            spellblade.attack(lavender)
        else:
            spellblade.spell(lavender)
        print(f"Lavender's health:{lavender.hp}, Spellblade's health: {spellblade.hp}")
        if lavender.hp == 0:
            text.fight_lost()
            exit()
        elif spellblade.hp == 0:
            break
        action = input("> ").lower()
        if action == "attack":
            lavender.attack(spellblade)
        elif action == "spell":
            lavender.spell(spellblade)
        elif action == "parry":
            lavender.parry()
        elif action == "mental":
            lavender.counterspell()
        else:
            print("You fumble around and lose your turn.")
        if spellblade.hp == 0:
            print("You won!")
            won = True
