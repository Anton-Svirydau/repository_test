import json
import base64
import os

def explore_json(data, parent_key=''):
    """
    Рекурсивный анализ JSON для выявления строк, которые могут быть base64.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            explore_json(value, f"{parent_key}.{key}" if parent_key else key)
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            explore_json(item, f"{parent_key}[{idx}]")
    elif isinstance(data, str):
        if is_potential_base64(data):
            save_base64_data(data, parent_key)
    else:
        pass


def is_potential_base64(string):
    """
    Проверка, может ли строка быть base64.
    """
    try:
        if len(string) > 50:  # Минимальная длина строки base64
            base64.b64decode(string, validate=True)
            return True
    except Exception as e:
        pass
    return False


def save_base64_data(data, path):
    """
    Декодирует и сохраняет base64-данные.
    """
    try:
        binary_data = base64.b64decode(data)
        sanitized_path = path.replace("[", "_").replace("]", "_").replace(".", "_")
        output_dir = "extracted_files"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{sanitized_path}.bin")
        with open(output_file, 'wb') as f:
            f.write(binary_data)
        print(f"Сохранено: {output_file}")
    except Exception as e:
        print(f"Ошибка при сохранении данных по пути {path}: {e}")


# Загрузка JSON-файла
input_file = 'shaka_offline_db_exported_data.json'
with open(input_file, 'r') as f:
    json_data = json.load(f)

# Запуск анализа
explore_json(json_data)
