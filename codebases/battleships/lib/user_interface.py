class UserInterface:
    def __init__(self, io, game):
        self.io = io
        self.game = game

    def run(self):
        self._show("Welcome to the game!")
        self._show("Set up your ships first.")
        while self._ships_unplaced_message():
            self._show("You have these ships remaining: {}".format(
                self._ships_unplaced_message()))
            self._prompt_for_ship_placement()
            self._show("This is your board now:")
            self._show(self._format_board())

        self._show("Starting game...")
        self._show(self._format_game_board())
        while not self.game.is_over():
            self._prompt_for_shot()
            self._show(self._format_game_board())

        self._show("You win! All ships destroyed.")


    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    def _ships_unplaced_message(self):
        ship_lengths = [str(ship.length) for ship in self.game.unplaced_ships]
        return ", ".join(ship_lengths)

    def _prompt_for_ship_placement(self):
        ship_length = self._prompt("Which do you wish to place?")
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        ship_row = self._prompt("Which row?")
        ship_col = self._prompt("Which column?")
        correct_placement = self._check_ship_placement(
            length=int(ship_length),
            orientation=ship_orientation,
            row=int(ship_row),
            col=int(ship_col),
        )
        if correct_placement:
            self._show("OK.")
            self.game.place_ship(
                length=int(ship_length),
                orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
                row=int(ship_row),
                col=int(ship_col),
            )

    def _check_ship_placement(self, length, orientation, row, col):
        if length not in [ship.length for ship in self.game.unplaced_ships]:
            self._show("Incorrect ship length")
            return False
        if orientation not in 'vh':
            self._show("Incorrect orientation: must be v or h")
            return False
        if row < 1 or row > self.game.rows:
            self._show(f"Incorrect row: must be more than 1 and less than or equal to {self.game.rows}")
            return False
        if col < 1 or col > self.game.cols:
            self._show(f"Incorrect column: must be more than 1 and less than or equal to {self.game.cols}")
            return False
        if orientation == 'v' and row + length - 1 > self.game.rows:
            self._show(f"Ship can't be placed off the board")
            return False
        if orientation == 'h' and col + length - 1 > self.game.cols:
            self._show(f"Ship can't be placed off the board")
            return False
        
        if orientation == 'v':
            for i in range(row, row + length):
                if self.game.ship_at(i, col):
                    self._show(f"Ship can't be placed on top of another ship")
                    return False
        elif orientation == 'h':
            for i in range(col, col + length):
                if self.game.ship_at(row, i):
                    self._show(f"Ship can't be placed on top of another ship")
                    return False
        
        return True
            

    def _prompt_for_shot(self):
        self._show("Take your shot!")
        row = int(self._prompt("Which row?"))
        col = int(self._prompt("Which column?"))
        if self.game.shot_already(row, col):
            self._show("You have already shot there, try again.")
            return 
        
        if not self.game.valid_shot(row, col):
            self._show("You must shoot within the game board")
            return
        
        if self.game.ship_at(row, col):
            self._show("HIT!\n")
            ship_hit = self.game.find_hit_ship(row, col)
            hit_or_miss = True
            self.game.add_shot(row, col, hit_or_miss)
            if self.game.ship_sunk(ship_hit):
                self._show("You sunk a battleship!")
        else:
            self._show("MISS!\n")
            hit_or_miss = False
            self.game.add_shot(row, col, hit_or_miss)

        
        

    def _format_board(self):
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.ship_at(row, col):
                    row_cells.append(" S ")
                else:
                    row_cells.append(" . ")
            rows.append("".join(row_cells))
        return "\n".join(rows)
    

    def _format_game_board(self):
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.shot_hit(row, col):
                    row_cells.append(" X ")
                elif self.game.shot_miss(row, col):
                    row_cells.append(" O ")
                else:
                    row_cells.append(" . ")
            rows.append("".join(row_cells))
        return "\n".join(rows)
