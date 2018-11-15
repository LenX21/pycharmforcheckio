class Warrior:
    """
    One on one duel
    Warrior calss, the instances of which will have 2 parameters:
    - health = 50 point
    - attack = 5 point
    - property = is_alive (True or False)
     In addition you have to create the second unit type - Knight,
     which should be the subclass of the Warrior but have the increased attack - 7.
     Also you have to create a function fight(), which will initiate the duel
     between 2 warriors and define the strongest of them.
    """
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def strike(self, attack):
        self.health = self.health - attack

    def damage(self):
        return self.attack

class Knight(Warrior):

    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7


def fight(*args):
    rivals = len(args)
    while rivals > 1:
        for num, warrior in enumerate(args):
            print(f' Who strike: {warrior} Who was bitten: {args[num-1]}')
            args[num - 1].strike(warrior.damage())
            if not args[num - 1].is_alive:
                rivals -= 1
                break

    print(args[0].is_alive)


if __name__ == '__main__':
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    fight(chuck, bruce)
    print(chuck.is_alive)
    # print(bruce.is_alive())
    #fight(dave, carl, bruce)
    #print(carl.is_alive())
    # print(dave.is_alive())
    # print(bruce.is_alive())


