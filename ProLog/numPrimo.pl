main:- 
    write("Ingresa limite inferior: "), read(L1),
    write("Ingresa limite superior: "), read(L2), 
    .

forPrimo(L1, L2, X):-
    W is 2, i is L1

calc(i, X,_):-
    i == 0, X is 0.
calc(i, X,_):-
    i == 4, X is 0.
calc(i, X,_):-
    i == 1, X is 0.
calc(i, X, W):-
    i1 is i / 2, W < floor(sqrt(i1)), modulo(i, W, K)

modulo(i, W, K):-
    K is i mod W