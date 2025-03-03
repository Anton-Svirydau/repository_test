import json
import base64
from timeit import default_timer as timer

start = timer()
# Откройте JSON-файл
with open('shaka_offline_db_exported_data.json', 'r') as f:
    data = json.load(f)

# Предположим, что base64-данные хранятся под ключом 'video_data'
# Поменяйте ключ на тот, который у вас в JSON-файле
base64_data = data['segment-v5']

# Декодируем и записываем в файл
binary_data = base64.b64decode(base64_data)
with open('video_part.mp4', 'wb') as video_file:
    video_file.write(binary_data)

end = timer()
print(f"Время выполнения: {end - start:.5f} секунд")
