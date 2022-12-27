import feedback
from player import player

payout = {
    "ct_1": 35,
    "ct_2": 17,
    "ct_3": 11,
    "ct_4": 8,
    "ct_5": 6,
    "ct_6": 5,
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


def settle_bets(res):

    spin_net = -sum(list(b[0] for b in player["curr_bets"]))
    res_n = int(res[4:])

    for b in player["curr_bets"]:

        bet_won = False
        res_lbl = "loses"

        if b[1] == "color":
            bet_won = b[2].upper() == res[0:3]
        elif b[1] == "even_odd" and res_n <= 36:
            bet_won = b[2] == (res_n % 2)
        elif b[1] == "hi_low" and res_n <= 36:
            bet_won = b[2] == ((res_n - 1) // 18)
        elif b[1] ==  "grp_12" and res_n <= 36:
            bet_won = b[2] == (((res_n - 1) // 12) + 1)
        elif b[1][0:3] == "ct_":
            n_found = res_n in b[2]
            bet_won = True if n_found else False

        if bet_won:
            spin_net = spin_net + ((payout[b[1]] + 1) * b[0])
            res_lbl = "wins"

        print(f"\tbet ${b[0]} on {b[1]} - {b[2]}  {res_lbl}")


    player["curr_bets"] = []

    player["curr_bank"] = player["curr_bank"] + spin_net
    player["session"]["sess_net"] = player["session"]["sess_net"] + spin_net

    rm = player["strategy"]["res_mod"]

    if spin_net > 0:
        player["session"]["wins"] = player["session"]["wins"] + 1
        if player["session"]["sess_net"] > player["session"]["sess_max"]:
            player["session"]["sess_max"] = player["session"]["sess_net"]

        if rm["win_op"] == "mult":
            player["strategy"]["curr_u"] = player["strategy"]["curr_u"] * rm["win_adj"]


    elif spin_net < 0:
        player["session"]["losses"] = player["session"]["losses"] + 1
        if player["session"]["sess_net"] < player["session"]["sess_min"]:
            player["session"]["sess_min"] = player["session"]["sess_net"]

        if rm["lose_op"] == "mult":
            player["strategy"]["curr_u"] = player["strategy"]["curr_u"] * rm["lose_adj"]

    if player["strategy"]["curr_u"] < player["strategy"]["base_u"]:
        player["strategy"]["curr_u"] = player["strategy"]["base_u"]
    elif player["strategy"]["curr_u"] > player["strategy"]["max_u"]:
        player["strategy"]["curr_u"] = player["strategy"]["max_u"]


    if player["session"]["sess_net"] > 0:
        player["session"]["rounds_pos"] = player["session"]["rounds_pos"] + 1
    elif player["session"]["sess_net"] < 0:
        player["session"]["rounds_neg"] = player["session"]["rounds_neg"] + 1

    print(f"\nnet result for that spin:  ${spin_net}\n")

    feedback.rpt_sess_summ()