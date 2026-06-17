import html.entities

entity = "&nbsp;"
codepoint = html.entities.name2codepoint.get('nbsp')
print(f"Kode point untuk {entity}: {codepoint}")  # Kode untuk non-breaking space
# Fungsi: Mengambil kode point untuk sebuah entitas spesifik.
# Kondisi: Ketika Anda perlu mendapatkan nilai Unicode untuk entitas tertentu.