from flask import Flask, render_template, request
import chess
import chess.svg
import random
import base64
import io
from evaluator import classic_evaluator

board = chess.Board()


def to_svg(board):
    return chess.svg.board(board)

def legal_moves_str(legal_moves):
    legal_moves_text = [f"{x}" for x in legal_moves]
    return legal_moves_text

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def self_play():
    legal_moves = list(board.legal_moves)
    legal_moves_text = legal_moves_str(legal_moves)

    requested_move = request.form.getlist('requested_move')
    AI_move = random.choice(legal_moves)
    move_number = board.fullmove_number

    if requested_move:
        try:
            move = chess.Move.from_uci(requested_move[0])
            if move in legal_moves:
                board.push(move)
                legal_moves_text = legal_moves_str(list(board.legal_moves))
            else:
                requested_move = '\'' + requested_move[0] + '\'' + ' is an illegal move!'
        except ValueError:
            requested_move = '\'' + requested_move[0] + '\'' + ' is not a chess move!'

    if request.form.get('AI move') == 'AI move':
        board.push(AI_move)
        legal_moves_text = legal_moves_str(list(board.legal_moves))
    
    if request.form.get('reset') == 'reset':
        board.reset()
        legal_moves_text = legal_moves_str(list(board.legal_moves))

    return render_template('index.html',
        svg_img=(to_svg(board)), 
        text=requested_move, legal_text=legal_moves_text,
        evaluation = classic_evaluator(board))



if __name__ == '__main__':
    app.run(debug=True)
