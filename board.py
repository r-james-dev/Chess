import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

pygame.init()

display = pygame.display.set_mode((400, 400))

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


def find_moves(positions, x, y):
    allowed = set()
    if positions[y][x]:
        colour, piece_id = positions[y][x].split("-")
        if in_check[colour]:
            pass

        if piece_id in "QR":
            # left, right, up and down moves

            # left
            piece_collision = False
            tmp = x
            while tmp > 0 and not piece_collision:
                tmp -= 1
                if positions[y][tmp] == "":
                    allowed.update({(tmp, y)})

                elif colour == "b" and positions[y][tmp].startswith("w"):
                    allowed.update({(tmp, y)})
                    piece_collision = True

                elif colour == "w" and positions[y][tmp].startswith("b"):
                    allowed.update({(tmp, y)})
                    piece_collision = True

                else:
                    piece_collision = True

            # right
            piece_collision = False
            tmp = x
            while tmp < 7 and not piece_collision:
                tmp += 1
                if positions[y][tmp] == "":
                    allowed.update({(tmp, y)})

                elif colour == "b" and positions[y][tmp].startswith("w"):
                    allowed.update({(tmp, y)})
                    piece_collision = True

                elif colour == "w" and positions[y][tmp].startswith("b"):
                    allowed.update({(tmp, y)})
                    piece_collision = True

                else:
                    piece_collision = True

            # up
            piece_collision = False
            tmp = y
            while tmp > 0 and not piece_collision:
                tmp -= 1
                if positions[tmp][x] == "":
                    allowed.update({(x, tmp)})

                elif colour == "b" and positions[tmp][x].startswith("w"):
                    allowed.update({(x, tmp)})
                    piece_collision = True

                elif colour == "w" and positions[tmp][x].startswith("b"):
                    allowed.update({(x, tmp)})
                    piece_collision = True

                else:
                    piece_collision = True

            # down
            piece_collision = False
            tmp = y
            while tmp < 7 and not piece_collision:
                tmp += 1
                if positions[tmp][x] == "":
                    allowed.update({(x, tmp)})

                elif colour == "b" and positions[tmp][x].startswith("w"):
                    allowed.update({(x, tmp)})
                    piece_collision = True

                elif colour == "w" and positions[tmp][x].startswith("b"):
                    allowed.update({(x, tmp)})
                    piece_collision = True

                else:
                    piece_collision = True

        if piece_id in "QB":
            # diagonol moves

            # left, up
            piece_collision = False
            tmp_x, tmp_y = x, y
            while tmp_x > 0 and tmp_y > 0 and not piece_collision:
                tmp_x -= 1
                tmp_y -= 1
                if positions[tmp_y][tmp_x] == "":
                    allowed.update({(tmp_x, tmp_y)})

                elif colour == "b" and positions[tmp_y][tmp_x].startswith("w"):
                    allowed.update({(tmp_x, tmp_y)})
                    piece_collision = True

                elif colour == "w" and positions[tmp_y][tmp_x].startswith("b"):
                    allowed.update({(tmp_x, tmp_y)})
                    piece_collision = True

                else:
                    piece_collision = True

            # right, up
            piece_collision = False
            tmp_x, tmp_y = x, y
            while tmp_x < 7 and tmp_y > 0 and not piece_collision:
                tmp_x += 1
                tmp_y -= 1
                if positions[tmp_y][tmp_x] == "":
                    allowed.update({(tmp_x, tmp_y)})

                elif colour == "b" and positions[tmp_y][tmp_x].startswith("w"):
                    allowed.update({(tmp_x, tmp_y)})
                    piece_collision = True

                elif colour == "w" and positions[tmp_y][tmp_x].startswith("b"):
                    allowed.update({(tmp_x, tmp_y)})
                    piece_collision = True

                else:
                    piece_collision = True

            # left, down
            piece_collision = False
            tmp_x, tmp_y = x, y
            while tmp_x > 0 and tmp_y < 7 and not piece_collision:
                tmp_x -= 1
                tmp_y += 1
                if positions[tmp_y][tmp_x] == "":
                    allowed.update({(tmp_x, tmp_y)})

                elif colour == "b" and positions[tmp_y][tmp_x].startswith("w"):
                    allowed.update({(tmp_x, tmp_y)})
                    piece_collision = True

                elif colour == "w" and positions[tmp_y][tmp_x].startswith("b"):
                    allowed.update({(tmp_x, tmp_y)})
                    piece_collision = True

                else:
                    piece_collision = True

            # right, down
            piece_collision = False
            tmp_x, tmp_y = x, y
            while tmp_x < 7 and tmp_y < 7 and not piece_collision:
                tmp_x += 1
                tmp_y += 1
                if positions[tmp_y][tmp_x] == "":
                    allowed.update({(tmp_x, tmp_y)})

                elif colour == "b" and positions[tmp_y][tmp_x].startswith("w"):
                    allowed.update({(tmp_x, tmp_y)})
                    piece_collision = True

                elif colour == "w" and positions[tmp_y][tmp_x].startswith("b"):
                    allowed.update({(tmp_x, tmp_y)})
                    piece_collision = True

                else:
                    piece_collision = True

        if piece_id == "K":
            if y:
                ranks = positions[y - 1 : y + 2]
                y_offset = y - 1

            else:
                ranks = positions[: 2]
                y_offset = y

            if x:
                if x < 7:
                    files = range(x - 1, x + 2)

                else:
                    files = range(6, 8)

            else:
                files = range(2)

            for tmp_y, row in enumerate(ranks):
                for tmp_x in files:
                    if row[tmp_x] == "":
                        allowed.update({(tmp_x, y_offset + tmp_y)})

                    elif colour == "b" and row[tmp_x].startswith("w"):
                        allowed.update({(tmp_x, y_offset + tmp_y)})

                    elif colour == "w" and row[tmp_x].startswith("b"):
                        allowed.update({(tmp_x, y_offset + tmp_y)})

        if piece_id == "N":
            coords = []
            if y < 7:
                if x < 6:
                    coords.append((x + 2, y + 1))

                if x > 1:
                    coords.append((x - 2, y + 1))

            if y < 6:
                if x < 7:
                    coords.append((x + 1, y + 2))

                if x:
                    coords.append((x - 1, y + 2))

            if y:
                if x < 6:
                    coords.append((x + 2, y - 1))

                if x > 1:
                    coords.append((x - 2, y - 1))

                if y > 2:
                    if x < 7:
                        coords.append((x + 1, y - 2))

                    if x:
                        coords.append((x - 1, y - 2))

            for tmp_x, tmp_y in coords:
                if positions[tmp_y][tmp_x] == "":
                    allowed.update({(tmp_x, tmp_y)})

                if colour == "b" and positions[tmp_y][tmp_x].startswith("w"):
                    allowed.update({(tmp_x, tmp_y)})

                if colour == "w" and positions[tmp_y][tmp_x].startswith("b"):
                    allowed.update({(tmp_x, tmp_y)})

        if piece_id == "p":
            if colour == "b":
                if positions[y + 1][x] == "":
                    allowed.update({(x, y + 1)})

                    if y == 1 and positions[3][x] == "":
                        # first move, 2 spaces
                        allowed.update({(x, 3)})

                if x > 0 and positions[y + 1][x - 1].startswith("w"):
                    allowed.update({(x - 1, y + 1)})

                if x < 7 and positions[y + 1][x + 1].startswith("w"):
                    allowed.update({(x + 1, y + 1)})

            elif colour == "w":
                if positions[y - 1][x] == "":
                    allowed.update({(x, y - 1)})

                    if y == 6 and positions[4][x] == "":
                        # first move, 2 spaces
                        allowed.update({(x, 4)})

                if x > 0 and positions[y - 1][x - 1].startswith("b"):
                    allowed.update({(x - 1, y - 1)})

                if x < 7 and positions[y - 1][x + 1].startswith("b"):
                    allowed.update({(x + 1, y - 1)})

    return allowed


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

in_check = {"b": False, "w": False}
highlighted = ()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            x //= 50
            y //= 50

            if highlighted == (x, y):
                highlighted = ()

            else:
                highlighted = (x, y)

    # draw checkered pattern
    colours = ((50, 50, 50), (255, 255, 255))
    colour_idx = 0
    for y in range(8):
        colour_idx = not colour_idx
        for x in range(8):
            pygame.draw.rect(display, colours[colour_idx], pygame.Rect(x * 50, y * 50, 50, 50))
            colour_idx = not colour_idx

    # highlight spaces
    if highlighted:
        moves = list(find_moves(positions, *highlighted))
        if moves:
            highlight_square(display, *highlighted, colour="#00FF00")
            for file, rank in moves:
                highlight_square(display, file, rank)

        else:
            highlighted = ()

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
