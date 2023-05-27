main:-











generaRandom(0,_,[]):-
    !.
generaRandom(N,Limite,[X | Resto]):-
    X is random(Limite),
    N1 is N - 1,
    generaRandom(N1,Limite,Resto).

imprimeLista([]):-
    !,nl.
imprimeLista([X | Resto]):-
    write(X), write(' '),
    imprimeLista(Resto).

insercion([],[]):- !.
insercion([X | Resto], Y):-
    insercion(Resto,Lista),
    inserta(X,Lista,Y).
inserta(X,[],[X]):- !.
inserta(X,[Y | Resto], [X,Y | Resto]):-
    X =< Y, !.
inserta(X,[Y | Resto], [Y | Lista]):-
    inserta(X,Resto,Lista).

mainOrdenar:-
    write('Cuantos numeros: '),
    read(N), 
    write('Ingresa el limite: '),
    read(L),
    generaRandom(N,Limite,X),
    write('Arreglo Original: '), nl,
    imprimeLista(X),
    insercion(X,Y),
    write('Arreglo Orden: '), nl,
    imprimeLista(Y),
    write('Arreglo Quick: '), nl,
    quick(X, Y).

quick([],[]):- !.
quick([X| Resto], Y):-
    particion(X,Resto,Menores,Mayores),
    quick(Menores,Lista1),
    quick(Mayores,Lista2),
    append(Lista, [X | Lista2], Y).

particion(_,[],[],[]):- !.
particion(X,[Y | Resto],[Y | Otros], Lista):-
    Y =< X, particion(X, Resto, Otros, Lista).
particion(X, [Y| Resto],Lista,[Y | Otros]):-
    particion(X, Resto, Lista, Otros).