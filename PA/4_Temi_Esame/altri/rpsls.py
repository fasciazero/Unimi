'''The rules: "Scissors cuts paper, paper covers rock, rock crushes lizard,
lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard,
lizard eats paper, paper disproves Spock, Spock vaporizes rock,
and as it always has, rock crushes scissors.'''


class LizardSpock(type):
    def __new__(meta, classname, supers, classdict):
        def wrapper(self, *args):
            init(self, *args)
            self.__dict__['_wins_with'] = rules[classname]
                
        init = classdict['__init__']
        return type.__new__(meta, classname, supers, classdict | {'__init__': wrapper})


class Play(metaclass=LizardSpock):
    def __init__(self): pass

    def __str__(self):
        return self.__class__.__name__

    def __gt__(self, other):
        return other.__class__ in self._wins_with

    def __lt__(self, other):
        return \
            not self.__gt__(other) and \
                not self.__class__ == other.__class__


class Rock(Play):
    def __init__(self):
        self._wins_with = [Scissors]


class Scissors(Play): 
    def __init__(self):
        self._wins_with = [Paper]


class Paper(Play):
    def __init__(self):
        self._wins_with = [Rock]


class Lizard(Play):
    def __init__(self):
        pass


class Spock(Play):
    def __init__(self):
        pass


rules = {
    'Rock': [Lizard, Scissors],
    'Paper': [Rock, Spock],
    'Scissors': [Paper, Lizard],
    'Lizard': [Paper, Spock],
    'Spock': [Rock, Scissors]
}


if __name__ == '__main__':
    
    player_1 = Lizard()
    player_2 = Spock()

    if player_1 < player_2:
        print('{0} vs {1} -> player_2 wins'.format(player_1, player_2))
    else:
        if player_1 > player_2:
            print('{0} vs {1} -> player_1 wins'.format(player_1, player_2))
        else:
            print('{} vs {} -> draw'.format(player_1, player_2))
    