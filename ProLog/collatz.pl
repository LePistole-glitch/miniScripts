% PROGRAMA: CALCULAR LA CANTIDAD DE ITERACIONES DE LA CONJETURA DE COLLATZ
% JESUS CHAVEZ ARIAS


main:-
    write('Ingresa un valor de N: '), read(N), K is N mod 2,
    collatz(N,K,1).
collatz(N,_,I):-
    N == 1, write('Total de iteraciones de la Conjetura de Collatz: '), write(I),!.
collatz(N,K,I):-
    K == 0, N1 is N / 2, I1 is I + 1, K1 is N1 mod 2,
    collatz(N1,K1,I1).
collatz(N,K,I):-
    K \== 0, N1 is (N * 3) + 1, I1 is I + 1, K1 is N1 mod 2,
    collatz(N1,K1,I1).