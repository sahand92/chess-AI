from flask import Flask, render_template, Markup, request
import chess
import chess.svg
import base64
import io
from evaluator import classic_evaluator

board = chess.Board()


def to_svg(board):
    return chess.svg.board(board)

def legal_moves_str(legal_moves):
    legal_moves_text = ""
    for i in range(len(legal_moves)):
        legal_moves_text += f"{legal_moves[i]},\n"
    return legal_moves_text

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def self_play():
    legal_moves = list(board.legal_moves)
    legal_moves_text = legal_moves_str(legal_moves)

    move_text = request.form.getlist('text')
    move_number = board.fullmove_number

    if move_text:
        try:
            move = chess.Move.from_uci(move_text[0])
            if move in legal_moves:
                board.push(move)
                legal_moves_text = legal_moves_str(list(board.legal_moves))
            else:
                move_text = '\'' + move_text[0] + '\'' + ' is an illegal move!'
        except ValueError:
            move_text = '\'' + move_text[0] + '\'' + ' is not a chess move!'
    
    if request.form.get('reset') == 'reset':
        board.reset()
        legal_moves_text = legal_moves_str(list(board.legal_moves))
    return render_template('index.html',
     svg_img=Markup(to_svg(board)), 
    text=move_text, legal_text=legal_moves_text,
     evaluation = classic_evaluator(board))



if __name__ == '__main__':
    app.run(debug=True)
