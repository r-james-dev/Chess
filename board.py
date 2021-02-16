from moves import find_moves
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

pygame.init()

display = pygame.display.set_mode((400, 400))

# images courtesy of my shitty pixel art skills
images = {
    "black": {
        "B": pygame.image.load("assets/b-black.png"),
        "K": pygame.image.load("assets/k-black.png"),
        "N": pygame.image.load("assets/n-black.png"),
        "p": pygame.image.load("assets/p-black.png"),
        "Q": pygame.image.load("assets/q-black.png"),
        "R": pygame.image.load("assets/r-black.png")
    },
    "white": {
        "B": pygame.image.load("assets/b-white.png"),
        "K": pygame.image.load("assets/k-white.png"),
        "N": pygame.image.load("assets/n-white.png"),
        "p": pygame.image.load("assets/p-white.png"),
        "Q": pygame.image.load("assets/q-white.png"),
        "R": pygame.image.load("assets/r-white.png")
    }
}

def draw_piece(display, piece, colour, x, y):
    x *= 50
    y *= 50
    piece = images[colour][piece]
    x += 25 - piece.get_width() / 2
    y += 25 - piece.get_height() / 2
    display.blit(piece, (x, y))


def highlight_square(display, x, y, colour="#FFFF00"):
    pygame.draw.rect(display, colour, pygame.Rect(x * 50, y * 50, 50, 50))


positions = [
    ["b-R", "b-N", "b-B", "b-Q", "b-K", "b-B", "b-N", "b-R"],
    ["b-p"] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    ["w-p"] * 8,
    ["w-R", "w-N", "w-B", "w-Q", "w-K", "w-B", "w-N", "w-R"],
]

have_moved = {
    "pawns": {
        "black": [0] * 8,
        "white": [0] * 8
    },
    "kings": {
        "black": 0,
        "white": 0
    },
    "rooks": {
        "black": [0, 0],
        "white": [0, 0]
    }
}

in_check = {"b": False, "w": False}
highlighted = []
selected = None

turn = "white"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            x //= 50
            y //= 50

            if (x, y) in highlighted and selected is not None:
                # move piece

                # en passant only possible on first move
                have_moved["pawns"]["black"] = [
                    1 if i == 2 else i for i in have_moved["pawns"]["black"]
                ]
                have_moved["pawns"]["white"] = [
                    1 if i == 2 else i for i in have_moved["pawns"]["white"]
                ]

                if positions[selected[1]][selected[0]].endswith("p"):
                    if positions[selected[1]][selected[0]].startswith("b"):
                        col = "black"

                    else:
                        col = "white"

                    if have_moved["pawns"][col][x] == 0:
                        if col == "black" and y == 3 and selected[0] == x:
                            print(x, y)
                            have_moved["pawns"][col][x] = 2

                        elif col == "white" and y == 4 and selected[0] == x:
                            print(x, y)
                            have_moved["pawns"][col][x] = 2

                        elif selected[0] == x:
                            have_moved["pawns"][col][x] = 1

                piece = positions[selected[1]][selected[0]]
                if piece.endswith("p") and positions[y][x] == "":
                    if selected[0] != x:
                        # doing en passant
                        if piece.startswith("b"):
                            positions[y - 1][x] = ""

                        else:
                            positions[y + 1][x] = ""

                positions[selected[1]][selected[0]] = ""
                positions[y][x] = piece
                highlighted = []
                selected = None
                turn = "black" if turn == "white" else "white"

            elif positions[y][x]:
                # view possible moves
                if turn == "white" and positions[y][x].startswith("b"):
                    continue

                if turn == "black" and positions[y][x].startswith("w"):
                    continue

                moves = list(find_moves(positions, have_moved, x, y))
                highlighted = []

                if moves:
                    selected = (x, y)
                    highlight_square(display, x, y, colour="#00FF00")
                    for file, rank in moves:
                        highlighted.append((file, rank))

    # draw checkered pattern
    colours = ((50, 50, 50), (255, 255, 255))
    colour_idx = 0
    for y in range(8):
        colour_idx = not colour_idx
        for x in range(8):
            pygame.draw.rect(display, colours[colour_idx], pygame.Rect(
                x * 50, y * 50, 50, 50
            ))
            colour_idx = not colour_idx

    # highlight spaces
    for file, rank in highlighted:
        highlight_square(display, file, rank)

    # draw pieces
    for y, row in enumerate(positions):
        for x, piece in enumerate(row):
            if piece == "":
                continue

            colour, piece_id = piece.split("-")
            colour = "black" if colour == "b" else "white"
            draw_piece(display, piece_id, colour, x, y)

    pygame.display.flip()

pygame.quit()
