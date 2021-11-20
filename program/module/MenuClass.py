import module.console as console
import module.init as Route
from module.SPLClass import SPL

# Object untuk mengelola navigasi menu.
# #
class Menu:
    # Constructor function.
    def __init__(self, use):
        # self.use = use
        self.selected_main_menu = 0
        self.selected_menu_1 = 0
        self.selected_menu_2 = 0

    # Kontrol menu utama.
    def main_menu(self):
        console.clear()
        print('>>> MENU UTAMA PROGRAM PERHITUNGAN MATRIKS <<<\n')
        print('Pilih opsi:')
        print('[1] Sistem Persamaan Linier (SPL)')
        print('[2] Matriks Hilbert')
        print('[3] Rangkaian Listrik')
        print('[4] Polinom Interpolasi')
        print('[99] Keluar')

        # self.selected_main_menu = input('Input opsi: ')
        self.selected_main_menu = '1'

        # Validasi input pilihan menu.
        if self.selected_main_menu == '99':
            # Keluar dari console program.
            console.out()

        elif self.selected_main_menu == '1':
            # Menggunakan SPLClass untuk menghitung SLP
            spl = SPL(True)
            spl.main()
            # Route.menu.menu_spl()
        else:
            console.selected_unknow()
            Route.menu.main_menu()

    # Kontrol menu pada sub-menu spl.
    def menu_spl(self):
        console.clear()
        print('SPL -> Metode Perhitungan:')
        print('[1] Eliminasi Gauss')
        print('[2] Eliminasi Gauss-Jordan')
        print('[99] Kembali ke Manu Utama')

        self.selected_menu_1 = input('Pilih Metode: ')
        # self.selected_menu_1 = '1'

        # Validasi input pilihan menu.
        if self.selected_menu_1 == '99':
            Route.menu.main_menu()
        elif self.selected_menu_1 == '1':
            Route.gauss.menu()
        else:
            console.selected_unknow()
            Route.menu.menu_spl()