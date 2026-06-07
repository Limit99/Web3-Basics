import urllib.request
import json

# ============================================
# BACA DATA DARI BLOCKCHAIN
# ============================================
# File ini mengajarkan:
# - Cara membaca data publik dari blockchain
# - Apa itu block explorer
# - Bagaimana melihat transaksi di blockchain
# ============================================

def cek_harga_eth():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd,idr"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data["ethereum"]

def simulasi_block_explorer():
    """Simulasi data seperti di Etherscan"""
    blocks = [
        {
            "nomor": 19000001,
            "waktu": "2024-01-01 00:00:01",
            "transaksi": 187,
            "miner": "0xea674fdde714fd979de3edf0f56aa9716b898ec8",
            "reward": "0.0523 ETH"
        },
        {
            "nomor": 19000002,
            "waktu": "2024-01-01 00:00:13",
            "transaksi": 203,
            "miner": "0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97",
            "reward": "0.0489 ETH"
        },
        {
            "nomor": 19000003,
            "waktu": "2024-01-01 00:00:25",
            "transaksi": 165,
            "miner": "0x388c818ca8b9251b393131c08a736a67ccb19297",
            "reward": "0.0612 ETH"
        }
    ]
    return blocks

# ============================================
# SIMULASI
# ============================================

print("=" * 55)
print("  🔍 SIMULASI BLOCK EXPLORER")
print("=" * 55)

print("\n📊 Harga ETH saat ini:")
try:
    harga = cek_harga_eth()
    print(f"   USD : ${harga['usd']:,}")
    print(f"   IDR : Rp{harga['idr']:,}")
except:
    print("   ⚠️ Tidak bisa ambil harga (cek koneksi internet)")

print("\n📦 Block terbaru di Ethereum:")
print("-" * 55)

blocks = simulasi_block_explorer()
for block in blocks:
    print(f"\n🔷 Block #{block['nomor']}")
    print(f"   ⏰ Waktu      : {block['waktu']}")
    print(f"   📝 Transaksi  : {block['transaksi']} tx")
    print(f"   ⛏️  Miner      : {block['miner'][:20]}...")
    print(f"   💰 Reward     : {block['reward']}")

print("\n💡 Kamu bisa lihat data ini secara REAL di:")
print("   🌐 https://etherscan.io")
print("   🌐 https://bscscan.com")
print("   🌐 https://solscan.io")
