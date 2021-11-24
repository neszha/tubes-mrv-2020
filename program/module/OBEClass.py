import numpy as np
import module.console as console

# Class untuk menghanddle operasi OBE.
# #
class OBE:
    # Constructor method.
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_origin = matrix.copy()
        self.with_method = None
        self.solution_param = 0 # [-1: Solusi banyak, 0: Tidak ada solusi, 1: Solusi unik]
        self.solution = None

    # Mengambil hasil persamaan dari persamaan matriks argumented.
    def get_solution(self):
        self.validate_solution()
        if self.with_method == 'gauss': self.generate_solution_gauss()
        elif self.with_method == 'gauss_jordan': self.generate_solution_gauss_jordan()
        return self.solution

    # Melakukan eliminasi gauss pada matriks argumented.
    def gauss(self):
        self.with_method = 'gauss'
        [row, col] = self.matrix.shape
        size = min(row, col)

        for i in range(size):
            # Mencari nilai 1 untuk dilakukan pivoting ke atas.
            for j in range(i, size):
                elm = self.matrix[j][i]
                if elm == 1:
                    self.pivoting(j, i)
                    break

            # Mencari titik element 1 utama.
            elm_point = 1
            for j in range(i, col):
                elm = self.matrix[i][j]
                if elm != 0:
                    elm_point = elm;
                    break

            # Membuat element 1 utama.
            for j in range(i, col): self.matrix[i][j] /= elm_point

            # Membuat element di bawah 1 bernilai 0.
            for j in range(i + 1, size):
                ratio = self.matrix[j][i] / self.matrix[i][i]
                for k in range(size + 1):
                    self.matrix[j][k] -= ratio * self.matrix[i][k]

        return self.matrix

    # Melakukan eliminasi gauss jordan pada matriks argumented.
    def gauss_jordan(self):
        # Malakukan OBE gauss.
        self.gauss();

        # Melanjutkan menjadi gauss jordan.
        self.with_method = 'gauss_jordan'
        [row, col] = self.matrix.shape
        size = min(row, col)
        size = 3

        for i in range(size):
            # Membuat element di atas 1 bernilai 0.
            for j in range(size):
                if i != j:
                    ratio = self.matrix[j][i] / self.matrix[i][i]
                    for k in range(size+1):
                        self.matrix[j][k] -= ratio * self.matrix[i][k]

        return self.matrix

    # Melakukan pivoting atau pertukaran element kolom pada
    # matriks argumented.
    def pivoting(self, from_row, to_row):
        if from_row == to_row: return True
        temp_row = self.matrix[to_row].copy()
        self.matrix[to_row] = self.matrix[from_row]
        self.matrix[from_row] = temp_row

    # Mencari hasil persamaan dari pertihungan matriks argumented
    # dengan eliminasi gauss.
    def generate_solution_gauss(self):
        [row, col] = self.matrix.shape
        n = col-1;
        self.solution = np.zeros(col-1)
        self.solution[n-1] = self.matrix[n-1][n] / self.matrix[n-1][n-1]
        for i in range(n-2, -1, -1):
            self.solution[i] = self.matrix[i][n]
            for j in range(i+1, n):
                self.solution[i] -= self.matrix[i][j] * self.solution[j]
            self.solution[i] /= self.matrix[i][i]

    # Mencari hasil persamaan dari pertihungan matriks argumented
    # dengan eliminasi gauss jordan.
    def generate_solution_gauss_jordan(self):
        [row, col] = self.matrix.shape
        self.solution = np.zeros(col-1)
        for i in range(row):
            self.solution[i] = self.matrix[i][col-1]

    # Menantukan apakah hasil operasi OBE menghasilkan solusi
    # unik, banyak, ataupun tidak memiliki solusi.
    def validate_solution(self):
        [row, col] = self.matrix.shape
        elms_end = self.matrix[row-1]
        if elms_end[col-1] and elms_end[col-2]: self.solution_param = 1 # Solusi unik.
        elif elms_end[col-1] and not(elms_end[col-2]): self.solution_param = -1 # Solusi banyak.
        else: self.solution_param = 0 # Tidak ada solusi.

    # Menampilkan hasil persamaan.
    def show_result(self):
        console.clear()
        print('Persamaan dengan matriks argumented:')
        print(self.matrix_origin)

        self.get_solution()
        if self.solution_param == 1: result = 'Solusi unik.'
        elif self.solution_param == -1: result = 'Solusi banyak.'
        else: result = 'Tidak ada solusi.'

        print('\n=> Hasil: ' + result)

        if not(self.solution_param): return

        n = len(self.solution)
        for i in range(n):
            print('X[' + str(i+1) + '] = ' + str(self.solution[i]))
