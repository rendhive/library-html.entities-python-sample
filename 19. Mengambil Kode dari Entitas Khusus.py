import html.entities

custom_entities = {'my_entity': 12345}
code = custom_entities.get('my_entity')
if code:
    print(f"Kode untuk entitas my_entity: {code}")
# Fungsi: Mengambil kode dari entitas khusus.
# Kondisi: Ketika Anda ingin melakukan validasi atau pengambilan langsung dari entitas kustom