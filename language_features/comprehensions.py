sudoku = [
	[8,2,7,1,5,4,3,9,6],
	[9,6,5,3,2,7,1,4,8],
	[3,4,1,6,8,9,7,5,2],
	[5,9,3,4,6,8,2,7,1],
	[4,7,2,5,1,3,6,8,9],
	[6,1,8,9,7,2,4,3,5],
	[7,8,6,2,3,5,9,1,4],
	[1,5,4,7,9,6,8,2,3],
	[2,3,9,8,4,1,5,6,7]]


def eval_array(row: list) -> bool:
	"""Check if a list contains exactly one and only one of each number from 1 to 9"""
	return sorted(row) == list(range(1,10))

def construct_block(matrix: list, i: int, j: int) -> list:
	"""Generate a list with the elements inside the 3x3 block that starts at (i,j) from a given 9x9 matrix"""
	return (matrix[i][j:j+3])+(matrix[i+1][j:j+3])+(matrix[i+2][j:j+3])


if __name__ == '__main__':
	"""Apply eval_array to each row in the sudoku"""
	eval_rows = [eval_array(row) for row in sudoku]
	print("Validate rows: ", eval_rows)

	"""Apply a construct_block to all 9 (i,j) combinations"""
	blocks = [construct_block(sudoku, i, j) for i in [0,3,6] for j in [0,3,6]]
	print("\nGenerate blocks: ", blocks)
	eval_blocks = [eval_array(row) for row in blocks]
	print("Validate blocks: ", eval_blocks)

	"""Generate a MATRIX where every row is a column of the original matrix"""
	columns = [[row[i] for row in sudoku] for i in range(9)]
	print("\nGenerate columns: ", columns)
	eval_columns = [eval_array(row) for row in columns]
	print("Validate columns: ", eval_columns)

	is_sudoku_complete = not (False in eval_rows or False in eval_columns or False in eval_blocks)
	print("\nIs Sudoku solved? ", is_sudoku_complete)