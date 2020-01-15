import random

class Ability(object):
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value


class Armor(object):
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self, max_block):
        random_value = max_block


class Hero(object):
    def __init__(self, name, starting_health = 100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor):
        self.armors.append(armor)
    
    def defend(self, damage_amt):
        defense = 0
        for armor in self.armors:
            defense += armor
        return defense

    def take_damage(self, damage):
        defense = self.defend(damage)
        self.current_health -= damage - defense
   
    def is_alive(self):
        if self.current_health <= 0:
            return True
        else:
            return False
    
    def fight(self, opponent):
        if self.abilities:
            if opponent.abilities:
                    while self.current_health > 0 and opponent.current_health > 0:
                        self.take_damage(opponent.attack())
                        print(self.current_health)
                        opponent.take_damage(self.attack())
                        print(opponent.current_health)
                    print("Hero 1: {}".format(self.is_alive()))
                    print("Hero 2: {}".format(opponent.is_alive()))
            else:
                print("no abilities!")
        else:
            print("no abilities!")



if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero2 = Hero("Samir Ingle", 100)
    ability2= Ability("software", 500)
    hero2.add_ability(ability2)
    hero.add_ability(ability)
    print(hero.abilities)
    hero.take_damage(hero.attack())
    print(hero.current_health)
    print(hero.is_alive())
    hero.fight(hero2)











