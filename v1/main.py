import random


class Die:

    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    def roll(self):
        self._value = random.randint(1, 6)


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def die(self):
        return self._die

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        self._die.roll()


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        self._print_welcome()

        while True:
            self._play_round()

            if self._check_game_over():
                break

    def _play_round(self):
        self._print_new_round()
        self._roll_dice()
        self._show_dice()

        match self._check_round_result():
            case 1:
                print("You won this round! 🎉")
                self._update_counters(winner=self._player, loser=self._computer)
            case 0:
                print("The computer won this round. 😥 Try again.")
                self._update_counters(winner=self._computer, loser=self._player)
            case -1:
                print("It's a tie! 😎")

        self._show_counters()

    def _roll_dice(self):
        self._player.roll_die()
        self._computer.roll_die()

    @staticmethod
    def _print_welcome():
        print("=============================")
        print("🎲 Welcome to Roll the Dice!")
        print("=============================")

    @staticmethod
    def _print_new_round():
        print("\n------ New Round ------")
        input("🎲 Press any key to roll the dice.🎲 ")

    def _show_dice(self):
        print(f"Your die: {self._player.die.value}")
        print(f"Computer die: {self._computer.die.value}\n")

    def _show_counters(self):
        print(f"\nYour counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")

    @staticmethod
    def _update_counters(winner, loser):
        winner.increment_counter()
        loser.decrement_counter()

    def _check_round_result(self):
        if self._player.die.value > self._computer.die.value:
            return 1
        elif self._computer.die.value > self._player.die.value:
            return 0
        else:
            return -1

    def _check_game_over(self):
        if self._player.counter == 0:
            self._show_game_over(winner=self._computer)
            return True
        elif self._computer.counter == 0:
            self._show_game_over(winner=self._player)
            return True
        else:
            return False

    @staticmethod
    def _show_game_over(winner):
        if winner.is_computer:
            string = "The computer won the game. Sorry..."
        else:
            string = "You won the game! Congratulations"

        print("\n=====================")
        print(" G A M E   O V E R ✨")
        print("=======================")
        print(string)
        print("=======================")


player_die = Die()
computer_die = Die()

my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

game.play()
