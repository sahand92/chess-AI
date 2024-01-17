from evaluator import classic_evaluator
import chess

def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player=True):
    if depth == 0 or board.is_game_over():
        return classic_evaluator(board)

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# if __name__ == "__main__":
#     board = chess.Board()

#     print("Current Board:")
#     print(board)

#     # Search for the best move with a depth of 3 (you can adjust the depth)
#     best_move = None
#     best_eval = float('-inf')
#     alpha = float('-inf')
#     beta = float('inf')

#     for move in board.legal_moves:
#         board.push(move)
#         eval = minimax_alpha_beta(board, depth=5, alpha=alpha, beta=beta, maximizing_player=False)
#         board.pop()

#         if eval > best_eval:
#             best_eval = eval
#             best_move = move

#         alpha = max(alpha, eval)

#     print("\nBest Move:")
#     print(best_move)