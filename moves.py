from figures import *


def pawn_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if di != 0:
        return False
    if board[fj][fi] != SPACE:
        return False
    if board[sj][si] > 0 and sj == 1 and dj == 2:
        return True
    if board[sj][si] < 0 and sj == 6 and dj == -2:
        return True
    return abs(dj) == 1 and dj * board[sj][si] > 0


def knight_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if board[fj][fi] != SPACE:
        return False
    if (abs(dj) == 1 and abs(di) == 2) or (abs(dj) == 2 and abs(di) == 1):
        return True


def bishop_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if board[fj][fi] != SPACE:
        return False
    if abs(di) == abs(dj):
        return True


def rook_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if board[fj][fi] != SPACE:
        return False
    if di == 0 or dj == 0:
        return True


def queen_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if board[fj][fi] != SPACE:
        return False
    if (di == 0 or dj == 0) or (abs(di) == abs(dj)):
        return True


def king_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if board[fj][fi] != SPACE:
        return False
    if ((di == 0 and abs(dj) == 1) or (dj == 0 and abs(di) == 1)) or (abs(di) == abs(dj) == 1):
        return True


def make_move(board, si, sj, fi, fj):
    board[fj][fi] = board[sj][si]
    board[sj][si] = SPACE