import chess
def classic_evaluator(board):

    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0}
    
    val = 0.0
    pm = board.piece_map()
    for i in pm:
        val_i = piece_values[pm[i].piece_type]
        if pm[i].color == chess.WHITE:
            val += val_i
        else:
            val -= val_i

    return val