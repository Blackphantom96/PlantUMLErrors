from pyswip import Prolog
prolog = Prolog()
prolog.consult("project.pl")
#print(list(prolog.query('class(X)')))
print(list(prolog.query('multiplicityError(X)')))
print(list(prolog.query('warningAlone(X)')))
