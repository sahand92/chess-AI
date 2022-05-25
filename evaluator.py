
def classic_evaluator(board):
# create list of pieces on the board
    piece_type = []
    piece_color_w =[]
    piece_color_b =[]

    for x in board.piece_map().values():
        piece_type.append(list([x.piece_type]))
        piece_color_w.append(list([int(not(x.color))]))
        piece_color_b.append(list([int(x.color)]))

    # map the list to piece values
    # piece: type -> value
    # p: 1 -> 1
    # n: 2 -> 3
    # b: 3 -> 3
    # r: 4 -> 5
    # q: 5 -> 9
    # k: 6 -> 0

    for i in range(len(piece_type)):
        if piece_type[i] == [5]:
            piece_type[i] = [9]
        if piece_type[i] == [2]:
            piece_type[i] = [3]
        if piece_type[i] == [4]:
            piece_type[i] = [5]
        if piece_type[i] == [6]:
            piece_type[i] = [0]

    # calculate sum for each color
    value_w = 0
    value_b = 0
    for i in range(len(piece_type)):
        value_w += piece_type[i][0]*piece_color_w[i][0]
        value_b += piece_type[i][0]*piece_color_b[i][0]

    return value_w-value_b