%IMPRIMIR UNA TABLA DE CONVERSION DE TEMPERATURA:
%°C ----> °F Los valores de C van de 0 a 40 de 2 en 2
%JESUS CHAVEZ ARIAS

main:-
    write('\e[2J'), write('TABLA DE CONVERSIONES DE GRADOS Celsius A Fahrenheit'), nl, 
    convert(0).

convert(C):-
    C == 42, !.

convert(C):-
    F is C * (9/5) + 32, write('C:'), write(C), write(' ----> '), write('F:'), format('~1f', F), nl, 
    C1 is C + 2,
    convert(C1).