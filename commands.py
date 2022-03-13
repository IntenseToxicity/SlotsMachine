import main


def help():
    print(f'''
Welcome to help. All available options are:
"help or ?" are options for Help.
"about or info" are options for the version and about information.
"quit, leave, walk, or walk away" are options to end game.
"Rules, Instructions, I, or R" are options for the rules and instructions of the game.
"check, wallet, or money" are options to view your wallet/funds.
"no or n" are options to not continue playing. Similar to quit.
"yes or y" are options to play another round.
If you want to change the default values, open the hidden folder .Slots in the same directory the exe is in.
''')


def rules():
    """
    This function stores the game's rules and provides them when requested.
    :return: The game rules
    """
    print(f'''
Welcome to Python Slots!

Answer with yes or no. You can type ? for more options.
There is no case sensitivity, type it however you like!

To win you must get one of the following combinations:
BAR\tBAR\tBAR\t\tpays\t{main.SlotMachine.currency}{main.configuration.conf.get('Reel_Payouts', 'BAR')}
BELL\tBELL\tBELL/BAR\tpays\t{main.SlotMachine.currency}{main.configuration.conf.get('Reel_Payouts', 'BELL')}
PLUM\tPLUM\tPLUM/BAR\tpays\t{main.SlotMachine.currency}{main.configuration.conf.get('Reel_Payouts', 'PLUM')}
ORANGE\tORANGE\tORANGE/BAR\tpays\t{main.SlotMachine.currency}{main.configuration.conf.get('Reel_Payouts', 'ORANGE')}
LEMON\tLEMON\tLEMON\tpays\t{main.SlotMachine.currency}{main.configuration.conf.get('Reel_Payouts', 'LEMON')}
CHERRY\tCHERRY\tCHERRY\t\tpays\t{main.SlotMachine.currency}{main.configuration.conf.get('CHERRY_PAYOUTS', '3_CHERRY')}
CHERRY\tCHERRY\t  -\t\tpays\t{main.SlotMachine.currency}{main.configuration.conf.get('CHERRY_PAYOUTS', '2_CHERRY')}
CHERRY\t  -\t  -\t\tpays\t{main.SlotMachine.currency}{main.configuration.conf.get('CHERRY_PAYOUTS', '1_CHERRY')}
7\t  7\t  7\t\tpays\t The Jackpot!
''')


def about():
    print(f'''
Welcome to the Python Slots about page.

\033[1mCreated by:\033[0;0m\t\tJames Dandy
\033[1mRevision date:\033[0;0m\t11 March 2022
\033[1mDescription:\033[0;0m\tA basic slot machine game.
\033[1mLicense:\033[0;0m\t\tCreative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License 
\033[1mVersion:\033[0;0m\t\t1.0.2

Thank you to everyone who plays this and especially to those who supported me while I learned python and made this.
\t- James Dandy
''')


def where_stored():
    print(f'''
Slots stores configuration and save information in %appdata%\\InsanityNet\\.Slots\\
''')

