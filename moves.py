def moves_rook(positions: list, x: int, y: int, colour: str) -> set:
    allowed = set()

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

    return allowed


def moves_bishop(positions: list, x: int, y: int, colour: str) -> set:
    allowed = set()

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

    return allowed


def moves_king(positions: list, x: int, y: int, colour: str) -> set:
    allowed = set()

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

    return allowed


def moves_knight(positions: list, x: int, y: int, colour: str) -> set:
    allowed = set()

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

        if y > 1:
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

    return allowed


def moves_pawn(positions: list, pre: dict, x: int, y: int, colour: str) -> set:
    allowed = set()

    if colour == "b":
        if positions[y + 1][x] == "":
            allowed.update({(x, y + 1)})

            if y == 1 and positions[3][x] == "":
                # first move, 2 spaces
                allowed.update({(x, 3)})

        if x > 0:
            if positions[y + 1][x - 1].startswith("w"):
                allowed.update({(x - 1, y + 1)})

            if positions[y][x - 1] == "w-p" and positions[y + 1][x - 1] == "":
                if pre["pawns"]["white"][x - 1] == 2:
                    allowed.update({(x - 1, y + 1)})

        if x < 7:
            if positions[y + 1][x + 1].startswith("w"):
                allowed.update({(x + 1, y + 1)})

            if positions[y][x + 1] == "w-p" and positions[y + 1][x + 1] == "":
                if pre["pawns"]["white"][x + 1] == 2:
                    allowed.update({(x + 1, y + 1)})

    elif colour == "w":
        if positions[y - 1][x] == "":
            allowed.update({(x, y - 1)})

            if y == 6 and positions[4][x] == "":
                # first move, 2 spaces
                allowed.update({(x, 4)})

        if x > 0:
            if positions[y - 1][x - 1].startswith("b"):
                allowed.update({(x - 1, y - 1)})

            if positions[y][x - 1] == "b-p" and positions[y - 1][x - 1] == "":
                if pre["pawns"]["black"][x - 1] == 2:
                    allowed.update({(x - 1, y - 1)})

        if x < 7:
            if positions[y - 1][x + 1].startswith("b"):
                allowed.update({(x + 1, y - 1)})

            if positions[y][x + 1] == "b-p" and positions[y - 1][x - 1] == "":
                if pre["pawns"]["black"][x + 1] == 2:
                    allowed.update({(x + 1, y - 1)})

    return allowed


def find_moves(positions: list, pre: dict, x: int, y: int) -> set:
    allowed = set()

    if positions[y][x]:
        colour, piece_id = positions[y][x].split("-")

        if piece_id in "QR":
            allowed.update(moves_rook(positions, x, y, colour))

        if piece_id in "QB":
            allowed.update(moves_bishop(positions, x, y, colour))

        if piece_id == "K":
            allowed.update(moves_king(positions, x, y, colour))

        if piece_id == "N":
            allowed.update(moves_knight(positions, x, y, colour))

        if piece_id == "p":
            allowed.update(moves_pawn(positions, pre, x, y, colour))

    return allowed


def calculate_check(positions: list, pre: dict) -> dict:
    in_check = {"black": False, "white": False}

    for y, rank in enumerate(positions):
        for x, file in enumerate(rank):
            available = find_moves(positions, pre, x, y)
            if not file.endswith("K"):
                for pos in available:
                    if positions[pos[1]][pos[0]]:
                        if positions[pos[1]][pos[0]].endswith("K"):
                            if positions[pos[1]][pos[0]].startswith("w"):
                                if file.startswith("b"):
                                    in_check["white"] = True

                            elif file.startswith("w"):
                                in_check["black"] = True

    return in_check


def find_legal_moves(positions: list, pre: dict, x: int, y: int) -> set:
    in_check = calculate_check(positions, pre)
    available = find_moves(positions, pre, x, y)
    allowed = set()
    if available:
        if positions[y][x].startswith("b"):
            colour = "black"

        else:
            colour = "white"

        for move in available:
            piece = positions[y][x]
            new_positions = [i.copy() for i in positions]
            new_positions[y][x] = ""
            new_positions[move[1]][move[0]] = piece

            if piece.endswith("p") and positions[move[1]][move[0]] == "":
                if x != move[0]:
                    # en-passant
                    if colour == "black":
                        new_positions[move[1] - 1][move[0]] = ""

                    else:
                        new_positions[move[1] + 1][move[0]] = ""

            if not calculate_check(new_positions, pre)[colour]:
                allowed.update({(move[0], move[1])})

    return allowed
