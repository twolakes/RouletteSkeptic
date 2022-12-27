import random

def spin():

    reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    spin_data = {
        "hit": "",
        "even_odd": -1,
        "hi_low": -1,
        "grp_12": -1
    }

    result = random.choice(list(range(1,39)))
    print(result)

    if result in [37, 38]:
        spin_data |= [
            ("hit", f"GRN {'0' * (39 - result)}")
        ]
    else:

        color = "RED " if result in reds else "BLK "

        spin_data |= [
            ("hit", f"{color}{str(result)}"),
            ("even_odd", result % 2),
            ("hi_low", ((result - 1) // 18)),
            ("grp_12", ((result - 1) // 12) + 1)
        ]

    return spin_data

