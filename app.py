import time

import feedback
from play import add_bets, settle_bets
from wheel import spin
from player import player, sess_reset


def run_session():

    play = True

    while play:
        add_bets()
        print("\nhere we go, no more bets ...")
        result = spin()
        player["session"]["spins"] = player["session"]["spins"] + 1
        print(f"{result}\n")
        settle_bets(result)
        print(player["session"]["spins"])
        if player["session"]["sess_net"] >= player["strategy"]["take_win"]:
            play = False
            player["d_run"]["win_sess"] += 1
            if player["session"]["sess_net"] > player["d_run"]["max_win"]:
                player["d_run"]["max_win"] = player["session"]["sess_net"]
        elif player["session"]["sess_net"] <= player["strategy"]["stop_loss"]:
            play = False
            player["d_run"]["lose_sess"] += 1
            if player["session"]["sess_net"] < player["d_run"]["max_loss"]:
                player["d_run"]["max_loss"] = player["session"]["sess_net"]

        elif player["session"]["spins"] > 1000:
            play = False




def main():
    print("\n")

    for i in range(20):
        player["d_run"]["sessions"] += 1
        run_session()
        feedback.rpt_sess_summ()
        print("\n")
        sess_reset()
        feedback.rpt_run_summ()
        print("next sess\n\n")

 

if __name__ == "__main__":
    main()
