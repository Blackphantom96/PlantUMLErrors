:- include('assert.pl').

implements(A,B):- class(A,_),interface(B,_),inheritance(A,B).

warningMultiplicity(X):- class(X,_),association(_,X,X,"1..*",_);association(_,X,X,_,"1..*").

transitiveInheritance(A,B):- inheritance(A,B).
transitiveInheritance(A,B) :- inheritance(A,C), inheritance(C,B).
cyclicInheritanceError(A,B):- transitiveInheritance(A,B),transitiveInheritance(B,A).

warningAlone(A) :- not(association(_,A,_,_,_);association(_,_,A,_,_)).

errorNotAllImplement(X) :- class(X,_), inheritance(X,Y) ,(not(operation(N,RT,P,X,V)),operation(N,RT,P,Y,V)).

errorNotImplements(X) :- class(X,_), not(inheritance(X,Y)) ,(not(operation(N,RT,P,X,V)),operation(N,RT,P,Y,V)).

warningDiamondProblem(X) :- inheritance(B,A),inheritance(C,A),inheritance(X,B),inheritance(X,C).

