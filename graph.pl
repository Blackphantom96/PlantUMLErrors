% 
%   b   c
% a       f
%   d   e
% 
edge(a,b).
edge(b,c).
edge(c,f).
% edge(c,d).
edge(a,d).
edge(d,e).
edge(e,f).

% path(X,Y) :- edge(X,Y).
% path(X,Y) :- edge(X,Z),path(Z,Y).

path(X,Y) :- edge(X,Y).
path(X,Y) :- edge(X,Z),path(Z,Y).

