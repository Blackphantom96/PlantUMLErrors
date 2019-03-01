import os
import sys
import argparse
from sys import stdin
from sys import stdout

from parser import *
from prologConverter import *
from settings import *


def command_line_parser():
    """
    returns a dict with the options passed to the command line
    according with the options available
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("file", type=str,
                        help="input file, none or - to read from stdin")

    parser.add_argument("-o", "--output", type=str, default="-",
                        help="output file, none or - to write to stdout")


    parser.add_argument("-v", "--verbose", action="store_true")
    # parser.add_argument("subjects", type=str,
    #                     help="subjects to check comma separated")

    args = parser.parse_args()

    options = dict()
    options['file']    = args.file
    options['outfile'] = args.output
    options['verbose'] = args.verbose

    return options


def start(inputfile, outputfile):
    clauses = Parser.parse(inputfile)
    PrologConverter.convert(clauses, outputfile)

def main():
    options = command_line_parser()

    settings = Settings()
    settings.setSetting("debug", options['verbose'])

    FILENAME     = options['file']
    OUT_FILENAME = options['outfile']

    inputfile = open(FILENAME, "r") if FILENAME not in ("-", "") else stdin

    outfile = open(OUT_FILENAME, "w") if OUT_FILENAME not in ("-", "") else stdout

    start(inputfile, outfile)

if __name__ == "__main__":
    main()
