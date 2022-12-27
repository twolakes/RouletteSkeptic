from player import player


def rpt_sess_summ():

    sess = player["session"]

    print(f"\tsession net: \t{sess['sess_net']}")
    print(f"\tplayer bank: \t{player['curr_bank']}")
    print(f"\tspins, w / l:\t{sess['spins']}\t{sess['wins']} / {sess['losses']}")
    print(f"\tsession net: \t{sess['sess_net']}")
    print(f"\tsession max: \t{sess['sess_max']}")
    print(f"\tsession min: \t{sess['sess_min']}\n\n")