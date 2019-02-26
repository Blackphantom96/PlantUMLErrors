private(x). %Class, Method or Attribute
public(x). %Class, Method or Attribute
protected(x). %Class, Method or Attribute
class(c). %Define a class
interface(c). %Define a interface
abstract(c). %Define AbstractClass

method(m,c).
attribute(a,c).

dependency(a,b). %A use B
multiplicity(a,b,m). %A have [0,1,*,1..*] of B
aggregation(a,b). %Car <>-- Passengers
composition(a,b). %Car <o>-- Engine
inheritance(a,b). %User <|-- Admin // User <|-- Monitor
implements(a,b). %A implements B


error(X,Y) :- inheritance(X,Y),inheritance(Y,X).
