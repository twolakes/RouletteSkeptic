player = {
    "name": "",
    "init_bank": 1000,
    "curr_bank": 1000,

    "d_run": {
        "sessions": 0,
        "win_sess": 0,
        "lose_sess": 0,
        "max_win": 0,
        "max_loss": 0
    },

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
        "unit_mult": 2,
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
            "win_op": "add",
            "win_adj": -1,
            "lose_op": "add",
            "lose_adj": 2
        },
        "take_win": 50,
        "stop_loss": -400
    },
    "curr_bets": []

}

res_params = [
    ("sess_net", 0),
    ("sess_max", 0),
    ("rounds_pos", 0),
    ("sess_min", 0),
    ("rounds_neg", 0),
    ("spins", 0),
    ("wins", 0),
    ("losses", 0)
]

def sess_reset():
    for p in res_params:
        player["session"][p[0]] = p[1]
    player["strategy"]["curr_u"] = player["strategy"]["base_u"]