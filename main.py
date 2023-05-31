import tkinter
from PIL import Image, ImageTk
from figures import *
from moves import *


WIDTH = HEIGHT = 80
lkd = 0


def new_game():
    board = [[W_ROOK, W_KNIGHT, W_BISHOP, W_QUEEN, W_KING, W_BISHOP, W_KNIGHT, W_ROOK],
             [W_PAWN] * 8,
             [SPACE] * 8,
             [SPACE] * 8,
             [SPACE] * 8,
             [SPACE] * 8,
             [B_PAWN] * 8,
             [B_ROOK, B_KNIGHT, B_BISHOP, B_QUEEN, B_KING, B_BISHOP, B_KNIGHT, B_ROOK]]
    return board


def show_figure():
    c.delete("all")
    for i in range(4):
        for j in range(5):
            c.create_rectangle((WIDTH * i * 2 + WIDTH, HEIGHT * j * 2), (WIDTH * i * 2 + 2*WIDTH, HEIGHT * j * 2 + HEIGHT), outline="white",
                               fill="white")
    for i in range(4):
        for j in range(5):
            c.create_rectangle((WIDTH * i * 2, HEIGHT * j * 2 + HEIGHT), (WIDTH * i * 2 + WIDTH, HEIGHT * j * 2 + 2*HEIGHT), outline="white",
                               fill="white")
    c.create_rectangle((0, 0), (640, 80), outline="white", fill="white")
    c.create_rectangle((0, 720), (640, 800), outline="white", fill="white")
    c.create_line((0, 80), (640, 80), width=4, fill="#BD8926")
    c.create_line((4, 80), (4, 720), width=4, fill="#BD8926")
    c.create_line((640, 80), (640, 720), width=4, fill="#BD8926")
    c.create_line((0, 720), (640, 720), width=4, fill="#BD8926")
    for i in range(8):
        for j in range(8):
            if board[j][i]:
                c.create_image(i * WIDTH, 640 - j * HEIGHT, anchor="nw", image=pieces[board[j][i]])
    if si >= 0:
        c.create_rectangle((si * WIDTH, 640 - sj * HEIGHT), (si * WIDTH + WIDTH, 640 - sj * HEIGHT + HEIGHT), outline="#1de300", width="5")
        if board[sj][si]:
            c.create_image(si * WIDTH, 640 - sj * HEIGHT, anchor="nw", image=pieces[board[sj][si]])
        if fi >= 0:
            c.create_rectangle((fi * WIDTH, 640 - fj * HEIGHT), (fi * WIDTH + WIDTH, 640 - fj * HEIGHT + HEIGHT), outline="#1de300", width="5")
            if board[fj][fi]:
                c.create_image(fi * WIDTH, 640 - fj * HEIGHT, anchor="nw", image=pieces[board[fj][fi]])
    if lf > 0:
        c.create_rectangle((599, 44), (639, 4), outline="black", fill="black", width="5")
    else:
        c.create_rectangle((599, 44), (639, 4), outline="black", fill="white", width="5")
    if Check_Win_White(board):
        c.create_rectangle((0, 0), (640, 800), outline="white", fill="white", width="5")
        c.create_text(320, 400, text="WHITE WIN", font='200')
    if Check_Win_Black(board):
        c.create_rectangle((0, 0), (640, 800), outline="#BD8926", fill="#BD8926", width="5")
        c.create_text(320, 400, text="BLACK WIN", font='200')


def load_pieces():
    pieces[W_PAWN] = ImageTk.PhotoImage(Image.open("images/wP.png"))
    pieces[W_KNIGHT] = ImageTk.PhotoImage(Image.open("images/wN.png"))
    pieces[W_BISHOP] = ImageTk.PhotoImage(Image.open("images/wB.png"))
    pieces[W_ROOK] = ImageTk.PhotoImage(Image.open("images/wR.png"))
    pieces[W_QUEEN] = ImageTk.PhotoImage(Image.open("images/wQ.png"))
    pieces[W_KING] = ImageTk.PhotoImage(Image.open("images/wK.png"))
    pieces[B_PAWN] = ImageTk.PhotoImage(Image.open("images/bP.png"))
    pieces[B_KNIGHT] = ImageTk.PhotoImage(Image.open("images/bN.png"))
    pieces[B_BISHOP] = ImageTk.PhotoImage(Image.open("images/bB.png"))
    pieces[B_ROOK] = ImageTk.PhotoImage(Image.open("images/bR.png"))
    pieces[B_QUEEN] = ImageTk.PhotoImage(Image.open("images/bQ.png"))
    pieces[B_KING] = ImageTk.PhotoImage(Image.open("images/bK.png"))


def click(event):
    global si, sj, fi, fj, lkd, lf, end
    ci, cj = event.x // WIDTH, abs(event.y // HEIGHT - 8)
    print(board[cj][ci])
    if Check_Win_White(board) or Check_Win_Black(board):
        return False
    elif (lf > 0 and board[cj][ci] > 0 and si == -1 and sj == -1) or (lf < 0 and board[cj][ci] < 0 and si == -1 and sj == -1):
        return False
    else:
        if fi >= 0:
            if board[cj][ci]:
                si, sj, fi, fj = ci, cj, -1, -1
        else:
            if abs(board[sj][si]) == W_PAWN and pawn_move(board, si, sj, ci, cj):
                print(pawn_move(board, si, sj, ci, cj))
                make_move(board, si, sj, ci, cj)
                si = sj = fj = -1
                fi = 0
                lf *= -1
            if abs(board[sj][si]) == W_KNIGHT and knight_move(board, si, sj, ci, cj):
                print(knight_move(board, si, sj, ci, cj))
                make_move(board, si, sj, ci, cj)
                si = sj = fj = -1
                fi = 0
                lf *= -1
            if abs(board[sj][si]) == W_BISHOP and bishop_move(board, si, sj, ci, cj):
                print(bishop_move(board, si, sj, ci, cj))
                make_move(board, si, sj, ci, cj)
                si = sj = fj = -1
                fi = 0
                lf *= -1
            if abs(board[sj][si]) == W_ROOK and rook_move(board, si, sj, ci, cj):
                print(rook_move(board, si, sj, ci, cj))
                make_move(board, si, sj, ci, cj)
                si = sj = fj = -1
                fi = 0
                lf *= -1
            if abs(board[sj][si]) == W_QUEEN and queen_move(board, si, sj, ci, cj):
                print(queen_move(board, si, sj, ci, cj))
                make_move(board, si, sj, ci, cj)
                si = sj = fj = -1
                fi = 0
                lf *= -1
            if abs(board[sj][si]) == W_KING and king_move(board, si, sj, ci, cj):
                print(king_move(board, si, sj, ci, cj))
                make_move(board, si, sj, ci, cj)
                si = sj = fj = -1
                fi = 0
                lf *= -1
    show_figure()
    print(si, sj, fi, fj)


def Check_Win_White(board):
    f1 = False
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == B_KING:
                f1 = True
    if not f1:
        print("WHITE WIN")
        return True
    else:
        return False


def Check_Win_Black(board):
    f2 = False
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == W_KING:
                f2 = True
    if not f2:
        print("BLACK WIN")
        return True
    else:
        return False


pieces = {}
si = sj = fj = -1
fi = 0
lf = -1
w = tkinter.Tk()
w.title("Шахматы")
c = tkinter.Canvas(width=640, height=800, bg="#BD8926")
c.pack()
c.bind("<Button-1>", click)
board = new_game()
load_pieces()
show_figure()
w.mainloop()
