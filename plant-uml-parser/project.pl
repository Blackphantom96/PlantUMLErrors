:- include('assert.pl').

% Rules:
implements(A,B):- class(A),interface(B),inheritance(A,B).


% Bucle
multiplicityError(X):- class(X),(multiplicity(X,X,"1");multiplicity(X,X,"1..*");multiplicity(X,X,"")).

transitiveInheritance(A,B):- class(A),class(B),inheritance(A,B).
transitiveInheritance(A,B) :- class(A),class(B), inheritance(A,C), inheritance(C,B).
inheritanceError(A,B):- class(A),class(B),transitiveInheritance(A,B),transitiveInheritance(B,A).

warningAlone(A) :- dependency(A,_); aggregation(A,_); composition(A,_); inheritance(A,_); implements(A,_); 
dependency(_,A); aggregation(_,A); composition(_,A); inheritance(_,A); implements(_,A). 