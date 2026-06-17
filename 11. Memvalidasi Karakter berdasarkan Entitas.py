import html.entities

def is_valid_entity(entity):
    return entity in html.entities.name2codepoint

print("Is &copy; valid?", is_valid_entity("&copy;"))  # Memeriksa apakah entitas valid
# Fungsi: Memeriksa kevalidan entitas HTML.
# Kondisi: Ketika Anda perlu memvalidasi entitas yang diterima.