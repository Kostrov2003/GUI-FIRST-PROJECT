import pygame as pg
from game_config import *

pg.init()
clock = pg.time.Clock()


screen = pg.display.set_mode(WINDOW_SIZE)
screen.fill(BACKGROUND)

n_lines = pg.Surface((CELL_QTY * CELL_SIZE, CELL_SIZE // 2)).convert_alpha()
n_rows = pg.Surface((CELL_SIZE // 2, CELL_QTY * CELL_SIZE)).convert_alpha()
fields = pg.Surface((CELL_QTY * CELL_SIZE, CELL_QTY * CELL_SIZE)).convert_alpha()
board = pg.Surface((
    2 * n_rows.get_width() + fields.get_width(),
    2 * n_lines.get_height() + fields.get_height()
)).convert_alpha()

is_even_qty = (CELL_QTY % 2 == 0)
cell_color_index = 1 if (is_even_qty) else 0

for y in range(CELL_QTY):
    for x in range(CELL_QTY):
        #pg.draw.rect(screen, COLORS[cell_color_index], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        cell = pg.Surface((CELL_SIZE, CELL_SIZE)).convert_alpha()
        cell.fill(COLORS[cell_color_index])
        fields.blit(cell, (x * CELL_SIZE, y * CELL_SIZE))
        cell_color_index ^= True  # бинарное XOR
    cell_color_index = cell_color_index ^ True if (is_even_qty) else cell_color_index

for i in range(0, CELL_QTY):
    letter = FONT18.render(LTRS[i], 1, WHITE)
    number = FONT18.render(str(CELL_QTY - i), 1, WHITE)
    n_lines.blit(letter, (
        i * CELL_SIZE + (CELL_SIZE - letter.get_rect().width) // 2, #x
        (n_lines.get_height() - letter.get_rect().height) // 2 #y
        )
    )
    n_rows.blit(number, (
        (n_rows.get_width() - letter.get_rect().width) // 2, #x
        i * CELL_SIZE + (CELL_SIZE - number.get_rect().height) // 2, #y
        )
    )

board.blit(n_rows, (0, n_lines.get_height()))
board.blit(n_rows, (n_rows.get_width() + fields.get_width(), n_lines.get_height()))
board.blit(n_lines, (n_rows.get_width(), 0))
board.blit(n_lines, (n_rows.get_width(), n_rows.get_width() + fields.get_width()))
board.blit(fields, (n_rows.get_width(), n_lines.get_height()))
screen.blit(board, (
    (WINDOW_SIZE[0] - board.get_width()) // 2,
    (WINDOW_SIZE[1] - board.get_height()) // 2
    )
)

pg.display.update()

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    clock.tick(FPS)
