import html.entities

custom_entities = {'example': 32000}
print("Custom Entities:")
for name, code in custom_entities.items():
    print(f"&{name}; -> {code}")
# Fungsi: Mencetak entitas kustom yang dibuat secara manual.
# Kondisi: Ketika Anda memerlukan entitas khusus untuk aplikasi Anda.