import numpy as np 


## Function 

# function of round
def r1(val):
    return round(val,1)

def r2(val):
    return round(val,2)

def r3(val):
    return round(val,3)

# function to calculate defense rate
def defense_rate(defense):
    # maximum defense is 100
    max_defense = 100

    # maximum defense rate is 95%
    max_defense_rate = 0.95

    # function of defense rate
    defense_rate = max_defense_rate * np.sqrt(defense/max_defense)
    return defense_rate


## Class

# Character class
class Character:
    def __init__(self, name, hp, mp, damage, defense):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.damage = damage
        self.defense = defense
        self.defenese_rate = defense_rate(defense) # defense damage factor 
        self.DDF = 1-self.defenese_rate # damage defense factor

    def attack(self, target):
        target.hp -= r1(self.damage)
        print(f'{self.name} attacked {target.name} for {self.damage:.1f} damage. {target.name} has {target.hp:.1f} HP left.')

    def skill(self, skill, target):
        target.hp -= r1(skill.damage)
        self.mp -= skill.mp_cost
        print(f'{self.name} used {skill.name} on {target.name} for {self.damage:.1f} damage. {target.name} has {target.hp:.1f} HP left.')
    
    def equipped(self, Equip):
        if Equip.defense == 0:
            self.damage += Equip.damage
            print(f'{self.name} equipped {Equip.name}. Damage increased to {self.damage:.1f}.')
        elif Equip.damage == 0:
            self.defense += Equip.defense
            self.DDF = 1.0 - defense_rate(self.defense)
            print(f'{self.name} equipped {Equip.name}. Defense increased to {self.defense}.')


class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        damage = self.damage*target.DDF
        target.hp -= damage
        print(f'{self.name} attacked {target.name} for {damage:.1f} damage. {target.name} has {target.hp:.1f} HP left.')

    def use_magic(self, target):
        pass

    def use_item(self, target):
        pass


class Skill:
    def __init__(self, name, damage, mp_cost):
        self.name = name
        self.damage = damage
        self.mp_cost = mp_cost


class Equipment:
    def __init__(self, name, damage, defense):
        self.name = name
        self.damage = damage
        self.defense = defense


# Character
P1 = Character('Hero', hp=100, mp=50, damage=10, defense = 10)
P2 = Character('Warrior', hp=150, mp=0, damage=15, defense = 20)
P3 = Character('Mage', hp=50, mp=100, damage=5, defense = 0)

# Skill
S1 = Skill('Fireball', damage=20, mp_cost=10)

# Monster
M1 = Monster('Goblin', hp=50, damage=5)
M2 = Monster('Orc', hp=100, damage=10)
M3 = Monster('Dragon', hp=200, damage=20)

# Equipment
W1 = Equipment('Sword', damage=15, defense=0)
A1 = Equipment('Helmet', damage=0, defense=10)


P1.equipped(W1)
M1.attack(P1)
P1.equipped(A1)
M1.attack(P1)
print("3")


