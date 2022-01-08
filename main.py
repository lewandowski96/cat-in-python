import sys
import argparse

arguments = sys.argv

parser = argparse.ArgumentParser()
parser.add_argument("--version", action="version", version='%(prog)s 1.0', help="script version")
parser.add_argument("--info", help="accepted values : show | see this for usage")
parser.add_argument("-n", help="accepted values : true | this will number all output lines")
parser.add_argument("-file", help="specify your file's absolute path")
args = parser.parse_args()

if args.file is not None and args.n is None:

    file_open = open(args.file, 'r')
    lines = file_open.readlines()

    count = 0

    for line in lines:
        count += 1
        print(f"{line.strip()}")

elif args.file is not None and args.n is not None:

    if args.n == "true":

        file_open = open(args.file, 'r')
        lines = file_open.readlines()

        count = 0

        for line in lines:
            count += 1
            print(f"{count}    {line.strip()}")

    else:

        print("Accepted values for -n argument is 'true'. Leave it blank for default.")

elif args.info is not None:

    if args.info == "show":

        print("*******************************************************")
        print("This script emulates the linux 'cat' command in python")
        print('*******************************************************')
        print("\n")
        print("<= Usage =>")
        print("\n")
        print("```````````````````````````")
        print("To view the version : ")
        print("python3.7 main.py --version")
        print("`````````````````````````````````````````")
        print("To view the content of a specific file : ")
        print("python3.7 main.py -file {specify your file path here(absolute path)}")
        print("```````````````````````````````````````````````````````````````````")
        print("To view the content of a specific file with numbered output lines: ")
        print("python3.7 main.py -file {specify your file path here(absolute path)} -n true")
        print("````````````````````````````````````````````````````````````````````````````")
        print("\n")
        print("*******************************************************")

    else:

        print("Accepted values for --info argument is 'show'")