main:-
    write("Ingresa el anio: "), read(Y),
    esBisiesto(Y).

esBisiesto(A):-
    R1 is A mod 4,
    R2 is A mod 100,
    R3 is A mod 400,
    write(R1),nl,write(R2),nl,write(R3),nl,
    R1 = 0, R2 = 0, R3 =0.

