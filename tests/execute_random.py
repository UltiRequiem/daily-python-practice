from os import popen, system
from random import choice

CURRENT_PATH = popen("pwd").read().strip()
DIRECTORY = f"{CURRENT_PATH}/geeks_for_geeks/lists/"
SCRIPT = choice(popen(f"ls {DIRECTORY}*.py").read().split())

if __name__ == "__main__":
    print(f"The Script to run is {SCRIPT}.")
    system(f"python3 {SCRIPT}")
