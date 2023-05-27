main:-
    write('Ingresa el ancho que quieres: '), read(N),formatoN(25, N, 0).

formatoN(X,N,I):-
    I == N, write(X), !.
formatoN(X,N,I):-
    write(' '), I1 is I+1,
    formatoN(X,N,I1).