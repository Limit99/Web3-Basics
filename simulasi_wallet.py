import hashlib
import os

# ============================================
# SIMULASI KONEKSI WALLET
# ============================================
# File ini mengajarkan:
# - Bagaimana wallet terhubung ke aplikasi Web3
# - Apa itu signature (tanda tangan digital)
# - Bagaimana dApp memverifikasi identitasmu
# ============================================

class Web3Wallet:
    def __init__(self, nama):
        self.nama = nama
        self.private_key = os.urandom(32).hex()
        self.public_key = hashlib.sha256(
            self.private_key.encode()).hexdigest()
        self.alamat = "0x" + self.public_key[:40]
        self.terhubung = False

    def connect(self, dapp_nama):
        print(f"\n🔌 Menghubungkan wallet ke {dapp_nama}...")
        print(f"📱 Wallet    : {self.nama}")
        print(f"🔵 Alamat    : {self.alamat}")
        print(f"\n⚠️  {dapp_nama} meminta izin:")
        print("   ✅ Lihat alamat wallet")
        print("   ✅ Minta tanda tangan transaksi")
        print("   ❌ Tidak bisa akses private key")
        self.terhubung = True
        print(f"\n✅ Wallet berhasil terhubung ke {dapp_nama}!")

    def sign_transaksi(self, pesan):
        if not self.terhubung:
            print("❌ Wallet belum terhubung!")
            return
        tanda_tangan = hashlib.sha256(
            (pesan + self.private_key).encode()).hexdigest()
        print(f"\n✍️  Menandatangani transaksi...")
        print(f"📝 Pesan         : {pesan}")
        print(f"🔏 Tanda tangan  : {tanda_tangan[:30]}...")
        print(f"✅ Transaksi berhasil ditandatangani!")
        return tanda_tangan

    def disconnect(self, dapp_nama):
        self.terhubung = False
        print(f"\n🔌 Wallet berhasil disconnect dari {dapp_nama}!")

# ============================================
# SIMULASI
# ============================================

print("=" * 50)
print("  💼 SIMULASI KONEKSI WALLET WEB3")
print("=" * 50)

wallet = Web3Wallet("Jalaluddin")
wallet.connect("Uniswap")
wallet.sign_transaksi("Tukar 1 ETH dengan 2000 USDT")
wallet.disconnect("Uniswap")
