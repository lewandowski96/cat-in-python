import sys

arguments = sys.argv

if len(arguments) == 1:
    print("provide input file. ex: python3.7 main.py {filename or filepath}")
    quit()

file = open(arguments[1], 'r')
lines = file.readlines()

count = 0

for line in lines:
    count += 1
    print(f"{line.strip()}")