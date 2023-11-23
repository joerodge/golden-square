class Shot:
    def __init__(self, row, col, is_hit):
        self.row = row
        self.col = col
        self.is_hit = is_hit

    def __repr__(self):
        return f"Shot({self.row}, {self.col}, {'Hit' if self.is_hit else 'Miss'})"

