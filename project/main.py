import problem as sdku
from functools import partial
from analyze import timer
import genetic


board = sdku.add_spaces(sdku.first_example, 15)
print("Board with {} blank spaces".format(sdku.board_spaces(board)))
sdku.print_board(board)

with timer():
    population, generations = genetic.run_evolution(
        populate_func=partial(genetic.generate_population, size=50, genome_length=sdku.board_spaces(board)),
        fitness_func=partial(sdku.fitness, board=board.copy()),
        fitness_limit=0,
        generation_limit=500
    )

solution = population[0]
print("Solution: ", solution)

# Fill board with solution
solved = sdku.fill_board(solution, board)

# Print board solved
print("Solved board:")
sdku.print_board(solved)
print("Generation: ", generations)

# Contar los mstks en el board
mistakes = sdku.cnt_mistakes(solved)
print("Mistakes: " + str(mistakes))
