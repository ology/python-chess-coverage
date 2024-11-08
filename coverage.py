import chess
import re

board = chess.Board()
board.push_san("e4")
board.push_san("d5")

# print(board.parse_san('Nf3'))

# for m in board.legal_moves:
#     print(m)

# print(chess.PAWN)
# print(chess.piece_symbol(chess.PAWN))
# print(chess.piece_name(chess.PAWN))

def fetch_moves(posn):
    moves = []
    for m in board.legal_moves:
        string = str(m)
        # print(string)
        from_sq = string[0:2]
        to_sq = string[2:4]
        # print(f"F: {from_sq}, T: {to_sq}")
        if from_sq == posn:
            moves.append(to_sq)
    return moves

pieces = {
    "p": 1,
    "n": 2,
    "b": 3,
    "r": 4,
    "q": 5,
    "k": 6,
}
for square in chess.SQUARES:
    color = board.color_at(square)
    piece = board.piece_at(square)
    name = '-'
    if piece:
        posn = chess.square_name(square)
        lower = str(piece).lower()
        index = pieces[lower]
        name = chess.piece_name(index)
        board.turn = color
        moves = fetch_moves(posn)
        print(f"S: {square}, I: {index}, P: {posn}, C: {color}, P: {piece}, N: {name}, M: {moves}")

# attackers = board.attackers(chess.WHITE, chess.D5)
# print(attackers)

# coverage = {}

# can = chess.Move.from_uci("a2a5") in board.legal_moves
# print(can)
