import html.entities

codepoints_list = list(html.entities.name2codepoint.values())
print("Daftar semua kode point:", codepoints_list)  # Menampilkan semua kode point
# Fungsi: Mengambil semua kode point entitas HTML.
# Kondisi: Ketika Anda membutuhkan akses ke semua nilai Unicode yang mungkin ada.