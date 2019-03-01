import sys
import re

class PrologConverterException(Exception):
    """PrologConverterException"""


class PrologConverter:
    """TODO"""

    debug = False
    
    @staticmethod
    def lprint(*args, **kwargs):
        """
        makes print for log
        """
        if PrologConverter.debug:
            print("[LOG] ", end="")
            print(*args, **kwargs)

    @staticmethod
    def set_debug(val = True):
        """set debug flag"""
        PrologConverter.debug = val

    @staticmethod
    def write_clause(clause, outfile):
        """write clause"""
        if isinstance(clause, list):
            for subclause in clause:
                PrologConverter.write_clause(subclause, outfile)
        else:
            name = clause[0]
            attributes = clause[1:]
            outfile.write("%s(%s).\n" % (name, ", ".join([str(i) for i in attributes])))
        
    @staticmethod
    def convert(clauses, outfile):
        """convert"""
        assert hasattr(outfile, "write"), "cannot write output file, probably not a file"

        for clause in clauses:
            for subclause in clause:
                PrologConverter.write_clause(subclause, outfile)

        PrologConverter.lprint("finished writing clauses.")
