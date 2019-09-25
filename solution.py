from collections import defaultdict

def get_ships_amount(field):
    ships_dots = defaultdict(lambda: defaultdict(lambda: None))

    def get_closest_ship(x, y):
        if ships_dots[x+1][y]:
            return ships_dots[x+1][y]
        if ships_dots[x-1][y]:
            return ships_dots[x-1][y]
        if ships_dots[x][y+1]:
            return ships_dots[x][y+1]
        if ships_dots[x][y-1]:
            return ships_dots[x][y-1]
        return x,y

    for x in range(len(field)):
        for y in range(len(field[x])):
            if field[x][y] == 0:
                continue
            shipX, shipY = get_closest_ship(x,y)
            ships_dots[x][y] = (shipX, shipY)

    ships = set()
    for (_, row) in ships_dots.items():
        for (_, point) in row.items():
            if point is not None and point not in ships:
                ships.add(point)

    return len(ships)


