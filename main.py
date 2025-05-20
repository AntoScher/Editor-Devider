import os


def process_and_split_file(input_filename, output_prefix, max_length=3999):
    # Получаем текущую директорию проекта
    current_dir = os.getcwd()
    input_path = os.path.join(current_dir, input_filename)

    # Проверяем, существует ли файл
    if not os.path.isfile(input_path):
        print(f"Файл {input_filename} не найден в директории {current_dir}.")
        return

    # Читаем файл
    with open(input_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Удаляем пустые строки
    lines = text.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    cleaned_text = ' '.join(non_empty_lines)

    # Разбиваем текст на части
    parts = [cleaned_text[i:i + max_length] for i in range(0, len(cleaned_text), max_length)]

    # Сохраняем части в новые файлы
    for index, part in enumerate(parts, start=1):
        output_filename = f"{output_prefix}_{index}.txt"
        output_path = os.path.join(current_dir, output_filename)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(part)
        print(f"Сохранен файл: {output_filename}")

    print("Обработка завершена.")


# Пример использования
input_filename = 'input.txt'  # Имя исходного файла
output_prefix = 'output_part'  # Префикс для имен выходных файлов

process_and_split_file(input_filename, output_prefix)