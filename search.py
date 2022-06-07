from evaluator import classic_evaluator

# Brute force search:
# generate sequence of all possible moves (at given depth)
# and evalute leaf
def search_moves(board):
    search_depth = 5
    for i in board.legal_moves:
        board.push(i)
        val = classic_evaluator(board)
        print(i,val)
        board.pop()
        