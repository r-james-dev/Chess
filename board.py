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


positions = [
    ["b-R", "b-N", "b-B", "b-Q", "b-K", "b-B", "b-N", "b-R"],
    ["b-p"] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    ["w-p"] * 8,
    ["w-R", "w-N", "w-B", "w-Q", "w-K", "w-B", "w-N", "w-R"]
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    colours = ((50, 50, 50), (255, 255, 255))
    colour_idx = 0
    for y in range(8):
        colour_idx = not colour_idx
        for x in range(8):
            pygame.draw.rect(display, colours[colour_idx], pygame.Rect(x * 50, y * 50, 50, 50))
            colour_idx = not colour_idx

    for y, row in enumerate(positions):
        for x, piece in enumerate(row):
            if piece == "":
                continue

            colour, piece_id = piece.split("-")
            colour = "black" if colour == "b" else "white"
            draw_piece(display, piece_id, colour, x, y)

    pygame.display.flip()

pygame.quit()
