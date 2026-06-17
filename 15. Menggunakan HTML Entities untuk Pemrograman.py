import html.entities

def escape_html(text):
    for name, code in html.entities.name2codepoint.items():
        text = text.replace(name, f"&{name};")
    return text

escaped = escape_html("This text has <tag> and & special characters.")
print("Escaped Text:", escaped)  # Menggunakan entitas untuk pemrograman
# Fungsi: Mengonversi semua karakter khusus ke entitas HTML.
# Kondisi: Ketika Anda ingin memastikan teks aman untuk digunakan dalam HTML.