from player import player


def rpt_sess_summ():

    sess = player["session"]

    print(f"\tsession net: \t{sess['sess_net']}")
    print(f"\tplayer bank: \t{player['curr_bank']}")
    print(f"\tspins, w / l:\t{sess['spins']}\t{sess['wins']} / {sess['losses']}")
    print(f"\tsession net: \t{sess['sess_net']}")
    print(f"\tsession max: \t{sess['sess_max']}")
    print(f"\tsession min: \t{sess['sess_min']}\n\n")

def rpt_run_summ():
    print(f"Run Summary: {player['d_run']['sessions']} sessions")
    print(f"W / L:\t{player['d_run']['win_sess']} / {player['d_run']['lose_sess']}")
    print(f"max win:\t{player['d_run']['max_win']}")
    print(f"max loss:\t{player['d_run']['max_loss']}\n")
    print(f"starting bank:\t{player['init_bank']}")
    print(f"current bank:\t{player['curr_bank']}\n")
