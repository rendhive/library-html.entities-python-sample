import html.entities

text = "I love &lt;Python&gt; programming &amp; &copy; 2023."
converted_text = text.encode("ascii", "xmlcharrefreplace").decode()
print("Converted Text:", converted_text)  # Mengkonversi teks ke ASCII
# Fungsi: Mengonversi teks HTML ke format ASCII tampilan dengan entitas.
# Kondisi: Ketika Anda perlu menampilkan teks dalam format yang lebih umum.