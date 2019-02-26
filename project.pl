inheritance(a,b).

error(X,Y) :- inheritance(X,Y),inheritance(Y,X).
error(X,Y) :- 