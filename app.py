import time

from play import add_bets, settle_bets
from wheel import spin
from player import player




def main():
    print("\n")
    
    for i in range(10):
        add_bets()
        print("\nhere we go, no more bets ...")
        result = spin()
        player["session"]["spins"] = player["session"]["spins"] + 1
        print(f"{result}\n")
        settle_bets(result)

 

if __name__ == "__main__":
    main()
