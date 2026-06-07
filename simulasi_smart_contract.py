# ============================================
# SIMULASI SMART CONTRACT
# ============================================
# File ini mengajarkan:
# - Apa itu Smart Contract
# - Bagaimana Smart Contract bekerja
# - Contoh Smart Contract sederhana
# ============================================

class SmartContract:
    """Simulasi Smart Contract sederhana"""
    
    def __init__(self, nama, pemilik):
        self.nama = nama
        self.pemilik = pemilik
        self.saldo = {}
        self.aktif = True
        print(f"📜 Smart Contract '{nama}' dibuat!")
        print(f"👤 Pemilik: {pemilik}\n")

    def deposit(self, pengguna, jumlah):
        if not self.aktif:
            print("❌ Contract tidak aktif!")
            return
        if pengguna not in self.saldo:
            self.saldo[pengguna] = 0
        self.saldo[pengguna] += jumlah
        print(f"✅ {pengguna} deposit {jumlah} ETH")
        print(f"   Saldo baru: {self.saldo[pengguna]} ETH")

    def transfer(self, pengirim, penerima, jumlah):
        if not self.aktif:
            print("❌ Contract tidak aktif!")
            return
        if pengirim not in self.saldo:
            print(f"❌ {pengirim} tidak punya saldo!")
            return
        if self.saldo[pengirim] < jumlah:
            print(f"❌ Saldo {pengirim} tidak cukup!")
            return
        if penerima not in self.saldo:
            self.saldo[penerima] = 0
        self.saldo[pengirim] -= jumlah
        self.saldo[penerima] += jumlah
        print(f"✅ Transfer berhasil!")
        print(f"   {pengirim} → {penerima}: {jumlah} ETH")

    def cek_saldo(self, pengguna):
        saldo = self.saldo.get(pengguna, 0)
        print(f"💰 Saldo {pengguna}: {saldo} ETH")

    def tampilkan_semua(self):
        print("\n📊 Semua Saldo:")
        print("-" * 30)
        for pengguna, saldo in self.saldo.items():
            print(f"   {pengguna}: {saldo} ETH")

# ============================================
# SIMULASI
# ============================================

print("=" * 50)
print("  📜 SIMULASI SMART CONTRACT")
print("=" * 50)

# Buat smart contract
contract = SmartContract("TokenTransfer", "Jalaluddin")

# Simulasi transaksi
print("📥 Deposit:")
contract.deposit("Budi", 5)
contract.deposit("Ani", 3)
contract.deposit("Cici", 2)

print("\n💸 Transfer:")
contract.transfer("Budi", "Ani", 2)
contract.transfer("Ani", "Cici", 1)
contract.transfer("Budi", "Dodi", 10)  # Gagal - saldo kurang

print("\n📊 Cek Saldo Akhir:")
contract.tampilkan_semua()

print("\n💡 Kesimpulan:")
print("✅ Smart Contract berjalan OTOMATIS")
print("✅ Tidak butuh perantara/pihak ketiga")
print("✅ Aturan tidak bisa dimanipulasi")
print("✅ Transparan & bisa dilihat semua orang")
