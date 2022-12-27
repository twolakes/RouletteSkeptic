import random

def spin():

    reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    spin = random.choice(list(range(1,39)))
    # spin = 38  <<<<<<<<<<< GET RID OF THIS
    # print(f"{spin}")

    if spin in [37, 38]:
        result = f"GRN {str(spin)}"

    else:
        color = "RED" if spin in reds else "BLK"
        result = f"{color} {str(spin)}"

    return result

