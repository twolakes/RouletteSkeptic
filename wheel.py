import random

def spin_res():

    reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    spin_data = {
        "number": "",
        "color": "",
        "even_odd": -1,
        "hi_low": "",
        "group_12": 0
    }

    result = random.choice(list(range(1,39)))
    print(result)

    if result in [37, 38]:
        spin_data |= [
            ("number", "0" * (39 - result)),
            ("color", "green"),
            ("even_odd", -1),
            ("hi_low", "na"),
            ("group_12", 0)
        ]
    else:

        spin_data |= [
            ("number", str(result)),
            ("color", "red" if result in reds else "black"),
            ("even_odd", result % 2),
            ("hi_low", "low" if result <= 18 else "hi"),
            ("group_12", ((result - 1) // 12) + 1)
        ]

    return spin_data

