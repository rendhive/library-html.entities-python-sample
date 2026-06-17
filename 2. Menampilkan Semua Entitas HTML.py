import html.entities

print("Daftar semua entitas HTML:")
for entity in html.entities.name2codepoint:
    print(f"&{entity}; -> {html.entities.name2codepoint[entity]}")
# Fungsi: Menampilkan semua entitas HTML yang tersedia.
# Kondisi: Ketika Anda ingin melihat entitas karakter yang bisa digunakan dalam HTML.