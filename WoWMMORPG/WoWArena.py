from WoWCharacters import Character
from random import randrange


class Arena:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def __str__(self):
        st = "(===============)\nTEAM A\n"
        for character in self.team1:
            st += str(character)
        st += "(===============)\nTEAM B\n"
        for character in self.team2:
            st += str(character)
        st += "(===============)"
        return st

    def __repr__(self):
        st = 'Arena('
        for character in self.team1:
            st += "[" + repr(character) + "]"
        st += "), ("
        for character in self.team2:
            st += "[" + repr(character) + "]"
        st += ")"
        return st

    def play(self):
        global defending
        time = -1
        while True:
            print(self)
            time += 1
            print("=" * 20)
            print(f'Time = {time}')
            print("=" * 20)

            # create list of character to play

            ready_characters = []
            for character in self.team1:
                if character.delay == 0:
                    ready_characters.append(("A", character))
            for character in self.team2:
                if character.delay == 0:
                    ready_characters.append(("B", character))

            # active characters attack

            for character in ready_characters:
                attacking = character[1]
                if character[0] == "A":
                    defending = self.team2[randrange(len(self.team2))]
                elif character[0] == "B":
                    defending = self.team1[randrange(len(self.team1))]
                damage = attacking.attack()
                defending.health -= damage
                print(f'{attacking.name} dealt {damage} damage to {defending.name}')

            # check for dead characters

            for pos in range(len(self.team1) - 1, -1, -1):
                if self.team1[pos].is_dead():
                    print(f'{self.team1[pos].name} is dead')
                    self.team1.pop(pos)
            for pos in range(len(self.team2) - 1, -1, -1):
                if self.team2[pos].is_dead():
                    print(f'{self.team2[pos].name} is dead')
                    self.team2.pop(pos)

            # check for winning team

            if len(self.team1) == 0:
                print('Team B has won!')
                break
            elif len(self.team2) == 0:
                print('Team A has won!')
                break

            # end round

            for character in self.team1:
                character.end_round()
            for character in self.team2:
                character.end_round()

            input("Press any key to continue: ")



