
def bitmap(width. height, val):
    for y in len(height):
        row = []
        for _ in len(width):
            row.append(val)
        yield row