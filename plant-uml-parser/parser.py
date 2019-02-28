import sys
import re

class ParserException(Exception):
    """ParserException"""


class Element(object):
    def __init__(self, name):
        self.name = name


class Parser:
    """TODO"""
    
    regexps = [
        (r'abstract\s+(\w+)\s*([<]{2}(\w+)[>]{2})?', lambda x: ("abstract", x.group(1), x.group(3))),
        (r'interface\s+(\w+)\s*([<]{2}(\w+)[>]{2})?', lambda x: ("interface", x.group(1), x.group(3))),
        (r'(\w+)\s*<|--\s*(\w+)', lambda x: ("inheritance", x.group(1), x.group(2))),
    ]
    
    @staticmethod
    def parse_line(line):
        """parse line"""
        print("ENTRA: \"", line, "\"")
        for r in Parser.regexps:
            # print("ENTRA EN CICLO")
            res = re.match(r[0], line)
            print(res)
            if res is not None:
                print("RES:", r[1](res))

        # print("SALE")
        return ()
    
    @staticmethod
    def parse(archive) -> tuple:
        """parse"""
        assert hasattr(archive, 'readlines'), "archive has no readline method, probably not a file"
        
        lines = [i.strip() for i in archive.readlines()]

        s = "\n".join(lines).strip()

        if not (s.startswith("@startuml") and s.endswith("@enduml")):
            raise ParserException("Invalid start or end of file")

        for line in s.split("\n"):
            Parser.parse_line(line)

        return () # TODO
