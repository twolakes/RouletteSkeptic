from player import player

payout = {
    "number": 35,
    "grp_2": 17,
    "grp_3": 11,
    "grp_4": 8,
    "grp_5": 6,
    "grp_6": 5,
    "grp_12": 2,
    "hi_low": 1,
    "even_odd": 1,
    "color": 1
}

def add_bets():
    curr_u = player["strategy"]["curr_u"]
    u_mult = player["strategy"]["unit_mult"]

    for b in player["strategy"]["bets"]:
        player["curr_bets"].append(
            (
                curr_u * u_mult * b["bet_mult"],
                b["bet_ty"],
                b["bet_on"]
            )
        )

    for b in player["curr_bets"]:
        print(f"\tbet ${b[0]} on {b[1]} - {b[2]}")
