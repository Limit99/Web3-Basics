```python
# ============================================
# PENGENALAN WEB3
# ============================================
# File ini mengajarkan:
# - Apa itu Web3
# - Perbedaan Web1, Web2, dan Web3
# - Kenapa Web3 penting untuk masa depan
# ============================================

web_evolution = {
    "Web1 (1990-2000)": {
        "deskripsi": "Internet hanya bisa dibaca",
        "contoh": ["Website statis", "Berita online"],
        "kontrol": "Perusahaan"
    },
    "Web2 (2000-sekarang)": {
        "deskripsi": "Internet bisa dibaca & ditulis",
        "contoh": ["Facebook", "Twitter", "YouTube"],
        "kontrol": "Perusahaan besar (Google, Meta)"
    },
    "Web3 (masa depan)": {
        "deskripsi": "Internet bisa dibaca, ditulis & dimiliki",
        "contoh": ["DeFi", "NFT", "DAO", "Metaverse"],
        "kontrol": "Pengguna sendiri!"
    }
}

print("🌐 Evolusi Internet: Web1 → Web2 → Web3\n")
print("=" * 50)

for era, info in web_evolution.items():
    print(f"\n📌 {era}")
    print(f"   Deskripsi : {info['deskripsi']}")
    print(f"   Contoh    : {', '.join(info['contoh'])}")
    print(f"   Kontrol   : {info['kontrol']}")
    print("-" * 50)

print("\n💡 Kesimpulan:")
print("Web3 = Internet yang DIKENDALIKAN oleh penggunanya")
print("Tidak ada perusahaan yang bisa sensor atau hapus datamu!")
print("\n🔑 Komponen utama Web3:")
komponen = [
    "Blockchain - Penyimpanan data terdesentralisasi",
    "Smart Contract - Program yang berjalan otomatis",
    "Wallet - Identitas digital kamu di Web3",
    "Token/NFT - Aset digital yang kamu miliki sendiri"
]
for k in komponen:
    print(f"  ✅ {k}")
