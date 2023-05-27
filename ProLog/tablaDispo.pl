main:-
    N is 100000, write('Z'), write('\t'),
    colu(0, 0.09) , nl,
   	tabla(0, 0, 0.01, 4, N, 0).

fx(X, Y):- Y is exp(-X*X/2) /sqrt(2*pi).

sigma(_, _, N, N, 0) :- !.
sigma(A, Base, I, N, Area):- 
    I1 is I +1,
    sigma(A, Base, I1, N, Area1),
    X1 is A + I*Base, X2 is  X1 + Base,
    fx(X1, Y1), fx(X2, Y2), Y is (Y1 + Y2)/2,
    Area is Base*Y + Area1.

colu(F, F):-
    write(F),!.
colu(I, F):-
    I < F, !,
    write('	'), format('~2f', I), write('\t\t\t\t'),
    I1 is I+0.01,
    colu(I1,F).

tabla(_, B, _, B, _, _):- 
    !.
tabla(A, B, I, T, N, CONT):-
    B \= T, !,
    Base is (B-A)/N,
    sigma(A, Base, 0, N, Area),
    fl(CONT, B),
    format('~4f', Area), write('\t'),
    B1 is B+I, CONT1 is CONT+I,
    (CONT1 =< 0.09) -> tabla(A,B1,I,T,N,CONT1);
    B2 is B+0.01, rdn(B2, Y, 2),nl, tabla(A,Y,I,T,N,0).

fl(CONT, B):-
    (CONT = 0) -> format('~1f',B),
    write('|'), write('\t'); 
    write('   ').

rdn(X,Y,D) :- Z is X * 10^D, rdn(Z, ZA), Y is ZA / 10^D.