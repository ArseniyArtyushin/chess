from figures import *


def pawn_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if di != 0:
        return abs(di) == 1 and dj * board[sj][si] == 1 and board[fj][fi] != SPACE and board[sj][si] * board[fj][fi] > 0
    if board[fj][fi] != SPACE:
        return False
    if board[sj][si] > 0 and sj == 1 and dj == 2 and board[sj+1][si] == SPACE:
        return True
    if board[sj][si] < 0 and sj == 6 and dj == -2 and board[sj-1][si] == SPACE:
        return True
    if di == 0 and dj == 0:
        return True
    return abs(dj) == 1 and dj * board[sj][si] > 0


def knight_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if board[sj][si] * board[fj][fi] > 0:
        return False
    if (abs(dj) == 1 and abs(di) == 2) or (abs(dj) == 2 and abs(di) == 1):
        return True
    if di == 0 and dj == 0:
        return True


def bishop_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if board[fj][fi] != SPACE:
        return False
    if abs(di) == abs(dj) and check_empty(board, si, sj, fi, fj):
        return True


def rook_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if board[fj][fi] != SPACE:
        return False
    if (di == 0 or dj == 0) and check_empty(board, si, sj, fi, fj):
        return True


def queen_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if board[fj][fi] != SPACE:
        return False
    if (di == 0 or dj == 0) or (abs(di) == abs(dj)) and check_empty(board, si, sj, fi, fj):
        return True


def king_move(board, si, sj, fi, fj):
    di = fi - si
    dj = fj - sj
    if board[fj][fi] != SPACE:
        return False
    if ((di == 0 and abs(dj) == 1) or (dj == 0 and abs(di) == 1)) or (abs(di) == abs(dj) == 1):
        return True
    if di == 0 and dj == 0:
        return True


def check_empty(board, si, sj, fi, fj):
    di = 1 if fi > si else 0 if fi == si else -1
    dj = 1 if fj > sj else 0 if fj == sj else -1
    i, j = si, sj
    while 0 <= i < 8 and 0 <= j < 8:
        i += di
        j += dj
        if (i, j) == (fi, fj):
            return True
        if board[j][i] != SPACE:
            return False
    return False




def make_move(board, si, sj, fi, fj):
    board[fj][fi] = board[sj][si]
    board[sj][si] = SPACE
