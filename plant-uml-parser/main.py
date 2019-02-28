import os
import sys
import argparse
from sys import stdin

from parser import *


def command_line_parser():
    """
    returns a dict with the options passed to the command line
    according with the options available
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("file", type=str,
                        help="input file, none or - to read from stdin")


    parser.add_argument("-v", "--verbose", action="store_true")
    # parser.add_argument("subjects", type=str,
    #                     help="subjects to check comma separated")

    args = parser.parse_args()

    options = dict()
    options['file']    = args.file
    options['verbose'] = args.verbose

    return options


def main():
    options = command_line_parser()

    FILENAME = options['file']

    f = open(FILENAME) if FILENAME != "-" else stdin

    parsed_data = Parser.parse(f)

    print(parsed_data)

    # TODO

if __name__ == "__main__":
    main()
