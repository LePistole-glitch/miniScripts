main:-
    write("Ingresa el año: "), read(Y),
    .

esBisiesto(A):-
    R is A mod 400, R = 0, 
    !.
esBisiesto(A):-
    R1 is A mod 4,
    R2 is A mod 100,
    R3 is A mod 400,
    R1 = 0, R2 \= 0.

diasMes(M, X):-
    numDias(M, [31,28,31,30,31,30,31,31,30,31,30,31], X).

numDias(1,[X | _], X):- !.
numDias(M, [_ | Resto], X):- 
    M1 is M - 1,
    numDias(M1, Resto, X).