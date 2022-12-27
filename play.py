payout = {
    "number": 35,
    "group_12": 2,
    "hi_low": 1,
    "even_odd": 1,
    "color": 1
}

strategy = {
    "base_unit": 10,
    "base_bets": [
        (("group_12", 2), 1),
        (("group_12", 3), 1)
    ],
    "after_win": -1,
    "after_loss": 2,
    "max_u_ct": 10,
    "start_bank": 2000,
    "take_wins": 200,
    "stop_loss": -99999
}