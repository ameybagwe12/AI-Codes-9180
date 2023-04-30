% Predicate to solve N-Queens problem
n_queens(N, Solution) :-
    length(Solution, N),     % The solution list must have N elements
    place_queens(N, Solution),    % Place the queens on the board
    is_valid(Solution).      % Check if the solution is valid

% Helper predicate to place the queens on the board
place_queens(0, _).
place_queens(I, Solution) :-
    I > 0,
    place_queens(I-1, Solution),
    member(X, [1,2,3,4,5,6,7,8]),
    no_attack(X/I, Solution),
    Solution = [X | Rest].

% Helper predicate to check if the solution is valid
is_valid([]).
is_valid([X | Rest]) :-
    no_attack(X/1, Rest),
    is_valid(Rest).

% Helper predicate to check if a queen can be placed in a given position
no_attack(_, []).
no_attack(X/Y, [X1/Y1 | Rest]) :-
    Y =\= Y1,
    abs(X1 - X) =\= abs(Y1 - Y),
    no_attack(X/Y, Rest).
