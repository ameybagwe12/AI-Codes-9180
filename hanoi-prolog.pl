% Move N disks from the From pole to the To pole using the Aux pole
% hanoi(+N, +From, +To, +Aux, -Moves)
hanoi(0, _, _, _, []).
hanoi(N, From, To, Aux, Moves) :-
    N1 is N - 1,
    hanoi(N1, From, Aux, To, Moves1),
    move(From, To, Moves2),
    hanoi(N1, Aux, To, From, Moves3),
    append(Moves1, Moves2, Temp),
    append(Temp, Moves3, Moves).

% Move a single disk from the From pole to the To pole
% move(+From, +To, -Moves)
move(From, To, [move(From, To)]).
