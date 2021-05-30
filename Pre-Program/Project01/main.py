from Attacker import Attacker
from Defender import Defender
from GameOverException import GameOver


def main():
    """
    Risk game
    """
    print("*---------------------------------------*")
    ## print("Please enter the file path to translate: ")
    ## input_file = input()
    ## print("Translation to LOLSPEAK - Done")

    attacker = Attacker()
    defender = Defender()

    attacker.set_units(4)
    defender.set_units(3)

    print(attacker.get_units(), defender.get_units())

    while True:

        try:
            attacker_rolls = attacker.roll_dice()
            defender_rolls = defender.roll_dice()

            max_pairs = 0

            if attacker.get_max_rolls() < defender.get_max_rolls():
                max_pairs = attacker.get_max_rolls()
            else:
                max_pairs = defender.get_max_rolls()

            print(attacker_rolls, defender_rolls)

            for i in range(0, max_pairs):
                if attacker_rolls[i] > defender_rolls[i]:
                    defender.loses()
                elif attacker_rolls[i] < defender_rolls[i]:
                    defender.wins()
                else:
                    attacker.loses()
                print(i, attacker.get_units(), defender.get_units())

        except GameOver:
            print(attacker.get_units())
            print(defender.get_units())
            break

    if attacker.get_units() > defender.get_units():
        print("Attacker wins!")
    else:
        print("Defender wins!")


if __name__ == '__main__':
    main()
