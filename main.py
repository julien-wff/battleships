# ---------- BOARD HELPERS ----------

def generate_board():
    return [[0] * 10 for i in range(10)]


axis_indices = {
    'x': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'y': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
}

def display_board(board):
    print(' ' * 5 + '  '.join(axis_indices['x']))
    for index, line in enumerate(board):
        text_index = axis_indices['y'][index]
        print(
            (' ' + text_index if len(text_index) == 1 else text_index) + '   ' +
            '  '.join([str(point) for point in line])
        )
    print('')


# ---------- GAME LOOP ----------

ships = [
    ["porte-avion", 1, 5],
    ["croiseur", 2, 4],
    ["contre-torpilleurs", 3, 3],
    ["sous-marin", 4, 3],
    ["torpilleur", 5, 2],
]

board1 = generate_board()
board2 = generate_board()


if __name__ == '__main__':
    display_board(board1)
