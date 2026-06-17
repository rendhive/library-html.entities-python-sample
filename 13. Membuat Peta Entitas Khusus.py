import html.entities

custom_entities = {'my_entity': 12345}
print("Add Custom Entity:", html.entities.codepoint2name[custom_entities['my_entity']] if custom_entities.get('my_entity') else "Entity not found")
# Fungsi: Menambahkan atau mengubah entitas khusus.
# Kondisi: Ketika Anda perlu menambahkannya dalam konteks tertentu.