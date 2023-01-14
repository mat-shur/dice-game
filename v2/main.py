from random import randint


class Player:

    def __init__(self, name, die_inst, is_computer=False):
        self._counter = 3
        self._name = name
        self._die = die_inst
        self._is_computer = is_computer

    @property
    def counter(self):
        return self._counter

    @property
    def name(self):
        return self._name

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    def change_counter(self, win):
        self._counter += 1 if win else -1

    def roll_die(self):
        if not self._is_computer:
            input(f"\t{self._name}, press enter to roll ur dice!")
        else:
            print(f"\tComputer {self._name} rolls the dice!")

        self._die.roll()
        print(f"\t\tAfter throwing the dice, {self._name} got the number {self._die.value}!")


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        self._value = randint(1, 6)


class DiceGame:

    def __init__(self, *players):
        self._players = list(players)
        self._is_started = False
        self._rounds = 0
        self._losers = {}

    @property
    def is_started(self):
        return self._is_started

    def play(self):
        self._is_started = True
        print(f"The game between {' and '.join([player.name for player in self._players])} has begun!")

    def play_round(self):
        if not self._is_started:
            print("Before that you have to start the game!")
            return

        self._new_round()
        self._roll_dice()
        self._check_round_win()
        self._check_game_over()

        if not self._is_started:
            print("\n\n--- Game is over! ---")
            self._show_places()

    def _new_round(self):
        self._rounds += 1
        print(f"Round #{self._rounds}:")

    def _roll_dice(self):
        for player in self._players:
            player.roll_die()

        print("\t= The dice have been cast! =\n")

    def _check_round_win(self):
        print("\t= The numbers are counting now... =")

        max_die_value = self._players[0].die.value

        for player in self._players:
            if player.die.value > max_die_value:
                max_die_value = player.die.value

        if self._check_tie(max_die_value):
            print("\tNo one won this round.")
        else:
            for player in self._players:
                if player.die.value == max_die_value:
                    player.change_counter(True)
                    print(f"\t{'Player' if not player.is_computer else 'Computer'} {player.name} won!")
                    self._show_counter(player)
                else:
                    player.change_counter(False)
                    print(f"\t{'Player' if not player.is_computer else 'Computer'} {player.name} lost!")
                    self._show_counter(player)

    @staticmethod
    def _show_counter(player):
        print(f"\t\tHis counter: {player.counter}.")

    def _check_tie(self, max_die_value):
        for player in self._players:
            if player.die.value != max_die_value:
                return False

        return True

    def _check_game_over(self):
        for player in self._players:
            if player.counter == 0:
                print(f"\t{player.name} lost the game.")
                self._losers[player.name] = len(self._players)
                self._players.remove(player)

        if len(self._players) == 1:
            self._is_started = False

    def _show_places(self):
        print("\nPlaces:")
        print(f"\t1. {self._players[0].name}")

        for loser in dict(reversed(list(self._losers.items()))):
            print(f"\t{self._losers[loser]}. {loser}")


player1 = Player("Matthew", Die())
player2 = Player("Andrew", Die())
computer = Player("Tobby", Die(), is_computer=True)

dice_game = DiceGame(player1, player2, computer)
dice_game.play()

while dice_game.is_started:
    dice_game.play_round()
    print()

dice_game.play()
