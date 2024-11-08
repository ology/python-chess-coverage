import chess
import re

pieces = {
    "p": 1,
    "n": 2,
    "b": 3,
    "r": 4,
    "q": 5,
    "k": 6,
}

# print(board.parse_san('Nf3'))

# for m in board.legal_moves:
#     print(m)

# print(chess.PAWN)
# print(chess.piece_symbol(chess.PAWN))
# print(chess.piece_name(chess.PAWN))

def fetch_moves(board, posn):
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

def fetch_threatens(board, moves):
    threatens = []
    for m in moves:
        string = str(m)
        square = chess.parse_square(string)
        piece = board.piece_at(square)
        if piece:
            threatens.append(string)
    return threatens

def fetch_protects(board, posn, square):
    protects = []
    fen = board.fen()
    parts = fen.split(" ", 1)
    flipped_fen = parts[0].swapcase()
    fen_extra = flipped_fen + " " + parts[1]
    board_copy = chess.Board(fen=fen_extra)
    piece = board_copy.piece_at(square)
    color = piece.color
    piece.color = not color
    board_copy.set_piece_at(square, piece)
    board_copy.turn = not color
    # print(posn)
    print(board_copy)
    moves = fetch_moves(board_copy, posn)
    # print(board_copy)
    # print(f"P: {posn}, C: {color}, M: {moves}")
    protects = fetch_threatens(board_copy, moves)
    return protects

board = chess.Board()
board.push_san("e4")
board.push_san("d5")

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
        moves = fetch_moves(board, posn)
        threatens = fetch_threatens(board, moves)
        protects = fetch_protects(board, posn, square)
        print(f"Sq: {square}, Pos: {posn}, C: {color}, P: {piece}, N: {name}, M: {moves}, T: {threatens}, Pr: {protects}")

# attackers = board.attackers(chess.WHITE, chess.D5)
# print(attackers)

# coverage = {}

# can = chess.Move.from_uci("a2a5") in board.legal_moves
# print(can)
