import html.entities

text = "Tom & Jerry &gt;"
converted_text = text.replace("&gt;", html.entities.codepoint2name[62])
print("Converted Text:", converted_text)
# Fungsi: Mengonversi teks yang berisi entitas HTML yang salah menjadi entitas yang benar.
# Kondisi: Ketika Anda sedang memperbaiki teks HTML yang telah di-scrap atau di-generate.