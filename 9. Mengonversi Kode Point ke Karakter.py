import html.entities

codepoint = 169
char = chr(codepoint)
entity = html.entities.codepoint2name.get(codepoint)
print(f"Karakter untuk kode point {codepoint} adalah: {char} (Entitas: &{entity};)")
# Fungsi: Mengonversi kode point Unicode menjadi karakter yang sesuai.
# Kondisi: Ketika Anda ingin menampilkan karakter berdasarkan nilai Unicode.