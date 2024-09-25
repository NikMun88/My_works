import pandas as pd


def txt_to_csv(txt_file, csv_file, delimiter=','):
    # Читаем .txt файл с указанным разделителем
    df = pd.read_csv(txt_file, delimiter=delimiter)

    # Сохраняем в .csv файл
    df.to_csv(csv_file, index=False)
    print(f'Файл {txt_file} успешно преобразован в {csv_file}')


# Пример использования
txt_to_csv('data.txt', 'data.csv', delimiter=',')  # Замените ',' на '\t', если разделитель табуляция
