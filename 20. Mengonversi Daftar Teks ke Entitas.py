import html.entities

texts = ["Hello <World>", "This is &copy; 2023!", "Use &lt; for less than"]
entities_converted = [escape_html(text) for text in texts]
print("Entities Converted:", entities_converted)
# Fungsi: Konversi daftar teks biasa ke entitas HTML.
# Kondisi: Ketika Anda perlu mengkonversi banyak teks sekaligus untuk keamanan di HTML.