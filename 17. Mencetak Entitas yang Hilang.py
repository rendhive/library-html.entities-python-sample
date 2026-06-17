import html.entities

def print_entity(name):
    if name in html.entities.name2codepoint:
        print(f"Entitas: {name} -> {html.entities.name2codepoint[name]}")
    else:
        print(f"Entitas '{name}' tidak ditemukan.")

print_entity("&gt;")  # Memeriksa entitas spesifik
# Fungsi: Mencetak informasi tentang entitas spesifik.
# Kondisi: Ketika Anda ingin mengecek satu entitas tertentu.