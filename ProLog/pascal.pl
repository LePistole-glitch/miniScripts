main:-
    get_time(X), floor(X,Y), aMinutos(Y, YM), aHoras(YM, YH), aDias(YH, YD),
    write(YD).

aMinutos(Y, YM):-
    YM is Y div 60.

aHoras(YM, YH):-
    YH is YM div 60.

aDias(YH, YD):-
    YD is YH div 24.