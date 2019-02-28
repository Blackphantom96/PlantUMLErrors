import sys
import re

class ParserException(Exception):
    """ParserException"""


class Element(object):
    def __init__(self, name):
        self.name = name


class Parser:
    """TODO"""

    debug = False
    regexps = [
        (r'abstract\s+(\w+)\s+([<]{2}(\w+)[>]{2})?', lambda x: ("abstract", x.group(1), x.group(3))),
        (r'interface\s+(\w+)\s+([<]{2}(\w+)[>]{2})?', lambda x: ("interface", x.group(1), x.group(3))),
        (r'(\w+)\s+<\|--\s+(\w+)', lambda x: ("inheritance", x.group(1), x.group(2))),
        (r'(\w+)\s+--\|>\s+(\w+)', lambda x: ("inheritance", x.group(2), x.group(1))),
        (r'(\w+)(\s+\"(\w+)\")?\s+--\s+(\"(\w+)\")?\s*(\w+)', lambda x: [("dependency", x.group(1), x.group(6))] +
         ([("multiplicity", x.group(1), x.group(6), x.group(5))] if x.group(5) else []) +
         ([("multiplicity", x.group(6), x.group(1), x.group(3))] if x.group(3) else [])),
    ]

    @staticmethod
    def lprint(*args, **kwargs):
        """
        makes print for log
        """
        if Parser.debug:
            print("[LOG {}] ", end="")
            print(*args, **kwargs)

    @staticmethod
    def set_debug(val = True):
        debug = val
    
    @staticmethod
    def parse_line(line):
        """parse line"""
        Parser.lprint("ENTRA: \"", line, "\"")

        results = []
        
        for r in Parser.regexps:
            res = re.match(r[0], line)
            Parser.lprint(res)
            if res is not None:
                result = r[1](res)
                Parser.lprint("RES:", result)
                results.append(result)

        return results
    
    @staticmethod
    def parse(archive) -> tuple:
        """parse"""
        assert hasattr(archive, 'readlines'), "archive has no readline method, probably not a file"
        
        lines = [i.strip() for i in archive.readlines()]

        s = "\n".join(lines).strip()

        if not (s.startswith("@startuml") and s.endswith("@enduml")):
            raise ParserException("Invalid start or end of file")

        results = []
        for line in s.split("\n"):
            r = Parser.parse_line(line)
            if r:
                results.append(r)

        return results
