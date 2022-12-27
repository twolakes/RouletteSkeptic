import time

import feedback
from play import add_bets, settle_bets
from wheel import spin
from player import player




def main():
    print("\n")
    play = True

    while play:
        add_bets()
        # print("\nhere we go, no more bets ...")
        result = spin()
        player["session"]["spins"] = player["session"]["spins"] + 1
        # print(f"{result}\n")
        settle_bets(result)
        # print(player["session"]["spins"])
        if player["session"]["sess_net"] >= player["strategy"]["take_win"]:
            play = False
        elif player["session"]["sess_net"] <= player["strategy"]["stop_loss"]:
            play = False
        elif player["session"]["spins"] > 1000:
            play = False

    feedback.rpt_sess_summ()
 

if __name__ == "__main__":
    main()
