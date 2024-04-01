import board

print("Program started.")

print("Initialize the board.")
b = board.Board()
b.width = 3
b.height = 3

print("Build the board.")
b.build()

print("Board information:")
print(f"width: {b.width}, height: {b.height}")
print("blocks count:", b.blocks_count())

print("Program ended.")