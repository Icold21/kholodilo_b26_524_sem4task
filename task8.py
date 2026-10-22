def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError:
        print(f"Ошибка: файл не найден - {path}")

    except PermissionError:
        print(f"Ошибка: нет прав доступа к файлу - {path}")

    except IsADirectoryError:
        print(f"Ошибка: путь указывает на директорию, а не на файл - {path}")

    except NotADirectoryError:
        print(f"Ошибка: некорректный путь, часть пути не является директорией - {path}")

    except UnicodeDecodeError as e:
        print(f"Ошибка: не удалось прочитать файл как текст (проблема кодировки) - {path}. Детали: {e}")

    except OSError as e:
        print(f"Ошибка операционной системы при чтении файла - {path}. Детали: {e}")

    return None

if __name__ == '__main__':
    path: str = ""
    
    print()