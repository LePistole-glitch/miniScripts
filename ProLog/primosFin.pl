%L = Lim inferior
%S = Lim Superior

main:-
    write('Lim Inferior: '), read(L),
    write('Lim Superior: '), read(S),
    loop(L,S).

loop(M,N):-
   between(M, N, X),
   calc(X, TF), 
   X >= N, !.
   loop(M,X).

loop2(M,N, XC):-
   between(M, N, K),  XC1 is XC mod K,
   ifuno(XC1), 
   K >= N, !.
   loop(M,K).

ifuno(XC1):-
    XC1 == 0, TF is 0 ,!.
ifuno(XC1, TF):-
    XC1 \= 0, 
    
calc(X, TF):-
	X == 1, TF is 0, !.

calc(X, TF):-
	X == 0,TF is 0, !.

calc(X, TF):-	
	X == 4,TF is 0, !.

calc(X, TF):-
    C is floor(X / 2), XC is X, loop2(2, C, XC) 
    