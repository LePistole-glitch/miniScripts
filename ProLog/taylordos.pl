%N = VALOR DE LAS ITERTACIONES
%X = VALOR DE LA FUNCION DE X
%S = SUMA
%I = CONTADOR
% taylor.pl
% Calcular la Serie de Taylor de e^X
main:-
    write('Ingresa el valor de X: '), read(X), write('Ingresa el valor de n'), read(N),
    taylor(X,N,0,0).

taylor(_,N,S,I):-
    I==N, write(S), !.
taylor(X,N,S,I):-
    Pow is X**I, factorial(I,Y), S1 is Pow/Y,
    S2 is S+S1, I1 is I+1,
    taylor(X, N, S2, I1).

factorial(0, 1).
factorial(X, Y) :-
    X>0,
    A is X-1,
    factorial(A, B),
    Y is X*B,
    !.