class KendaraanDarat:
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        self.TahunKeluaran = tahun_keluaran
        self.Nama = nama
        self.Warna = warna
        self.Kecepatan = kecepatan
        self.BahanBakar = bahan_bakar
        self.JumlahRoda = jumlah_roda
        self.KapasitasPenumpang = kapasitas_penumpang

    def startEngine(self):
        print("Mesin dinyalakan.")

    def stopEngine(self):
        print("Mesin dimatikan.")

    def Maju(self):
        print("Bergerak maju.")

    def Mundur(self):
        print("Bergerak mundur.")

    def Belok(self):
        print("Belok.")

class Kereta(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, gerbong, jumlah_kursi, jenis_layanan_kereta, rute):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.Gerbong = gerbong
        self.JumlahKursi = jumlah_kursi
        self.JenisLayananKereta = jenis_layanan_kereta
        self.Rute = rute

    def tambahRute(self, new_rute):
        self.Rute.append(new_rute)
        print(f"Rute baru {new_rute} ditambahkan.")

    def kurangiRute(self, old_rute):
        if old_rute in self.Rute:
            self.Rute.remove(old_rute)
            print(f"Rute {old_rute} dihapus.")
        else:
            print(f"Rute {old_rute} tidak ditemukan.")

class Mobil(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.JenisMobil = jenis_mobil

    def startEngine(self):
        print("Mesin mobil dinyalakan.")

    def stopEngine(self):
        print("Mesin mobil dimatikan.")

    def Maju(self):
        print("Mobil bergerak maju.")

    def Mundur(self):
        print("Mobil bergerak mundur.")

    def Belok(self):
        print("Mobil belok.")

class MobilBalap(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil, front_wing, rear_wing):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil)
        self.FrontWing = front_wing
        self.RearWing = rear_wing

    def race(self):
        print("Mobil balap sedang balapan.")

class MobilCrossroad(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil, sunroof_type, shock_breaker):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil)
        self.SunroofType = sunroof_type
        self.ShockBreaker = shock_breaker

    def sunroofTerbuka(self):
        print("Sunroof terbuka.")

    def sunroofTertutup(self):
        print("Sunroof tertutup.")