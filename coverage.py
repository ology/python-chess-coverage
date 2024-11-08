import chess
import json

class Coverage:
    def __init__(self, board):
        self.board = board

    def fetch_moves(self, board, posn):
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

    def fetch_threatens(self, board, moves):
        threatens = []
        for m in moves:
            string = str(m)
            square = chess.parse_square(string)
            piece = board.piece_at(square)
            if piece:
                threatens.append(string)
        return threatens

    def is_king(self, posn):
        square = chess.parse_square(posn)
        piece = self.board.piece_at(square)
        if piece.symbol().lower() == 'k':
            return True
        return False

    def fetch_protects(self, posn, square):
        protects = []
        fen = self.board.fen()
        parts = fen.split(" ", 1)
        flipped_fen = parts[0].swapcase()
        fen_extra = flipped_fen + " " + parts[1]
        board_copy = chess.Board(fen=fen_extra)
        piece = board_copy.piece_at(square)
        color = piece.color
        piece.color = not color
        board_copy.set_piece_at(square, piece)
        board_copy.turn = not color
        moves = self.fetch_moves(board_copy, posn)
        protects = self.fetch_threatens(board_copy, moves)
        for i in protects:
            if self.is_king(i):
                protects.remove(i)
                break
        return protects

    def can_move_here(self, coverage, posn, color_name, moves):
        for m in moves:
            string = str(m)
            square = chess.parse_square(string)
            piece = self.board.piece_at(square)
            if not piece:
                if not string in coverage:
                    coverage[string] = {}
                key = color_name + "_can_move_here"
                if not key in coverage[string]:
                    coverage[string][key] = []
                coverage[string][key].append(posn)
                # print(f"M: {string}, K: {key}, P: {posn}")
                # print(f"C: {coverage[string][key]}")

    def cover(self):
        coverage = {}
        for square in chess.SQUARES:
            color = self.board.color_at(square)
            piece = self.board.piece_at(square)
            pieces = {
                "p": 1,
                "n": 2,
                "b": 3,
                "r": 4,
                "q": 5,
                "k": 6,
            }
            name = '-'
            if piece:
                posn = chess.square_name(square)
                lower = str(piece).lower()
                index = pieces[lower]
                name = chess.piece_name(index)
                self.board.turn = color
                if color:
                    color_name = 'white'
                else:
                    color_name = 'black'
                moves = self.fetch_moves(self.board, posn)
                threatens = self.fetch_threatens(self.board, moves)
                protects = self.fetch_protects(posn, square)
                coverage[posn] = {
                    "index": square,
                    "position": posn,
                    "color": color,
                    "occupant": f"{color_name} {name}",
                    "symbol": lower,
                    "moves": moves,
                    "threatens": threatens,
                    "protects": protects,
                }
                self.can_move_here(coverage, posn, color_name, moves)
        for posn in coverage:
            c = coverage[posn]
            if not "is_threatened_by" in c:
                c["is_threatened_by"] = []
            if not "is_protected_by" in c:
                c["is_protected_by"] = []
            for i in coverage:
                cov = coverage[i]
                if i == posn:
                    continue
                if ('threatens' in cov) and (posn in cov['threatens']):
                    c["is_threatened_by"].append(i)
                if ('protects' in cov) and (posn in cov['protects']):
                    c["is_protected_by"].append(i)
        return coverage

def main():
    board = chess.Board()
    board.push_san("e4")
    board.push_san("d5")
    c = Coverage(board)
    coverage = c.cover()
    print(json.dumps(coverage, indent=2, sort_keys=True))
    print(board)

if __name__ == "__main__":
    main()
