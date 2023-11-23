from lib.ship import Ship
from lib.ship_placement import ShipPlacement
from lib.shot import Shot


class Game:
    def __init__(self, rows=10, cols=10):
        self.ships_placed = []
        self.rows = rows
        self.cols = cols
        # self.unplaced_ships = [
        #     Ship(2),
        #     Ship(3),
        # ]
        self.unplaced_ships = [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5)
            ]
        self.shots = []
        self.over = False


    def place_ship(self, length, orientation, row, col):
        ship_placement = ShipPlacement(
            length=length,
            orientation=orientation,
            row=row,
            col=col,
        )
        self.ships_placed.append(ship_placement)

        # Remove ship from unplaced ships
        for i, ship in enumerate(self.unplaced_ships):
            if ship.length == length:
                index_to_pop = i
                break
        self.unplaced_ships.pop(i)

    def add_shot(self, row, col, is_hit):
        shot = Shot(row, col, is_hit)
        self.shots.append(shot)

    def shot_miss(self, row, col):
        for shot in self.shots:
            if shot.row == row and shot.col == col and not shot.is_hit:
                return True
        return False

    def shot_hit(self, row, col):
        for shot in self.shots:
            if shot.row == row and shot.col == col and shot.is_hit:
                return True
        return False
            
    def shot_already(self, row, col):
        for shot in self.shots:
            if shot.row == row and shot.col == col:
                return True
        return False
    
    def valid_shot(self, row, col):
        if row > 0 and row <= self.rows and col > 0 and col <= self.cols:
            return True
        return False

    def ship_at(self, row, col):
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False
    
    def shot_at(self, row, col):
        for shot in self.shots:
            if shot.row == row and shot.col == col:
                return True
        return False

    def find_hit_ship(self, row, col):
        for ship in self.ships_placed:
            if ship.covers(row, col):
                return ship

    def ship_sunk(self, ship):
        if ship.orientation == "vertical":
            for i in range(ship.row, ship.row + ship.length):
                if not self.shot_at(i, ship.col):
                    return False
        else:
            for i in range(ship.col, ship.col + ship.length):
                if not self.shot_at(ship.row, i):
                    return False
                
        ship.sunk = True
        return True


    def is_over(self):
        for ship in self.ships_placed:
            if not ship.sunk:
                return False
        return True

