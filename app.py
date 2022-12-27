import time

from wheel import spin
from play import payout, strategy


p_base_u = strategy['base_unit']
session_net = 0
p_bank = strategy["start_bank"]

curr_u_ct = 1
curr_bets = []

session_max = -9999
session_min = 9999

def set_bets():
    for b in strategy['base_bets']:
        bet = b[1] * curr_u_ct * p_base_u
        curr_bets.append(
            (b[0], bet)
        )
        # print(f"bets ${bet} on {b[0][0]} - {b[0][1]}")
    # print("\nHere we go ...\n\n")

def settle_bets(rd, curr_res):
    
    global curr_bets
    global session_net
    global p_bank
    global session_max
    global session_min
    global curr_u_ct

    round_net = 0
    
    for b in curr_bets:
        
        if curr_res[b[0][0]] == b[0][1]:
            win_amt = payout[b[0][0]] * b[1]
            round_net = round_net + win_amt
            # print(f"wins ${win_amt} on {b[0][0]} - {b[0][1]}")
        else:
            round_net = round_net - b[1]
            # print(f"loses ${b[1]} on {b[0][0]} - {b[0][1]}")
            
    session_net = session_net + round_net
    p_bank = p_bank + round_net
    
    if round_net > 0:
        # print(f"{rd}\twon ${round_net} in that round")
        if session_net > session_max:
            session_max = session_net
        curr_u_ct = curr_u_ct + strategy["after_win"]
    elif round_net < 0:
        # print(f"{rd}\tlost ${-round_net} in that round")
        if session_net < session_min:
            session_min = session_net
        curr_u_ct = curr_u_ct + strategy["after_loss"]
    # else:
        # print(f"{rd}\tthat one was a wash")
    
    if curr_u_ct > strategy["max_u_ct"]:
        curr_u_ct = strategy["max_u_ct"]
        # print("** bet cap reached")
    elif curr_u_ct < 1:
        curr_u_ct = 1
        # print("** bet floor reached")

    print(f"session: ${session_net}\tbank: {p_bank}\n")

    curr_bets = []
    # print("\n\n--- Next Round ---")

def run_round():

    curr_rd = 0
    keep_playing = True

    while keep_playing:
        curr_rd = curr_rd + 1
        print(curr_rd)
        set_bets()
        result = spin_res()
        settle_bets(curr_rd, result)

        if session_net >= strategy["take_wins"]:
            keep_playing = False        

        if p_bank <= 0:
            keep_playing = False

    print(f"{curr_rd} rds\tsess: {session_net}\tmax up: {session_max}\tmax down: {session_min}")


def main():
    for t in (range(2)):
        run_round()



if __name__ == "__main__":
    main()
