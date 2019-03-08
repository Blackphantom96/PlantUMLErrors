import os
import sys
import argparse
from sys import stdin
from sys import stdout

from settings import *
from pyswip import Prolog

def command_line_parser():
    """
    returns a dict with the options passed to the command line
    according with the options available
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--assertz", type=str,
                        help="assertions file")

    parser.add_argument("-q", "--queries", type=str, default="-",
                        help="queries file, - to read from stdin")

    parser.add_argument("-o", "--output", type=str, default="-",
                        help="output file, - for stdout")

    parser.add_argument("-v", "--verbose", action="store_true")
    # parser.add_argument("subjects", type=str,
    #                     help="subjects to check comma separated")

    args = parser.parse_args()

    options = dict()
    options['assertz'] = args.assertz
    options['queries'] = args.queries
    options['output']  = args.output
    options['verbose'] = args.verbose

    return options


def getsubitems(item, sym_idx = 0) -> str:
    symbols = ("([{|", ")]}|")
    sym_len = len(symbols[0])
    r = []
    if isinstance(item, list):
        for subitem in item:
            r.append(getsubitems(subitem, (sym_idx +1) % sym_len))
    else:
        return str(item)

    return "%s %s %s" % (symbols[0][sym_idx],
                         ", ".join(r),
                         symbols[1][sym_idx])
    
def assertz(assertz):
    prolog = Prolog()
    for line in assertz:
        Utilities().lprint("ASSERT: '%s' -> '%s'" % (line, line.strip(" .")))
        if line.strip() == "":
            Utilities().lprint("... ignoring")
            continue
        prolog.assertz(line.strip(" ."))
    

def start_prolog(assertzfile, queriesfile, outfile):
    assert hasattr(assertzfile, "readlines"), "cannot read assertz file, probably not a file"
    assert hasattr(queriesfile, "readlines"), "cannot read queries file, probably not a file"
    assert hasattr(outfile, "write"), "cannot write output file, probably not a file"

    Utilities().lprint("<< Inserting assertions ... >>")
    assertz([i.strip() for i in assertzfile.readlines()])

    Utilities().lprint("<< Executing queries ... >>")
    answers = query([i.strip() for i in queriesfile.readlines()])

    Utilities().lprint("<< Writing output ... >>")
    for ans in answers:
        outfile.write(getsubitems(ans) + "\n")


def single_query(query):
    Utilities().lprint("query: '%s'" % (query))
    if query.strip() == "":
        return None
    
    prolog = Prolog()
    return list(prolog.query(query)) #catcherrors?

    
def query(query):
    assert isinstance(query, (str, list)), "query is not a str or a list"

    prolog = Prolog() # is a singleton
    answer = []
    if isinstance(query, list):
        for q in query:
            res = single_query(q)
            if res:
                Utilities().lprint("query result: '%s'" % (res))
                answer.append(res)

    return answer


def main():
    options = command_line_parser()

    settings = Settings()
    settings.setSetting("debug", options['verbose'])

    ASSERTZ = options['assertz']
    QUERIES = options['queries']
    OUTPUT  = options['output']
    
    assertzfile = open(ASSERTZ, "r")
    queriesfile = open(QUERIES, "r") if QUERIES not in ("-", "") else stdin
    outfile = open(OUTPUT, "w") if OUTPUT not in ("-", "") else stdout

    start_prolog(assertzfile, queriesfile, outfile)

if __name__ == "__main__":
    main()
