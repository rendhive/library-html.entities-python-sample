import html.entities

text_with_entities = "Hello &copy; World &lt;3"
decoded_text = html.unescape(text_with_entities)
print("Decoded Text:", decoded_text)  # Mengonversi entitas ke karakter asli
# Fungsi: Mengonversi entitas HTML kembali ke karakter aslinya.
# Kondisi: Ketika Anda perlu mendapatkan teks asli yang berisi entitas.