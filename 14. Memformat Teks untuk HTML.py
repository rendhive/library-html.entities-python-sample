import html.entities

def format_text_to_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

formatted_text = format_text_to_html("Hello & World <Python>")
print("Formatted Text:", formatted_text)  # Memformat teks untuk HTML
# Fungsi: Mengonversi teks biasa menjadi format HTML yang aman.
# Kondisi: Ketika Anda ingin menyajikan konten pada halaman web.