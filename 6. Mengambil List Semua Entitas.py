import html.entities

entities_list = list(html.entities.name2codepoint.keys())
print("Daftar entitas yang tersedia:", entities_list)  # Menampilkan daftar entitas
# Fungsi: Mengambil semua entitas sebagai list.
# Kondisi: Ketika Anda memerlukan akses cepat ke semua entitas untuk pemrosesan.