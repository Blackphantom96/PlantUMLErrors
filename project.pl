private(x). %Class, Method or Attribute
public(x). %Class, Method or Attribute
protected(x). %Class, Method or Attribute
class(c). %Define a class
interface(c). %Define a interface
abstract(c). %Define Abstract

method(m,c).
attribute(a,c).

dependency(a,b). %A use B
multiplicity(a,b,m). %A have [0,1,*,1..*] of B
aggregation(a,b). %Car <>-- Passengers
composition(a,b). %Car <o>-- Engine
inheritance(a,b). %User <|-- Admin // User <|-- Monitor
implements(a,b). %A implements B
% Rules:

% Bucle
multiplicityError(X):- class(X),multiplicity(X,X,"1");multiplicity(X,X,"1..*").



transitiveInheritance(A,B):- class(A),class(B),inheritance(A,B).
transitiveInheritance(A,B) :- class(A),class(B), inheritance(A,C), inheritance(C,B).
inheritanceError(A,B):- class(A),class(B),transitiveInheritance(A,B),transitiveInheritance(B,A).

