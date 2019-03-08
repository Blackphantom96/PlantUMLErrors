:- include('assert.pl').

primitiveTypes :- [short,int,string,float,double,bit,boolean,char,byte].
on(Item,[Item|_]).
on(Item,[_|Tail]) :- on(Item,Tail).

implements(A,B):- class(A,_),interface(B,_),inheritance(A,B).


transitiveInheritance(A,B):- inheritance(A,B).
transitiveInheritance(A,B) :- inheritance(A,C), inheritance(C,B).
cyclicInheritanceError(A,B):- transitiveInheritance(A,B),transitiveInheritance(B,A).

% warningMultiplicity(X):- class(X,_),association(_,X,X,"1..*",_);association(_,X,X,_,"1..*").
warning("warning Multiplicity"):- association(_,X,X,"1..*",_);association(_,X,X,_,"1..*").
% warningAlone(A) :- not(association(_,A,_,_,_);association(_,_,A,_,_)).
warning("warning Alone") :-not(association(_,A,_,_,_);association(_,_,A,_,_)).
% warningNotImplements(X) :- class(X,_), not(inheritance(X,Y)) ,not( (not(operation(N,RT,P,X,V)),operation(N,RT,P,Y,V)) ).
warning("warning Not Implements") :- class(X,_), not(inheritance(X,Y)) ,not( (not(operation(N,RT,P,X,V)),operation(N,RT,P,Y,V)) ).
% warningDiamondProblem(X) :- inheritance(B,A),inheritance(C,A),inheritance(X,B),inheritance(X,C).
warning("warning Diamond Problem") :- inheritance(B,A),inheritance(C,A),inheritance(X,B),inheritance(X,C).
% warningXX(X):- class(X,_), attribute(_,T,X,_), not(on(T,primitiveTypes)).
warning("warning attribute not in the model") :- class(X,_), attribute(_,T,X,_), not(on(T,primitiveTypes)).

warning("warning return type attribute not in the model") :- class(X,_), operation(_,T,_,X,_), not(on(T,primitiveTypes)).

% errorNotAllImplement(X) :- class(X,_),not(abstract(X)), inheritance(X,Y) ,( (not(operation(N,RT,P,X,V)), operation(N,RT,P,Y,V)) ).
error("error Not All Implement"):- class(X,_),not(abstract(X)), inheritance(X,Y) ,( (not(operation(N,RT,P,X,V)), operation(N,RT,P,Y,V)) ).
% errorInheritance(X):- class(X,_), transitiveInheritance(X,Y), transitiveInheritance(X,Z), transitiveInheritance(Y,Z).
error("Redundant inheritance") :- class(X,_), transitiveInheritance(X,Y), transitiveInheritance(X,Z), transitiveInheritance(Y,Z).

report(X):- error(X);warning(X).