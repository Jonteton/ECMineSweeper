import pygame
import sys
from cell import Cell
from calcs import measure_distance

pygame.init()

SCREEN_MIN_SIZE = 750  # Can be made to autoadjust after % of ur screen
amount_of_cells = 16  # The amount of cells is equal in rows and columns, 16x16
bomb_chance = 0.25

CELL_SIZE = SCREEN_MIN_SIZE // amount_of_cells
READJUSTED_SIZE = CELL_SIZE * amount_of_cells


SCREEN_WIDTH, SCREEN_HEIGHT = READJUSTED_SIZE, READJUSTED_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MineSweeper")
CELL_WIDTH = CELL_HEIGHT = CELL_SIZE

cells = []
font = pygame.font.Font("freesansbold.ttf", 32)


def create_cells():
    x_pos = y_pos = 0
    for a_row in range(amount_of_cells):
        row = []
        for a_column in range(amount_of_cells):
            cell = Cell(x_pos, y_pos, CELL_WIDTH, CELL_HEIGHT, bomb_chance)
            x_pos += CELL_WIDTH
            row.append(cell)
        x_pos = 0
        y_pos += CELL_HEIGHT
        cells.append(row)


def find_nearest_cell(mouse_x, mouse_y):
    for row_index, row in enumerate(cells):
        for column_index, cell in enumerate(row):
            cell_center_x = cell.cell_center[0]
            cell_center_y = cell.cell_center[1]
            distance = measure_distance(mouse_x, mouse_y, cell_center_x, cell_center_y)

            if distance < cell.width // 2:
                print(f"The mouse is within this cell, x:{cell.x} y:{cell.y}")
                return cell, row_index, column_index

    return None, None, None


def find_neighbouring_bombs():
    for row_index, row in enumerate(cells):
        for column_index, cell in enumerate(row):
            calc_neighbouring_bombs(cell, row_index, column_index)


def calc_neighbouring_bombs(currently_selected_cell, row_index, column_index):
    # Identify number of neighbouring bombs
    neighboring_cells = []

    # Below represents all possibilities for how a neighbour can be positioned relative in index
    neighbor_offsets = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    for offset_row, offset_col in neighbor_offsets:
        neighbor_row, neighbor_col = row_index + offset_row, column_index + offset_col

        if 0 <= neighbor_row < len(cells) and 0 <= neighbor_col < len(cells[0]):
            neighbor_cell = cells[neighbor_row][neighbor_col]
            neighboring_cells.append(neighbor_cell)

    for cell in neighboring_cells:
        if cell.bomb:
            currently_selected_cell.neighbouring_bombs += 1


def event_handler(event):
    if event.type == pygame.QUIT:
        terminate_program()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # i.e left mouse clicked:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pressed_cell, row_index, column_index = find_nearest_cell(mouse_x, mouse_y)
            if pressed_cell:
                pressed_cell.selected = True
                if pressed_cell.bomb:
                    print("Cell contains a bomb, game over")


def draw_cells():
    for row in cells:
        for cell in row:
            cell.draw(screen, font)
            # cell.dummy_draw(screen) #use this method if you want to draw dummy circles to visualize the middle


def terminate_program():
    pygame.quit()
    sys.exit()


def run_setup():
    create_cells()
    find_neighbouring_bombs()


def draw():
    draw_cells()


def main():
    run_setup()

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            event_handler(event)

        draw()
        pygame.display.update()

    terminate_program()


if __name__ == "__main__":
    main()
