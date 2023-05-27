main:-
    sortMerge([3,4,7,222,876,11,2,1],R),
    write(R).

split([],[],[]).
split([X | L], [X | L1], L2):- split(L, L2, L1).

merge(L,L,[]).
merge(L,[],L).
merge([X1 | L], [X1 | L1], [X2 | L2]):-
    X1 < X2, !, 
    merge(L, L1, [X2 | L2]).
merge([X2 | L], [X1 | L1], [X2 | L2]):-
    merge(L, [X1 | L1], L2).

sortMerge([],[]):- !.
sortMerge([X], [X]):- !.
sortMerge(L,S):- 
    split(L,L1,L2),
    sortMerge(L1,S1), sortMerge(L2,S2),
    merge(S,S1,S2).
