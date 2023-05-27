/*
 	CODIGO: SERIE EXPONENCIAL DE TAYLOR e^(X)
    JESUS CHAVEZ ARIAS
*/

main:-
    write('Ingresa N:'), read(N), write('Ingresa X:'), read(X),
    write('e^(X) = 1 + X'),
    taylor(2, N), write('=').

taylor(Act, N):-
    Act>N, !.
taylor(Act, N):-
    write(' + '), write('X'), write('^('), write(Act), write(')'),
    write('/'), fact(Act, F), write(F),
    Act1 is Act + 1, 
    taylor(Act1, N).



fact(0,1):- !.
fact(N,F):- 
    N1 is N-1,
    fact(N1, F1),
    F is N*F1.
    