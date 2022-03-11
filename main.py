import random
import time
import os
from enum import Enum
import configparser
import configuration
import saves

"""
Name: Python Slots
Description:
    This is a slot game produced in Python. 
    It uses a config file.
    It has one (1) save file currently.
"""
global NEW_USER_FLAG
global start_flag
start_flag = True

config = configuration.conf
config.read('.Slots\\Slot_settings.ini')


# TODO: find a way to allow multiple saves and
#  keep SlotMachine Jackpot same through all members.

def rules():
    """
    This function stores the game's rules and provides them when requested.
    :return: The game rules
    """
    rules_str = f'''
Welcome to Python Slots!

Answer with yes or no. You can type ? for more options.
There is no case sensitivity, type it however you like!

To win you must get one of the following combinations:
BAR\tBAR\tBAR\t\tpays\t{SlotMachine.currency}{configuration.conf.get('Reel_Payouts', 'BAR')}
BELL\tBELL\tBELL/BAR\tpays\t{SlotMachine.currency}{configuration.conf.get('Reel_Payouts', 'BELL')}
PLUM\tPLUM\tPLUM/BAR\tpays\t{SlotMachine.currency}{configuration.conf.get('Reel_Payouts', 'PLUM')}
ORANGE\tORANGE\tORANGE/BAR\tpays\t{SlotMachine.currency}{configuration.conf.get('Reel_Payouts', 'ORANGE')}
LEMON\tLEMON\tLEMON\tpays\t{SlotMachine.currency}{configuration.conf.get('Reel_Payouts', 'LEMON')}
CHERRY\tCHERRY\tCHERRY\t\tpays\t{SlotMachine.currency}{configuration.conf.get('CHERRY_PAYOUTS', '3_CHERRY')}
CHERRY\tCHERRY\t  -\t\tpays\t{SlotMachine.currency}{configuration.conf.get('CHERRY_PAYOUTS', '2_CHERRY')}
CHERRY\t  -\t  -\t\tpays\t{SlotMachine.currency}{configuration.conf.get('CHERRY_PAYOUTS', '1_CHERRY')}
7\t  7\t  7\t\tpays\t The Jackpot!
'''
    return rules_str


class SlotMachine:  # Main Class
    # Configure configparser and read the config file [INI file].

    currency = configuration.currencytype()

    # Configure the global variables from the config file.
    INITIAL_STAKE = int(config.get('Initial_Values', 'INITIAL_STAKE'))  # Wallet start value from config file.
    INITIAL_JACKPOT = int(config.get('Initial_Values', 'INITIAL_JACKPOT'))  # Jackpot start value from config file.

    class Reel(Enum):  # What each potential reel value coresponds to in decimal.
        CHERRY = 1
        LEMON = 2
        ORANGE = 3
        PLUM = 4
        BELL = 5
        BAR = 6
        SEVEN = 7

    _values = list(Reel)  # See above.

    # [Below] Pulls from the above config ini file to determine the values. See that file.
    payout_values = configuration.payout_values()

    payout = {
        Reel.CHERRY: int(payout_values[0]),
        Reel.LEMON: int(payout_values[1]),
        Reel.ORANGE: int(payout_values[2]),
        Reel.PLUM: int(payout_values[3]),
        Reel.BELL: int(payout_values[4]),
        Reel.BAR: int(payout_values[5]),
        Reel.SEVEN: str(payout_values[6])
    }  # What the values of a win should be based on the reel. Additional conditions are in keep_playing().

    def __init__(self, stake=INITIAL_STAKE, jackpot=INITIAL_JACKPOT):  # Initialization
        """
        Initialization information.

        :param stake: Sets Wallet value from Global default.
        :param jackpot: Sets machine Jackpot value from Global default.
        """
        self.current_stake = stake  # Set values for initial wallet from Global default.
        self.current_jackpot = jackpot  # Set values for initial Jackpot from Global default.

    @property
    def keep_playing(self):  # Continue playing, as per the function property.
        """
        This function checks between games to see if user wishes to continue playing,
        check their wallet, check the rules, or quit the game.

        :return: Boolean True or Boolean False.
        """
        while True:  # Constant loop until new game or quit.

            # If the slot machine has $1 or less, "refill" it.
            if self.current_jackpot <= 1:
                print("Machine balance reset.")  # Print a refill/reset message.
                self.current_jackpot = SlotMachine.INITIAL_JACKPOT  # Reset the slot machine Jackpot to global default.

            print(f"The Jackpot is currently: {self.currency}{self.current_jackpot}.")  # Print current Jackpot amount.

            # Does the player wish to continue playing, check their money, see the rules, or quit?
            answer = input("Would you like to [P]lay, check your money, or see the rules? ").lower()

            # User input checks.
            if answer in ["yes", "y", "play", ""]:  # If yes, clear console, return TRUE
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear Console
                return True  # Return TRUE

            elif answer in ["no", "n", "quit", "leave", "walk", "walk away"]:  # Print current wallet, return FALSE
                print(f"\nYou ended the game with {self.currency}{self.current_stake} in your hand. Great job!")

                if save_value == 0:
                    saves.save_information(
                        self.current_jackpot,
                        self.current_stake,
                        configuration.conf.get('saveOne', 'name'),
                        0
                    )
                elif save_value == 1:
                    saves.save_information(
                        self.current_jackpot,
                        self.current_stake,
                        configuration.conf.get('saveTwo', 'name'),
                        1
                    )
                else:
                    saves.save_information(
                        self.current_jackpot,
                        self.current_stake,
                        configuration.conf.get('saveThree', 'name'),
                        2
                    )

                time.sleep(5)  # Don't quit immedietely. Let the player see what they ended with.
                return False  # No new rounds. End Game.

            elif answer in ["check", "wallet", "money"]:  # If check wallet, clear console, print wallet.
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear Console
                print(f"\nYou currently have {self.currency}{self.current_stake}.")  # Print Wallet.

            elif answer in ["rules", "instructions", "r", "i"]:  # If see rules, clear console, print rules.
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear console.
                print(rules())  # Print the rules

            elif answer in ["?", "help"]:
                print(f'''
Welcome to help. All available options are:
"help or ?" are options for Help.
"quit, leave, walk, or walk away" are options to end game.
"Rules, Instructions, I, or R" are options for the rules and instructions of the game.
"check, wallet, or money" are options to view your wallet/funds.
"no or n" are options to not continue playing. Similar to quit.
"yes or y" are options to play another round.
If you want to change the default values, open the hidden folder .Slots in the same directory the exe is in.
''')

            else:  # If not a proper answer, print error.
                print("Whoops! Didn't get that.")  # Print Error

    def _play_round(self):
        """
        This function randomly selects the three reels/values used to determine win or loss.

        :return: Sends the randomly selected values to the _adjust_score() function to determine win or loss.
        """
        # Randomly chooses the slot machine values for first, second, and third reels.
        first, second, third = random.choice(SlotMachine._values),\
                                random.choice(SlotMachine._values),\
                                random.choice(SlotMachine._values)

        # Sends the values first, second, and third to the _adjust_score function to determin win or loss.
        self._adjust_score(first, second, third)

    def _adjust_score(self, first, second, third):
        """
        This function receives input from _play_round. It takes the inputs and determines win or loss.

        :param first: Reel one
        :param second: Reel two
        :param third: Reel three
        :return: new wallet amount.
        """
        # Prize determination
        if first == SlotMachine.Reel.CHERRY:  # IF first reel IS CHERRY

            if second == SlotMachine.Reel.CHERRY:  # If CHERRY, CHERRY, ANY then win 5
                win = int(configuration.conf.get('CHERRY_PAYOUTS', '3_CHERRY')) \
                    if third == SlotMachine.Reel.CHERRY \
                    else int(configuration.conf.get('CHERRY_PAYOUTS', '2_CHERRY'))  # IF CHERRY, CHERRY, CHERRY THEN win 7
            else:
                win = int(configuration.conf.get('CHERRY_PAYOUTS', '1_CHERRY'))  # IF CHERRY, ANY, ANY THEN win 2

        else:  # IF first reel NOT CHERRY
            if first == second == third:  # IF all reels are SAME
                win = self.payout[first]  # Use the first reel to determine win value.
                # [Below] IF all reels are SEVEN THEN the win is the Jackpot amount.
                win = self.current_jackpot if win == '\'jackpot\'' else win
            else:  # IF NOT any other condition, loss $1
                win = -1  # Loss $1

        # Jackpot win conditions
        if win == self.current_jackpot:  # If player won the Jackpot.
            print("\nYou won the JACKPOT!!\n")  # Print they won the Jackpot.
            self.current_stake += win  # give them their money!
        else:
            print()  # Blank Line time!
            # [Below] print the three reels to show user what values were selected.
            print('\t'.join(map(lambda x: x.name.center(6), (first, second, third))))
            # [Below] print that they won or lost x dollars with proper formatting.
            print("\nYou {} {}{}\n".format("won" if win > 0 else "lost", self.currency, win))
            self.current_stake += win  # Increment their Wallet.
            self.current_jackpot -= win  # Decrement the Jackpot.

    def play(self):
        """
        While the player still has money and chooses to play another round, run _play_round function.

        :return: another round.
        """
        global start_flag
        if start_flag == True:
            if save_value == 0:
                self.current_stake = int(configuration.conf.get('saveOne', 'wallet'))
                while True:
                    try:
                        self.current_jackpot = int(configuration.conf.get('MACHINE', 'jackpot'))
                        break
                    except configparser.NoSectionError:
                        self.current_jackpot = int(configuration.conf.get('Initial_Values', 'initial_jackpot'))
                        break
                start_flag = False
            elif save_value == 1:
                self.current_stake = int(configuration.conf.get('saveTwo', 'wallet'))
                self.current_jackpot = int(configuration.conf.get('MACHINE', 'jackpot'))
            elif save_value == 2:
                self.current_stake = int(configuration.conf.get('saveThree', 'wallet'))
                self.current_jackpot = int(configuration.conf.get('MACHINE', 'jackpot'))
            else:
                self.current_stake = int(configuration.conf.get('Initial_Values', 'initial_stake'))
                self.current_jackpot = int(configuration.conf.get('Initial_Values', 'initial_jackpot'))
                NEW_USER_FLAG = False
        while self.current_stake and self.keep_playing:
            if self.current_stake > 1:  # If money left, keep playing
                self._play_round()
            # Reset without a restart. Then reset the new user flag.
            else:
                loan = input(f"Do you wish to add another {self.currency}50? ").lower()  # Ask if they want more money.
                if loan in ["yes", "y"]:
                    self.current_stake += 50  # Add more money
                    continue  # Continue while loop
                else:
                    quit(0)  # Otherwise, quit.


# If this is run on its own and not as a library, print rules, ask if they want to play, and begin the slots game.
if __name__ == '__main__':
    # Debug
    class Debug:
        if config.get('Debug', 'Type') == '1':
            payout_values = configuration.payout_values()

            print(f"Payout Values are:"
                  f"Cherry: {payout_values[0]}"
                  f"Lemon: {payout_values[1]}"
                  f"Orange: {payout_values[2]}"
                  f"Plum: {payout_values[3]}"
                  f"Bell: {payout_values[4]}"
                  f"Bar: {payout_values[5]}"
                  f"Seven: {payout_values[6]}"
                  f"[End of Payout Values]\n")


    # [Below] Print the rules initially.
    print(rules())  # Print the rules

    # Get user input and validate. + loading or resetting of save.
    while True:
        try:
            # Confirm they read the rules/instructions and ask if they want to play.
            # Then set response to lowercase.
            start = input("Having read the above, do you wish to play? [Y]es or No ").lower()
            print()  # Spacing

            # If they agree to the rules and/or the instructions, clear the console and run the slot game.
            if start in ["yes", "y", ""]:
                while True:
                    try:
                        # Get the player name. AKA the save slot.
                        print(f"Saves:\n"
                              f"Slot 1: {configuration.saves()[0]}\n"
                              f"Slot 2: {configuration.saves()[1]}\n"
                              f"Slot 3: {configuration.saves()[2]}\n")
                        save_slot = input("Which save do you wish to load? ").capitalize()

                        # If the name matches save, welcome them back and exit loop.
                        save_value = 0  # Initialize save_value
                        if save_slot.lower() in ['one', '1', 'two', '2', 'three', '3']:  # Check if valid choice
                            print(f"Loading save slot {save_slot}.")
                            if save_slot.lower() in ['one', '1']:
                                save_value = 0
                            elif save_slot.lower() in ['two', '2']:
                                save_value = 1
                            elif save_slot.lower() in ['three', '3']:
                                save_value = 2

                            if configuration.saves()[save_value] in ['one', 'One', 'two', 'Two', 'three', 'Three']:
                                choice = input(f"Do you wish to rename your save? ")
                                if choice.lower() in ['yes', 'y']:
                                    rename = input(f"What do you want to name your save? ")
                                    if save_value == 0:
                                        configuration.conf.set('saveOne', 'name', rename)
                                    elif save_value == 1:
                                        configuration.conf.set('saveTwo', 'name', rename)
                                    elif save_value == 2:
                                        configuration.conf.set('saveThree', 'name', rename)

                                    with open('.Slots/Slot_settings.ini', 'w') as configfile:
                                        configuration.conf.write(configfile)
                            break

                        # If the name is blank, reask for name.
                        elif save_slot == '':
                            print(f"\nI didn't catch that. Please reenter your name.")
                            continue

                        # If not existing save name, ask if they want to overwrite
                        else:
                            # Print a welcome message
                            print(f"Invalid Choice.")
                            continue

                    except configparser.NoOptionError:  # If Options missing from Config/Save File.
                        print(f"[CRITICAL] Please let developer know the following:"
                              f"config error: NoOptionError"
                              f"save data")
                        quit(1)

                    except configparser.NoSectionError:  # If Section missing from Config/Save File.
                        print(f"[CRITICAL] Please let developer know the following:"
                              f"config error: NoSectionError"
                              f"save data")
                        quit(1)

                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console.
                SlotMachine().play()  # Call main function, start the game.

            elif start not in ['yes', 'no', 'y', 'n', 'quit', 'q']:
                print(f"I didn't catch that.\n")
                continue

            # If they don't want to play, or don't agree to the rules, quit the program.
            elif start in ['no', 'n', 'quit', 'q']:
                quit(0)  # Quit the program.

        except ValueError:  # If there is an error in the user input, reask them.
            continue  # continue the loop.

        break  # If no error, break the loop.
# End of Script.
