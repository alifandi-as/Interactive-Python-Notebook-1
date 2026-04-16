class HP:
    def __init__(self, merek, model, harga, status):
        self.merek = merek
        self.model = model
        self.harga = harga
        self.status = status

    def tampilkan_info(self):
        print(f"HP {self.merek} model {self.model} dengan harga Rp {self.harga} dan status {self.status}")

    def beli(self):
        if self.status == "Tersedia":
            self.status = "Dibeli"
            print(f"Buku '{self.merek} {self.model}' sudah dibeli.")
        else:
            print(f"Buku '{self.merek} {self.model}' telah laku..")

    def kembalikan(self):
        if self.status == "Dibeli":
            self.status = "Tersedia"
            print(f"Buku '{self.merek} {self.model}' telah dikembalikan.")
        else:
            print(f"Buku '{self.merek} {self.model}' tidak dapat dikembalikan karena masih tersedia.")