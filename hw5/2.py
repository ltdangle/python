# 2. Make a solution for Wheat and chessboard problem. Represent a solution in tons. Assume that one grain of wheat weights 0.065 gram
grains = 1
squares = 1
while squares <= 64:
    grains = grains * 2
    squares = squares + 1

weight = round(grains * 0.065)

print(f"squares: {squares}, grains: {grains}, weight: {weight} tons")
