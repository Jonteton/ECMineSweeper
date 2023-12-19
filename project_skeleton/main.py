import pygame
import sys
from cell import Cell
from calcs import measure_distance

""" This is the main file you work on for the project"""

pygame.init()

SCREEN_MIN_SIZE = 750  # Can be made to autoadjust after % of ur screen
amount_of_cells = 16  # The amount of cells is equal in rows and columns, 16x16 (LOCKED)
bomb_chance = 0.25  # Change to prefered value or use default 0.25

CELL_SIZE = SCREEN_MIN_SIZE // amount_of_cells  # how large can each cell be?
READJUSTED_SIZE = CELL_SIZE * amount_of_cells
CELL_WIDTH = CELL_HEIGHT = CELL_SIZE  # Probably not needed, just use cell_size

SCREEN_WIDTH, SCREEN_HEIGHT = READJUSTED_SIZE, READJUSTED_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("MineSweeper")

cells = []


def create_cells():
    """This function is meant to initialy generate all the cells and create the boundaries"""
    # This is a good base to go from (think about it thoroughly before you code!! We want to create 16x16 list with each object being a cell):
    # for a_row in range(amount_of_cells):
    #     row = []
    #     for a_column in range(amount_of_cells):
    #         pass
    # We want to create 16x16 new cells and place into a 2d list
    my_cell = Cell(0, 0, CELL_WIDTH, CELL_HEIGHT, bomb_chance)
    cells.append(my_cell)


def draw_cells():
    """In this function we want to draw each cell, i.e call upon each cells .draw() method!"""
    # Hint: take inspiration from the forloop in create_cells to loop over all the cells
    for my_cell in cells:
        print("nu är vi draw_cells funktionen!")
        my_cell.draw(screen)


def draw_test_distance():
    x1, y1 = 40, 40
    x2, y2 = 70, 70
    pygame.draw.circle(screen, "red", (x1, y1), 5)
    pygame.draw.circle(screen, "red", (x2, y2), 5)

    distance_between = measure_distance(x1, y1, x2, y2)
    print(distance_between)


def draw():
    """This function handles all the drawings to the screen, such as drawing rectangles, objects etc"""
    # draw_cells()
    draw_test_distance()


def event_handler(event):
    """This function handles all events in the program"""
    if event.type == pygame.QUIT:
        terminate_program()


def run_setup():
    """This function is meant to run all code that is neccesary to setup the app, happends only once"""
    create_cells()


def terminate_program():
    """Functionality to call on whenever you want to terminate the program"""
    pygame.quit()
    sys.exit()


def main():
    run_setup()

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            event_handler(event)

        draw()
        pygame.display.flip()

    terminate_program()


if __name__ == "__main__":
    main()
