main:-
    write("Digitar Numero: "), read(N),
    genRand(0,N).


genRand(N,N):- !.
genRand(C,N):- 
    random_between(1, 3999, R),
    write(R), write(': '),
    conRomano(R,[1000,900,500,400,100,90,50,40,10,9,5,4,1],['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']), nl,
    C1 is C + 1,
    genRand(C1, N).


conRomano(0,_,_) :- !.
conRomano(N,[X | Res1],[Y | Res2]) :-
    N >= X,!,
    write(Y),
    N1 is N-X,
    conRomano(N1,[X | Res1],[Y | Res2]).
conRomano(N,[_ | Res1],[_ | Res2]) :-
    conRomano(N,Res1,Res2).