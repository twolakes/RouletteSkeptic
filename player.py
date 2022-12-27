player = {
    "name": "",
    "init_bank": 1000,
    "curr_bank": 1000,

    "session": {
        "sess_net": 0,
        "sess_max": 0,
        "rounds_pos": 0,
        "sess_min": 0,
        "rounds_neg": 0,
        "spins": 0,
        "wins": 0,
        "losses": 0
    },
    "strategy": {
        "base_u": 1,
        "max_u": 999999,
        "curr_u": 1,
        "unit_mult": 10,
        "bets": [
            {
                "bet_mult": 1,
                "bet_ty": "grp_12",
                "bet_on": 2
            },
            {
                "bet_mult": 1,
                "bet_ty": "grp_12",
                "bet_on": 3
            }
        ],
        "res_mod": {
            "win_op": "mult",
            "win_adj": 0.5,
            "lose_op": "mult",
            "lose_adj": 2
        },
        "take_win": 100,
        "stop_loss": -256
    },
    "curr_bets": []

}