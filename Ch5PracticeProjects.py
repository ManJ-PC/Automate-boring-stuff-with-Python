valid_board = { 
    'e1': 'wking', 'e8': 'bking',
    'd1': 'wqueen', 'd8': 'bqueen',
    'a1': 'wrook', 'h1': 'wrook',
    'a8': 'brook', 'h8': 'brook',
    'b1': 'wknight', 'g1': 'wknight',
    'b8': 'bknight', 'g8': 'bknight',
    'c1': 'wbishop', 'f1': 'wbishop',
    'c8': 'bbishop', 'f8': 'bbishop',
    'a2': 'wpawn', 'b2': 'wpawn', 'c2': 'wpawn', 'd2': 'wpawn',
    'e2': 'wpawn', 'f2': 'wpawn', 'g2': 'wpawn', 'h2': 'wpawn',
    'a7': 'bpawn', 'b7': 'bpawn', 'c7': 'bpawn', 'd7': 'bpawn',
    'e7': 'bpawn', 'f7': 'bpawn', 'g7': 'bpawn', 'h7': 'bpawn',
    }

missing_king = {
    'e8': 'bking',
    'e1': 'wqueen'  # Missing white king
    }

extra_black_king = {
    'e1': 'wking', 'e8': 'bking',
    'd5': 'bking'  # Extra black king
    }

too_many_pawns = {
    'e1': 'wking', 'e8': 'bking',
    'a2': 'wpawn', 'b2': 'wpawn', 'c2': 'wpawn', 'd2': 'wpawn',
    'e2': 'wpawn', 'f2': 'wpawn', 'g2': 'wpawn', 'h2': 'wpawn',
    'a3': 'wpawn'  # One extra
    }

invalid_piece_name = {
    'e1': 'wking', 'e8': 'bking',
    'a2': 'wbanana'
    }

invalid_piece_color = {
    'e1': 'wking', 'e8': 'bking',
    'a2': 'zrook'
    }

invalid_position_file = {
    'e1': 'wking', 'e8': 'bking',
    'i3': 'wpawn'
    }

invalid_position_rank = {
    'e1': 'wking', 'e8': 'bking',
    'a9': 'wpawn'
    }

too_many_white_pieces = {
    'e1': 'wking', 'e8': 'bking',
    'a2': 'wpawn', 'b2': 'wpawn', 'c2': 'wpawn',
    'd2': 'wpawn', 'e2': 'wpawn', 'f2': 'wpawn',
    'g2': 'wpawn', 'h2': 'wpawn',
    'a3': 'wrook', 'b3': 'wrook', 'c3': 'wrook',
    'd3': 'wrook', 'e3': 'wrook', 'f3': 'wrook',
    'g3': 'wrook', 'h3': 'wrook',  # 9 white pieces + king = 10
    'g4': 'wqueen', 'h4': 'wbishop', 'a4': 'wbishop',
    'c4': 'wknight', 'd4': 'wknight', 'e4': 'wrook',
    }

def isValidChessBoard(chessBoard):
    """
    Check if the chess board is valid.
    :param chessBoard: dict
    :return: bool
    """
    chessBoard_count = {}
    numPieces = 0
    black_pieces=0
    white_pieces = 0

    for i in list(chessBoard.values()):
        chessBoard_count[i] = chessBoard_count.get(i, 0) + 1 # count number of pieces of each type
        if i[0] == 'b':
            black_pieces += 1 # count black pieces
        elif i[0] == 'w':
            white_pieces += 1 # count white pieces

    if chessBoard_count.get('bking', 0) > 1:
        print("🔴 RULE 1: Too many black kings.")
        return False
    elif chessBoard_count.get('wking', 0) > 1:
        print("🔴 RULE 2: Too many white kings.")
        return False
    elif black_pieces > 16:
        print("🔴 RULE 3: Too many black pieces.")
        return False
    elif white_pieces > 16:
        print("🔴 RULE 4: too many white pieces on the board.")
        return False
    elif len(chessBoard) > 32:
        print("🔴 RULE 5: Too many pieces on the board.")
        return False
    elif chessBoard_count.get('bpawn', 0) > 8 or chessBoard_count.get('wpawn', 0) > 8:
        print("🔴 RULE 6:   Too many pawns.")
        return False
    
    for i in list(chessBoard_count):
        if i[0] != 'b' and i[0] != 'w':
            print("There are too many pieces on the board.")
            return False
        elif i[1:] not in ['pawn', 'king', 'queen', 'rook', 'bishop', 'knight']:  #!= 'king' or i[1:] != 'queen' or i[1:] != 'rook' or i[1:] != 'bishop' or i[1:] != 'knight':
                print("There are invalid pieces on the board.")
                return False
    
    for i in chessBoard.keys():
        if len(i) !=2:
            print('Position is not valid: number')
            return False
        elif i[0] not in 'abcdefgh':
            print('Position is not valid: x-axis')
            return False
        elif i[1] not in '12345678':
            print('Position is not valid: y-axis')
            return False
    return True