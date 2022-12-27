player = {
    "name": "",
    "session": {
        "init_bank": 1000,
        "curr_bank": 1000,
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
            "win_adj": 2,
            "lose_op": "abs",
            "lose_adj": 1
        }
    },
    "curr_bets": [

    ]


}