import sys
import re

class InterpreterException(Exception):
    """ParserException"""


class Interpreter:
    """TODO"""

    debug = False
    
    @staticmethod
    def lprint(*args, **kwargs):
        """
        makes print for log
        """
        if Interpreter.debug:
            print("[LOG] ", end="")
            print(*args, **kwargs)

    @staticmethod
    def set_debug(val = True):
        Interpreter.debug = val
    
    @staticmethod
    def correct(clauses):
        """correct"""

        instances = set()
        relations = dict()

        for clause in clauses:
            if clause[0] in ("abstract", "interface", "class"):
                instances.add(clause)
            elif clause[0] in ("dependency", "multiplicity", "aggregation", "composition", "inheritance", "implements"):
                relations[clause[2]] = clause
            else:
                print("ERROR:", clause)
