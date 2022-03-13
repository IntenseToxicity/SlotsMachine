import os
import ctypes
import configparser

conf = configparser.ConfigParser(comment_prefixes='/', allow_no_value=True)

dir_path = '%s\\InsanityNet' % os.environ['APPDATA']

if not os.path.exists(f'{dir_path}\\Python_Slots_Settings.ini'):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ret = ctypes.windll.kernel32.SetFileAttributesW('.Slots', FILE_ATTRIBUTE_HIDDEN)
    conf['Initial_Values'] = {
        '; Your initial wallet. Default is 50': None,
        'INITIAL_STAKE': '50',
        '; The machine\'s default Jackpot amount. Default is 1000': None,
        'INITIAL_JACKPOT': '1000'}

    conf['Reel_Payouts'] = {
        '; Cherry default is 7': None,
        'CHERRY': '7',
        '; Lemon default is 10': None,
        'LEMON': '10',
        '; Orange default is 14': None,
        'ORANGE': '14',
        '; Plum default is 20': None,
        'PLUM': '20',
        '; Bell default is 35': None,
        'BELL': '35',
        '; Bar default is 250': None,
        'BAR': '250',
        '; Seven default is \'jackpot\'.': None,
        '; This option should not be changed.': None,
        '; It is here if you WANT to.': None,
        '; DO NOT BUG REPORT THIS IF ISSUES ARISE!': None,
        '; If you do, I will mark is closed.': None,
        'SEVEN': '\'jackpot\''}

    conf['CHERRY_PAYOUTS'] = {
        '; This section is for the cherry sub values.': None,
        '; These override the above cherry, above cherry is there to prevent errors.': None,
        '; I will clean it up in a future version.': None,
        '3_CHERRY': '7',
        '2_CHERRY': '5',
        '1_CHERRY': '2'}

    conf['CURRENCY'] = {
        '; You can change to your local currency by replacing $ with yours.': None,
        '; Only the following work right now': None,
        '; Dollar, Euro, Pound Sterling, Rupee, Rial': None,
        '; Sheqel, Yen, Won, Kip, Tugrik, Naira, Peso': None,
        'TYPE': 'Dollar'
    }

    conf['saveOne'] = {
        '; Do not edit this section please.': None,
        '; I have yet to learn how to encrypt this to prevent cheating.': None,
        'Name': 'One',
        'Wallet': '50',
    }

    conf['saveTwo'] = {
        '; Do not edit this section please.': None,
        '; I have yet to learn how to encrypt this to prevent cheating.': None,
        'Name': 'Two',
        'Wallet': '50',
    }

    conf['saveThree'] = {
        '; Do not edit this section please.': None,
        '; I have yet to learn how to encrypt this to prevent cheating.': None,
        'Name': 'Three',
        'Wallet': '50',
    }

    conf['Debug'] = {
        '; Debug testing. Set to 1 to show debug messages.': None,
        'Type': '0'
    }

    with open(f'{dir_path}\\Python_Slots_Settings.ini', 'w') as configfile:
        conf.write(configfile)

else:
    conf.read(f'{dir_path}\\Python_Slots_Settings.ini')


# ------------------- CURRENCY TYPE -------------------------
def currencytype():
    """
    This function determines the currency type and symbol from the config file.
    :return: the currency type and symbol.
    """
    currency = conf.get('CURRENCY', 'TYPE')
    if currency == "Dollar":  # Dollar
        currency = "\U00000024"
    elif currency == "Euro":  # Euro
        currency = "\U000020ac"
    elif currency == "Pound Stirling":  # Pound Stirling
        currency = "\U000000A3"
    elif currency == "Rupee":  # Rupee
        currency = "\U000020B9"
    elif currency == "Rial":  # Rial
        currency = "\U0000FDFC"
    elif currency == "Sheqel":  # Sheqel
        currency = "\U000020AA"
    elif currency == "Yen":  # Yen
        currency = "\U000000A5"
    elif currency == "Won":  # Won
        currency = "\U000020A9"
    elif currency == "Kip":  # Kip
        currency = "\U000020AD"
    elif currency == "Tugrik":  # Tugrik
        currency = "\U000020AE"
    elif currency == "Naira":  # Naira
        currency = "\U000020A6"
    elif currency == "Peso":  # Peso
        currency = "\U000020B1"
    else:  # Error, uses $ instead.
        print(f'''
    Unknown currency symbol: {currency}
    This is likely due to decoding issues.
    Alert me to your currency and I will fix it.
    Program will use $ now instead.''')
        currency = "\U00000024"

    return currency


# ---------- SAVES --------
def saves():
    """
    Figures out the save information.
    :return: save file names
    """

    save_one_name = conf.get('saveOne', 'Name')
    save_two_name = conf.get('saveTwo', 'Name')
    save_three_name = conf.get('saveThree', 'Name')

    return save_one_name, save_two_name, save_three_name


# ---------- PAYOUTS ----------
def payout_values():
    CHERRY_Value = int(conf.get('Reel_Payouts', 'CHERRY'))
    LEMON_Value = int(conf.get('Reel_Payouts', 'LEMON'))
    ORANGE_Value = int(conf.get('Reel_Payouts', 'ORANGE'))
    PLUM_Value = int(conf.get('Reel_Payouts', 'PLUM'))
    BELL_Value = int(conf.get('Reel_Payouts', 'BELL'))
    BAR_Value = int(conf.get('Reel_Payouts', 'BAR'))
    SEVEN_Value = conf.get('Reel_Payouts', 'SEVEN')

    payouts = [
        CHERRY_Value,
        LEMON_Value,
        ORANGE_Value,
        PLUM_Value,
        BELL_Value,
        BAR_Value,
        SEVEN_Value
    ]

    return payouts

