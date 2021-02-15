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

    draw_piece(display, "R", "black", 0, 0)
    draw_piece(display, "N", "black", 1, 0)
    draw_piece(display, "B", "black", 2, 0)
    draw_piece(display, "Q", "black", 3, 0)
    draw_piece(display, "K", "black", 4, 0)
    draw_piece(display, "B", "black", 5, 0)
    draw_piece(display, "N", "black", 6, 0)
    draw_piece(display, "R", "black", 7, 0)

    draw_piece(display, "p", "black", 0, 1)
    draw_piece(display, "p", "black", 1, 1)
    draw_piece(display, "p", "black", 2, 1)
    draw_piece(display, "p", "black", 3, 1)
    draw_piece(display, "p", "black", 4, 1)
    draw_piece(display, "p", "black", 5, 1)
    draw_piece(display, "p", "black", 6, 1)
    draw_piece(display, "p", "black", 7, 1)

    draw_piece(display, "R", "white", 0, 7)
    draw_piece(display, "N", "white", 1, 7)
    draw_piece(display, "B", "white", 2, 7)
    draw_piece(display, "Q", "white", 3, 7)
    draw_piece(display, "K", "white", 4, 7)
    draw_piece(display, "B", "white", 5, 7)
    draw_piece(display, "N", "white", 6, 7)
    draw_piece(display, "R", "white", 7, 7)

    draw_piece(display, "p", "white", 0, 6)
    draw_piece(display, "p", "white", 1, 6)
    draw_piece(display, "p", "white", 2, 6)
    draw_piece(display, "p", "white", 3, 6)
    draw_piece(display, "p", "white", 4, 6)
    draw_piece(display, "p", "white", 5, 6)
    draw_piece(display, "p", "white", 6, 6)
    draw_piece(display, "p", "white", 7, 6)

    pygame.display.flip()

pygame.quit()
