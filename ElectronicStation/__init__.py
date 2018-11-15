from Army_Battles import Army, Battle
from thewarriors import Warrior, Knight


if __name__ == '__main__':
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    a = Army()
    a.add_units(Warrior, 3)

    my_amy = Army()
    my_amy.add_units(Warrior, 4)
    my_amy.add_units(Knight, 2)

    enemy_army = Army()
    enemy_army.add_units(Knight, 3)
    battle = Battle()
    print(battle.fight(my_amy, enemy_army))


    print(my_amy.armyarray)
    print(enemy_army.armyarray)
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 20)
    army_2.add_units(Warrior, 21)
    battle = Battle()
    print(battle.fight(army_1, army_2))