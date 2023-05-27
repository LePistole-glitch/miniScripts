/*
%Y = 1; DENOMINADOR
%X = 1; AÑADIR
%i = 0; Ayuda
%N	  ;Cantidad de terminos
	Programa: pi.pl
    Calcula el valor de Pi usando una serie de Leibniz
*/
main:-
    Y = 1, X = 1, I = 0, write('Ingresa la cantidad de terminos: '), read(N), 
    calc(Y, X, N, I).

calc(_, X, N, I):-
    I>N-1, X2 is X * 4,
    write(X2), !.
calc(Y, X, N, I):-
    Y1 is Y + 2, X1 is X - (1/Y1), 
    Y2 is Y1 + 2, X2 is X1 + (1/Y2),
    I2 is I + 1,
    calc(Y2, X2, N, I2).
