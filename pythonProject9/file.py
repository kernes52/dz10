
def open_file():
    while True:
        filename = input("Введіть назву файла: ")

        mode = input("Оберіть режим відкриття файлу ('t' - текстовий, 'b' - двоічний)")

        if mode == 't':
            open_mode = 'r'
        elif mode == 'b':
            open_mode = 'rb'
        else:
            print("Невірний режим! Введіть 't' фбо 'b'.")
            continue

        try:
            with open(filename, open_mode) as file:
                if open_mode == 'r':
                    lines = file.readlines()
                    print(f"Файл '{filename}' відкрито. Кількість строк: {len(lines)}")
                else:
                    file_data = file.read()
                    print(f"Файл '{filename}' відкрито в двоічному режимі.")
            break
        except FileNotFoundError:
            print(f"Помилка: Файл'{filename}' не існує. Спробуйте ще раз.")
        except Exception as e:
            print(f"Помилка: Файл '{filename}' не може бути прочитаним ({e}).")
            break

if __name__ == "__main__":
    open_file()