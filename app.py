from flask import Flask, render_template, Markup, request
import chess
import chess.svg
import base64
import io

board = chess.Board()


def to_svg(board):
    return chess.svg.board(board)


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def self_play():
    legal_moves = list(board.legal_moves)
    legal_moves_str = ""
    for i in range(len(legal_moves)):
        legal_moves_str += f"{legal_moves[i]}\n"
    move_text = request.form.getlist('text')

    if move_text:
        try:
            move = chess.Move.from_uci(move_text[0])
            if move in legal_moves:
                board.push(move)
            else:
                move_text = '\'' + move_text[0] + '\'' + ' is an illegal move!'
        except ValueError:
            move_text = '\'' + move_text[0] + '\'' + ' is not a chess move!'
    if request.form.get('reset') == 'reset':
        board.reset()
    return render_template('index.html', svg_img=Markup(to_svg(board)), text=move_text)



#    return str(list(board.legal_moves))

if __name__ == '__main__':
    app.run(debug=True)
