import os
from math import cos, sin

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

os.environ["SDL_VIDEO_CENTERED"] = "1"
RES = WIDTH, HEIGHT = 800, 800
FPS = 60

PIXEL_WIDTH = 20
PIXEL_HEIGHT = 20

X_PIXEL = 0
Y_PIXEL = 0

SCREEN_WIDTH = WIDTH // PIXEL_WIDTH
SCREEN_HEIGHT = HEIGHT // PIXEL_HEIGHT
SCREEN_SIZE = SCREEN_WIDTH * SCREEN_HEIGHT

A, B = 0, 0

THETA_SPACING = 10
PHI_SPACING = 3

CHARS = ".,-~:;=!*#$@"

R1 = 10
R2 = 20
K2 = 200
K1 = SCREEN_HEIGHT * K2 * 3 / (8 * (R1 + R2))

pygame.init()

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20, bold=True)


def text_display(char, x, y):
    text = font.render(str(char), True, WHITE)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


k = 0
PAUSED = False

RUNNING = True
while RUNNING:
    clock.tick(FPS)
    pygame.display.set_caption("FPS: {:.2f}".format(clock.get_fps()))
    screen.fill(BLACK)

    output = [" "] * SCREEN_SIZE
    zbuffer = [0] * SCREEN_SIZE

    for theta in range(
        0, 628, THETA_SPACING
    ):  # theta goes around the cross-sectional circle of a torus, from 0 to 2phi
        for phi in range(
            0, 628, PHI_SPACING
        ):  # phi goes around the center of revolution of a torus, from 0 to 2phi

            cosA = cos(A)
            sinA = sin(A)
            cosB = cos(B)
            sinB = sin(B)

            costheta = cos(theta)
            sintheta = sin(theta)
            cosphi = cos(phi)
            sinphi = sin(phi)

            # x. y coordinates before revolving
            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            # 3D (x, y, z) coordinates after rotation
            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z  # one over z

            # x, y projection
            xp = int(SCREEN_WIDTH / 2 + K1 * ooz * x)
            yp = int(SCREEN_HEIGHT / 2 - K1 * ooz * y)

            position = xp + SCREEN_WIDTH * yp

            # luminance (L ranges from -sqrt(S) to sqrt(S))
            L = (
                cosphi * costheta * sinB
                - cosA * costheta * sinphi
                - sinA * sintheta
                + cosB * (cosA * sintheta - costheta * sinA * sinphi)
            )

            if ooz > zbuffer[position]:
                # larger ooz means the pixel is closer to the viewer than what's already plotted
                zbuffer[position] = ooz
                # we multiply by 8 to get luminance_index range 0..11 (8 * sqrt(2) == 11)
                luminance_index = int(L * 8)
                output[position] = CHARS[luminance_index if luminance_index > 0 else 0]

    for i in range(SCREEN_HEIGHT):
        Y_PIXEL += PIXEL_HEIGHT
        for j in range(SCREEN_WIDTH):
            X_PIXEL += PIXEL_WIDTH
            text_display(
                output[k], X_PIXEL - PIXEL_WIDTH // 2, Y_PIXEL - PIXEL_HEIGHT // 2
            )
            k += 1
        X_PIXEL = 0
    Y_PIXEL = 0
    k = 0

    A += 0.15 / 2
    B += 0.035 / 2

    if not PAUSED:
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
            if event.key == pygame.K_SPACE:
                PAUSED = not PAUSED
