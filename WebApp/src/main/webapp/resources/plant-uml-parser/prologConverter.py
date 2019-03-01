import sys
import re
from settings import *

class PrologConverterException(Exception):
    """PrologConverterException"""

class PrologConverter:
    """TODO"""

    @staticmethod
    def write_clause(clause, outfile):
        """write clause"""
        if isinstance(clause, list):
            for subclause in clause:
                PrologConverter.write_clause(subclause, outfile)
        else:
            name = clause[0]
            attributes = clause[1:]
            outfile.write("%s(%s).\n" % (name, ", ".join([str(i).lower() for i in attributes])))
        
    @staticmethod
    def convert(clauses, outfile):
        """convert"""
        assert hasattr(outfile, "write"), "cannot write output file, probably not a file"

        for clause in clauses:
            for subclause in clause:
                PrologConverter.write_clause(subclause, outfile)

        Utilities().lprint("finished writing clauses.")
