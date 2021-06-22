from os import popen, system
from random import choice

CURRENT_PATH = popen("pwd").read().strip()
EDABIT = f"{CURRENT_PATH}/finished/edabit/very_easy"
SCRIPT = choice(popen(f"ls {EDABIT}").read().split())

if __name__ == "__main__":
    print(f"The Script to run is {SCRIPT}.")
    system(f"python3 {EDABIT}/{SCRIPT}")
