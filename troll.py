from random import *
import time
race_words=["awesome.","cool.","good choice.","really.","come on.","horible choice."]
class_words=["boring.","ok.","not bad.","soso.","good.","meh."]
print("Welcome to troll")
print("Choose a race")
print("1: Dwarven")
print("2: Elven")
print("3: Human")
print("4: Gnomes")
monster = ({"attack":1,"defence":1,"damage":2,"hp":3,"armor":8})
race = input()
if race == "1":
    print("The Dwarven,",choice(race_words))
    race_dict = ({"defence":1,"attack":1,"damage":2,"hp":23,"armor":5})
if race == "2":
    print("The Elven,",choice(race_words))
    race_dict = ({"armor":2})
if race == "3":
    print("The Humans,",choice(race_words))
if race == "4":
    print("The Gnomes,",choice(race_words))
time.sleep(1)
print("Choose a class")
print("1: Fighter")
print("2: Rogue")
print("3: Bard")
print("4: Ranger")
_class = input()
if _class == "1":
    print("A Fighter,",choice(class_words))
if _class == "2":
    print("A Rogue,",choice(class_words))
if _class == "3":
    print("A Bard,",choice(class_words))
if _class == "4":
    print("A Ranger,",choice(class_words))
time.sleep(1)
def player_attack():
    monster["hp"]-= race_dict["damage"]
    monster["hp"]+=monster["defence"]
    print(monster["hp"])
def monster_attack():
    race_dict["hp"]-=monster["damage"]
    race_dict["hp"]+=race_dict["defence"]
    print(race_dict["hp"])
def battle():
    while race_dict["hp"] > 0 and monster["hp"] > 0:
        player_attack()
        monster_attack()
        time.sleep(1)
battle()
if race_dict["hp"] > monster["hp"]:
    print("Player wins")
else:
    print("Monster wins")