import random


def player_input_numbers():
    while True:
        user_input = input('\nWhat is your number?\n')
        if user_input == 'exit game':
            return
        try:
            user_number = int(user_input)
        except ValueError:
            print("\nA string is not a valid input!\n")
            continue

        if user_number < 0:
            print("\nThe number can't be negative!\n")
            continue
        elif user_number > 1000000:
            print("\nInvalid input! The number can't be bigger than 1000000.\n")
            continue
        return user_number


def end_game(player_wins, robot_wins, draws):
    print(f'\nYou won: {player_wins},')
    print(f'Robot won: {robot_wins},')
    print(f'Draws: {draws}.')


class Numbers:
    player_wins = 0
    robot_wins = 0
    draws = 0

    def winner(self, number, user_number, robot_number):
        player_distance = abs(number - user_number)
        robot_distance = abs(number - robot_number)
        if player_distance < robot_distance:
            self.player_wins += 1
            print('You won!')
        elif robot_distance < player_distance:
            self.robot_wins += 1
            print('The robot won!')
        else:
            self.draws += 1
            print("It's a draw!")

    def game(self):
        while True:
            number = random.randint(0, 1000000)
            user_number = player_input_numbers()
            if not user_number:
                end_game(self.player_wins, self.robot_wins, self.draws)
                return
            robot_number = random.randint(0, 1000000)
            print(f'The robot entered the number {robot_number}.')
            print(f'The goal number is {number}.')
            self.winner(number, user_number, robot_number)


class RPS:
    player_wins = 0
    robot_wins = 0
    draws = 0
    options = ('rock', 'paper', 'scissors')

    def player_input(self):
        while True:
            user_input = input('\nWhat is your move?\n')
            if user_input == 'exit game':
                return
            elif user_input.lower() not in self.options:
                print('\nNo such option! Try again!')
                continue
            else:
                return user_input.lower()

    def winner(self, player_move, robot_move):
        if (player_move == 'rock' and robot_move == 'paper') or (player_move == 'paper' and robot_move == 'scissors') \
                or (player_move == 'scissors' and robot_move == 'rock'):
            self.robot_wins += 1
            print('The robot won!')
        elif (player_move == 'paper' and robot_move == 'rock') or (player_move == 'scissors' and robot_move == 'paper') \
                or (player_move == 'rock' and robot_move == 'scissors'):
            self.player_wins += 1
            print('You won!')
        else:
            self.draws += 1
            print("It's a draw!")

    def game(self):
        while True:
            player_move = self.player_input()
            robot_move = random.choice(self.options)
            if not player_move:
                end_game(self.player_wins, self.robot_wins, self.draws)
                return
            print(f'The robot chose {robot_move}')
            self.winner(player_move, robot_move)


class Robot:
    name = ''
    battery_level = 100
    overheat_level = 0
    skills_level = 0
    boredom_level = 0
    rust_level = 0

    def __init__(self):
        self.name = input('How will you call your robot?\n')

    def print_options(self):
        print(f'''Available interactions with {self.name}:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills''')

    def print_info(self):
        print(f'''
{self.name}'s stats are:
battery is {self.battery_level},
overheat is {self.overheat_level},
skill level is {self.skills_level},
boredom is {self.boredom_level},
rust is {self.rust_level}.
''')

    def check_stats(self):
        stats = [self.battery_level, self.overheat_level, self.skills_level, self.boredom_level, self.rust_level]
        for n in range(len(stats)):
            if stats[n] > 100:
                stats[n] = 100
            elif stats[n] < 0:
                stats[n] = 0
        self.battery_level, self.overheat_level, self.skills_level, self.boredom_level, self.rust_level = stats

    def recharge(self):
        if self.battery_level == 100:
            print(f'{self.name} is charged!')
        else:
            previous_battery = self.battery_level
            previous_overheat = self.overheat_level
            previous_boredom = self.boredom_level
            self.battery_level += 10
            self.overheat_level -= 5
            self.boredom_level += 5
            self.check_stats()
            print(f"{self.name}'s level of overheat was {previous_overheat}. Now it is {self.overheat_level}.")
            print(f"{self.name}'s level of the battery was {previous_battery}. Now it is {self.battery_level}.")
            print(f"{self.name}'s level of boredom was {previous_boredom}. Now it is {self.boredom_level}.")
            print(f'{self.name} is recharged!')

    def sleep(self):
        if self.overheat_level == 0:
            print(f'{self.name} is cool!')
        else:
            previous_overheat = self.overheat_level
            self.overheat_level -= 20
            self.check_stats()
            print(f'{self.name} cooled off!')
            print(f"{self.name}'s level of overheat was {previous_overheat}. Now it is {self.overheat_level}.")
            if self.overheat_level == 0:
                print(f'{self.name} is cool!')

    def play(self):
        while True:
            game_choice = input('Which game would you like to play?\n').lower()
            if game_choice == 'numbers':
                numbers = Numbers()
                numbers.game()
                break
            elif game_choice == 'rock-paper-scissors':
                rps = RPS()
                rps.game()
                break
            else:
                print('Please choose a valid option: Numbers or Rock-paper-scissors?')

        previous_boredom = self.boredom_level
        previous_overheat = self.overheat_level
        self.boredom_level -= 20
        self.overheat_level += 10
        self.check_stats()
        print(f"{self.name}'s level of boredom was {previous_boredom}. Now it is {self.boredom_level}.")
        print(f"{self.name}'s level of overheat was {previous_overheat}. Now it is {self.overheat_level}.")
        if self.boredom_level == 0:
            print(f'{self.name} is in a great mood!')

    def check_end(self):
        if self.overheat_level == 100:
            print(f'The level of overheat reached 100, {self.name} has blown up! Game over. Try again?')
            return True
        if self.rust_level == 100:
            print(f'{self.name} is too rusty! Game over. Try again?')
            return True

    def learning(self):
        if self.skills_level == 100:
            print(f"There's nothing for {self.name} to learn!")
        else:
            previous_skills = self.skills_level
            previous_overheat = self.overheat_level
            previous_battery = self.battery_level
            previous_boredom = self.boredom_level
            self.skills_level += 10
            self.overheat_level += 10
            self.battery_level -= 10
            self.boredom_level += 5
            self.check_stats()
            print(f"{self.name}'s level of skill was {previous_skills}. Now it is {self.skills_level}.")
            print(f"{self.name}'s level of overheat was {previous_overheat}. Now it is {self.overheat_level}.")
            print(f"{self.name}'s level of the battery was {previous_battery}. Now it is {self.battery_level}.")
            print(f"{self.name}'s level of boredom was {previous_boredom}. Now it is {self.boredom_level}.")
            print(f"{self.name} has become smarter!")

    def working(self):
        if self.skills_level < 50:
            print(f"{self.name} has got to learn before working!")
        else:
            previous_battery = self.battery_level
            previous_boredom = self.boredom_level
            previous_overheat = self.overheat_level
            self.battery_level -= 10
            self.boredom_level += 10
            self.overheat_level += 10
            self.check_stats()
            print(f"{self.name} did well!")
            print(f"{self.name}'s level of boredom was {previous_boredom}. Now it is {self.boredom_level}.")
            print(f"{self.name}'s level of overheat was {previous_overheat}. Now it is {self.overheat_level}.")
            print(f"{self.name}'s level of the battery was {previous_battery}. Now it is {self.battery_level}.")

    def unpleasant_event(self):
        previous_rust = self.rust_level
        if self.battery_level < 10:
            self.rust_level += 50
            print(f"Guess what! {self.name} fell into the pool!")
        elif self.battery_level < 30:
            self.rust_level += 10
            print(f"Oh no, {self.name} stepped into a puddle!")
        self.check_stats()
        print(f"{self.name}'s level of rust was {previous_rust}. Now it is {self.rust_level}.")

    def oil(self):
        if self.rust_level == 0:
            print(f"{self.name} is fine, no need to oil!")
        else:
            previous_rust = self.rust_level
            self.rust_level -= 20
            self.check_stats()
            print(f"{self.name}'s level of rust was {previous_rust}. Now it is {self.rust_level}")

    def main(self):
        while True:
            self.print_options()
            user_input = input('\nChoose:\n').lower()
            if user_input == 'exit':
                print('Game over.')
                break
            elif user_input == 'info':
                self.print_info()
            elif user_input == 'recharge':
                if self.boredom_level == 100:
                    print(f'{self.name} is too bored! {self.name} needs to have fun!')
                else:
                    self.recharge()
            elif user_input == 'sleep':
                if self.battery_level == 0:
                    print(f'The level of the battery is 0, {self.name} needs recharging!')
                elif self.boredom_level == 100:
                    print(f'{self.name} is too bored! {self.name} needs to have fun!')
                else:
                    self.sleep()
            elif user_input == 'play':
                if self.battery_level == 0:
                    print(f'The level of the battery is 0, {self.name} needs recharging!')
                else:
                    self.play()
                    self.unpleasant_event()
            elif user_input == 'learn':
                if self.battery_level == 0:
                    print(f'The level of the battery is 0, {self.name} needs recharging!')
                elif self.boredom_level == 100:
                    print(f'{self.name} is too bored! {self.name} needs to have fun!')
                else:
                    self.learning()
                    self.unpleasant_event()
            elif user_input == 'work':
                if self.battery_level == 0:
                    print(f'The level of the battery is 0, {self.name} needs recharging!')
                elif self.boredom_level == 100:
                    print(f'{self.name} is too bored! {self.name} needs to have fun!')
                else:
                    self.working()
                    self.unpleasant_event()
            elif user_input == 'oil':
                if self.battery_level == 0:
                    print(f'The level of the battery is 0, {self.name} needs recharging!')
                elif self.boredom_level == 100:
                    print(f'{self.name} is too bored! {self.name} needs to have fun!')
                else:
                    self.oil()
            else:
                print('Invalid input, try again!')
            if self.check_end():
                break


def main():
    robot = Robot()
    robot.main()


if __name__ == '__main__':
    main()
