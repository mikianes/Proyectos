class Zelda:
    def __init__(self, rows):
        self.rows = rows
        self.lenght_row = 2 * rows

    def print_triangles(self):
        for n in range(1, self.rows + 1):
            line = '*' * (2 * n - 1)
            line = line.center(self.lenght_row * 2)
            print(line)

        for n in range(1, self.rows + 1):
            line = '*' * (2 * n - 1)
            line = line.center(self.lenght_row) + line.center(self.lenght_row)
            print(line)

if __name__ == "__main__":
    zelda = Zelda(int(input("Número de filas: ")))
    zelda.print_triangles()  