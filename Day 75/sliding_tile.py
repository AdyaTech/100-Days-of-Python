import random

# Define puzzle size
SIZE = 3  # 3x3 grid

def create_puzzle():
    """Generate a solvable shuffled puzzle."""
    numbers = list(range(1, SIZE*SIZE)) + [0]  # Last tile is empty (0)
    random.shuffle(numbers)
    return [numbers[i*SIZE:(i+1)*SIZE] for i in range(SIZE)]

def display_puzzle(board):
    """Print the puzzle in a readable format."""
    for row in board:
        print(" ".join(str(num).rjust(2, " ") if num else "⬜" for num in row))
    print()

def find_empty(board):
    """Find the position of the empty tile (0)."""
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return r, c

def move_tile(board, direction):
    """Move a tile into the empty space (if possible)."""
    r, c = find_empty(board)
    moves = {"W": (r-1, c), "S": (r+1, c), "A": (r, c-1), "D": (r, c+1)}
    
    if direction in moves:
        nr, nc = moves[direction]
        if 0 <= nr < SIZE and 0 <= nc < SIZE:  # Check bounds
            board[r][c], board[nr][nc] = board[nr][nc], board[r][c]  # Swap

def is_solved(board):
    """Check if the puzzle is solved."""
    correct = list(range(1, SIZE*SIZE)) + [0]
    return sum(board, []) == correct

# Initialize and play
puzzle = create_puzzle()
while not is_solved(puzzle):
    display_puzzle(puzzle)
    move = input("Move (WASD): ").upper()
    move_tile(puzzle, move)

print("🎉 You solved the puzzle! 🎉")
