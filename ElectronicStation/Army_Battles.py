class Army:
    '''
    The battles occur according to the following principles:
    at first, there is a duel between the first warrior of the first army and the first warrior of the second army.
    As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel,
    and the surviving warrior continues to fight with his current health.
    This continues until all the soldiers of one of the armies die.
    '''

    def __init__(self):
        self.armyarray = []

    def add_units(self, type: object, amount: int):
        '''
        Add fighter to amy
        :return:
        '''
        for i in range(amount):
            self.armyarray.append(type())
        #print(self.armyarray)


class Battle:

    @staticmethod
    def fight(army1: Army, army2: Army):
        attacker = army1
        defender = army2

        while all([len(attacker.armyarray) > 0, len(defender.armyarray) > 0]):
            defender.armyarray[0].strike(attacker.armyarray[0].damage())
            if not defender.armyarray[0].is_alive:
                del defender.armyarray[0]
            attacker, defender = defender, attacker
        return len(army1.armyarray) != 0

