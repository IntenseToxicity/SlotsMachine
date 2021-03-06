import configuration
import main


def saves():
    """
    Save file work.
    This checks each of the save files sections in the config and sends it to the main game.
    :return:
    """

    conf = configuration.conf

    save_file = configuration.saves()

    if ['One', 'Two', 'Three'] in save_file:
        print(f"[Debug]")

    save_names = configuration.saves()

    for each in save_names:
        # Debug check
        z = 0
        k = save_names[z]
        if conf.get('Debug', 'Type') == '1':
            if each in ['One', 'Two', 'Three']:
                print(f"[Debug] Save game: {each} is it's default name.")
        z += 1
    print()


saves()


def save_information(current_jackpot, current_stake, player_name, save_slot):
    if save_slot == 0:
        save_name = 'saveOne'
    elif save_slot == 1:
        save_name = 'saveTwo'
    else:
        save_name = 'saveThree'

    configuration.conf[save_name] = {
        '; Do not edit this section please.': None,
        '; I have yet to learn how to encrypt this to prevent cheating.': None,
        'name': player_name.lower(),
        'wallet': str(current_stake)
    }

    configuration.conf['MACHINE'] = {
        '; Do not edit this section please.': None,
        '; I have yet to learn how to encrypt this to prevent cheating.': None,
        'JACKPOT': str(current_jackpot)
    }

    with open('.Slots/Slot_settings.ini', 'w') as configfile:  # Write the player's wallet to file.
        configuration.conf.write(configfile)

    print("Game Saved!")
