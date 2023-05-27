%Manejo de archivos
%verbo de infinitivo y sus conjugaciones


esc_arch:-
    open('animal.txt', append,Str),
    write('Da un animal (fin termina): '),
    read(Animal), not(Animal = fin), !,
    write(Str, Animal),
    write(Str, '.'),
    nl(Str), 
    close(Str),
    esc_arch.
esc_arch.

lec_arch:-
    open('animal.txt', read, Str),
    lec_animal(Str, Lista),
    close(Str),
    write('Animales Leidos: '), write(Lista), nl.

lec_animal(Str, [X|L]):-
    read(Str, X),  not(X = end_of_file), !,
    write(X), nl,
    lec_animal(Str, L).
lec_animal(_,[]).