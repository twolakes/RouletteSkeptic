import time

from wheel import spin_res


def main():
    while True:
        result = spin_res()
        print(result)
        time.sleep(3)



if __name__ == "__main__":
    main()
