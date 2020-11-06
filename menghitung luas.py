import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Membuat fungsi utk menentukan layout window
# Memecah fungsi menjadi beberapa bagian, TopLayout merupakan fungsi untuk tampilan bagian atas

def topLayout(window):
    # Membuat Judul Dibagian Atas
    label = QLabel("Aplikasi Menghitung Luas Bangun Datar")
    # Mensetting Align nya agar berada Ditengah
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("Font: Bold; color:#8B0000; font-size:20pt")
    # Membuat Vertical Layout Dan Menambahkan Widget Nya
    layout1 = QVBoxLayout()
    layout1.addWidget(label)
    # Mereturn/mengembalikan nilai layout nya karena kita butuh layoutnya untuk ditambahkan ke gridLayout nya
    return layout1

def hitungJajarGenjang(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Menghitung Luas Jajar Genjang",window)
    # Membuat Widget Label
    labelRusuk = QLabel("Panjang Alas: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global rusuk
    labelTall = QLabel("Panjang Tinggi: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global tall
    # Membuat Widget Inputan
    rusuk = QLineEdit()
    tall = QLineEdit()
    # Membuat Button/ tombol
    btn = QPushButton("Hitung")
    # Mengirim Data Saat kita Mengklik button nya
    btn.clicked.connect(jajargenjang)
    # Membuat Form Layout Dan Menambahkan widget
    layout = QVBoxLayout()
    layout1 = QGridLayout()
    layout1.addWidget(labelRusuk)
    layout1.addWidget(rusuk)
    layout2 = QGridLayout()
    layout2.addWidget(labelTall)
    layout2.addWidget(tall)
    layout.addLayout(layout1)
    layout.addLayout(layout2)
    layout.addWidget(btn)
    groupbox.setLayout(layout)
    return groupbox

def jajargenjang():
    try:
        vRusuk = rusuk.text()
        vTall = tall.text()
        hKubus = int(vRusuk) * int(vTall)
        hasilKubus.setText(str(hKubus))
        rusuk.setText("")
        tall.setText("")
    except ValueError:
        pass
    
def hitungLayang(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Menghitung Luas Layang-layang", window)
    # Membuat Widget Label
    labelPanjang = QLabel("Panjang d1: ")
    labelLebar = QLabel("Panjang d2: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global d1, d2
    # Membuat Widget Inputan
    d1 = QLineEdit()
    d2 = QLineEdit()
    # Membuat Button/ tombol
    btn = QPushButton("Hitung")
    # Mengirim Data Saat kita Mengklik button nya
    btn.clicked.connect(layang)
    # Membuat Form Layout Dan Menambahkan widget
    layout1 = QGridLayout()
    layout1.addWidget(labelPanjang,0,0)
    layout1.addWidget(d1,0,1)
    layout1.addWidget(labelLebar,1,0)
    layout1.addWidget(d2,1,1)
    layout1.addWidget(btn,3,0,1,0)
    groupbox.setLayout(layout1)
    return groupbox

def layang():
    try:
        vPanjang = d1.text()
        vLebar = d2.text()
        hLayang = (int(vPanjang) * int(vLebar))/2
        hasilLayang.setText(str(hLayang))
        d1.setText("")
        d2.setText("")
    except ValueError:
        pass
    
def Tampil(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Hasil Operasi", window)
    # Membuat Widget Label
    labelKubus = QLabel("Luas Jajar Genjang: ")
    labelLayang = QLabel("Luas Layang-layang: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global hasilKubus,hasilLayang
    # Membuat Widget Inputan
    hasilKubus = QLineEdit()
    hasilKubus.setReadOnly(True)
    hasilLayang = QLineEdit()
    hasilLayang.setReadOnly(True)
    # Membuat Form Layout Dan Menambahkan widget
    layout1 = QFormLayout()
    layout1.addRow(labelKubus,hasilKubus)
    layout1.addRow(labelLayang,hasilLayang)
    groupbox.setLayout(layout1)
    return groupbox

def window_go():
    #inisialisasi pyqt
    app = QApplication(sys.argv)
    window = QWidget()
    # Menginisiasi GridLayout
    GLayout = QGridLayout()
    # Menambahkan Widget GroupBox Ke gridLayout
    GLayout.addLayout(topLayout(window),0,0,1 ,2)
    GLayout.addWidget(hitungJajarGenjang(window), 2, 0,1,0)
    GLayout.addWidget(hitungLayang(window), 3, 0,1,0)
    GLayout.addWidget(Tampil(window), 4, 0,1,0)
    # Menset agar jarak tidak terlalu renggang
    GLayout.setRowStretch(2,1)
    GLayout.setRowStretch(3,1)
    # Menset Layout Utama Ke GridLayout
    window.setLayout(GLayout)
    # Mensetting Ukuran Aplikasinya dan merubah warna background
    window.setGeometry(100,100,500,500)
    window.setStyleSheet("background-color:#FF7F50;")
    # Menset Judul Aplikasi
    window.setWindowTitle("Menghitung Bangun Datar")
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    window_go()
