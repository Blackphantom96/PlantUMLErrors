interface(X,V). %X is an interface
class(X,V). %X in a class
operation(N,RT,P,C,V). % The operation N(name) return RT(return type) receive params(P is a []) in C (Interface or class)
attribute(N,T,C,V). % The attribute N(name) of type T in class C
inheritance(A,B). % A --|> B
association(N,A,B,AB,BA). % A "AB"---N--- "BA" B
aggregation(N). % A "AB"<>---N--- "BA"
composition(N). % A "AB"<*>---N--- "BA"
abstract(A). % Abstract Class