#argparsa:


import argparse

parser = argparse.ArgumentParser(description="meow like cat")
parser.add_argument("-n", default=1, help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
