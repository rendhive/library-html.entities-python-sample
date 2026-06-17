import html.entities

text = "Hello & &lt;world&gt;! &copy;"
for name, code in html.entities.name2codepoint.items():
    text = text.replace(f"&{name};", chr(code))

print("Converted Full Text:", text)
# Fungsi: Mengonversi semua entitas dalam teks.
# Kondisi: Ketika Anda ingin mengkonversi seluruh teks HTML dengan entitas terdaftar.