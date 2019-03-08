import sys
import re
from settings import *

name_count = 0

def get_next_count():
    global name_count
    name_count += 1
    return name_count-1

class ParserException(Exception):
    """ParserException"""

class Parser:
    """TODO"""

    regexps = [
        # types
        (r'class\s+(\w+)', lambda x: ("class", x.group(1))),
        
        (r'abstract\s+(\w+)\s+([<]{2}(\w+)[>]{2})?', lambda x: ("abstract", x.group(1))),

        (r'interface\s+(\w+)\s+([<]{2}(\w+)[>]{2})?', lambda x: ("interface", x.group(1))),

        (r'(\w+)\s+--\|>\s+(\w+)', lambda x: ("inheritance", x.group(1), x.group(2))),
        (r'(\w+)\s+<\|--\s+(\w+)', lambda x: ("inheritance", x.group(2), x.group(1))),

        # relations
        
        (r'(\w+)(\s+\"(.+)\")?\s+--(\s+\"(.+)\")?\s+(\w+)(\s+:\s+(\w+))?',
         lambda x: ("association",
                    x.group(8) if x.group(8) else str(get_next_count()), # assign id
                    x.group(1),
                    x.group(6),
                    x.group(3),
                    x.group(5))),

        (r'(\w+)(\s+\"(.+)\")?\s+\*--(\s+\"(.+)\")?\s+(\w+)(\s+:\s+(\w+))?',
         lambda x: [
             ("association",
              str(get_next_count()),
              x.group(2),
              x.group(1)),
             ("composition", str(get_next_count()-1))]),
        (r'(\w+)(\s+\"(.+)\")?\s+--\*(\s+\"(.+)\")?\s+(\w+)(\s+:\s+(\w+))?',
         lambda x: [
             ("association",
              str(get_next_count()),
              x.group(1),
              x.group(2)),
             ("composition", str(get_next_count()-1))]),

        (r'(\w+)(\s+\"(.+)\")?\s+o--(\s+\"(.+)\")?\s+(\w+)(\s+:\s+(\w+))?', 
         lambda x: [
             ("association",
              str(get_next_count()),
              x.group(1), 
              x.group(2)),
             ("aggregation", str(get_next_count()-1))]),
        (r'(\w+)(\s+\"(.+)\")?\s+--o(\s+\"(.+)\")?\s+(\w+)(\s+:\s+(\w+))?', 
         lambda x: [
             ("association",
              str(get_next_count()),
              x.group(2), 
              x.group(1)),
             ("aggregation", str(get_next_count()-1))]),

        #methods # TODO
        # (r'(\w+)\s+:\s+(\w+)\((\.*)\)', lambda x: ("method", x.group(1), x.group(2), ),
    ]

    @staticmethod
    def parse_line(line):
        """parse line"""
        Utilities().lprint("ENTRA: \"{}\"".format(line))

        results = []
        
        for r in Parser.regexps:
            res = re.match(r[0], line)
            Utilities().lprint(res)
            if res is not None:
                result = r[1](res)
                Utilities().lprint("RES:", result)
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
