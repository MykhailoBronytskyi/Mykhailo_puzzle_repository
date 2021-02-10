''' Module for checking puzzle board for readiness for a game
https://github.com/MykhailoBronytskyi/Mykhailo_puzzle_repository.git
'''


def read_file_board(path: str) -> str:
    '''Reads game board from given file
    '''
    board = []
    with open(path, 'r') as file:
        for row in file:
            board.append(row.strip('\n'))

    return board

# print(read_file_board('puzzle_board.txt'))


def check_a_row_unicnes(row: str) -> bool:
    '''Checks unicness of numbers in a row.
    >>> check_a_row_unicnes('***  123 2*')
    False
    >>> check_a_row_unicnes('***  123 4*')
    True
    '''
    row = ''.join(row.replace('*', '').split(' '))
    return len(row) == len(set(row))


def check_rows_and_columns(board: str) -> bool:
    '''Checks the game board if numbers in rows
    and in columns  are different
    >>> check_rows_and_columns(['**  1****', '* 4 1****', ' 6  83  *', '3   1  **'])
    False
    '''
    new_board = []

    for index in range(len(board[0])):
        new_row = ''
        for row in board:
            new_row += row[index]
        new_board.append(new_row)

    for game in [board, new_board]:
        for row in game:
            if not check_a_row_unicnes(row):
                return False

    return True


def check_color_pattern(board: str) -> bool:
    '''Checks unicness of numbers in the same colour squares.
    >>> check_color_pattern(['**** ****', '***1 ****', '**  3****', '* 4 2****',\
    '     9 5 ', ' 6  83  *', '3   1  **', '  8  2***', '  2  ****'])
    True
    '''
    board = board[::-1]
    check_list = []

    for idx, row in enumerate(board[:5]):
        check_list += [row[idx: idx + 5]]
        for lower_row in board[idx + 1: idx + 5]:
            check_list[idx] += lower_row[idx]

    for row in check_list:
        if not check_a_row_unicnes(row):
            return False

    return True


def validate_board(board: list) -> bool:
    '''Checks whether the board is ready for the game.
    >>> validate_board(['**** ****', '***1 ****', '**  3****', '* 4 2****',\
    '     9 5 ', ' 6  83  *', '3   1  **', '  8  2***', '  2  ****'])
    True
    '''
    if not (check_rows_and_columns(board) and check_color_pattern(board)):
        return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
