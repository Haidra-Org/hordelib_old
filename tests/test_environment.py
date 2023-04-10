# test_environment.py
import os


def test_environment():
    with open("images/environment.txt", "wt") as outfile:
        for k, v in os.environ.items():
            outfile.write(f"{k} = {v}\n")
