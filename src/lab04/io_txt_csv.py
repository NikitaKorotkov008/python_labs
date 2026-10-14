from pathlib import Path
import csv
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Функция читает файл и возвращает его содержимое одной строкой

    По умолчанию стоит кодировка utf-8, чтобы поменять кодировку передайте:
    read_text("data/input.txt", encoding = "cp1251")

    raise:
    FileNotFoundError: Если файл не найден.
    UnicodeDecodeError: Если текст не декодируется
    в указанной кодировке.
    '''
    p = Path(path)
    return p.read_text(encoding=encoding)

print(read_text('data/input.txt', encoding= 'utf-8'))



def write_csv(rows: Iterable[Sequence], path: str | Path,header: tuple[str, ...] | None = None) -> None:
    '''Создать или перезаписать CSV с разделителем-запятой.

    Если передан header, записать его первой строкой.
    При разной длине строк поднять ValueError.
    '''
    p = Path(path)
    rows = list(rows)

    if len(rows) != 0:
        first_len = len(rows[0])
        for i in rows:
            if len(i) != first_len:
                raise ValueError('Все строки должны иметь одинаковую длину')

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)



if __name__ == '__main__':
    print(read_text('data/input.txt', encoding= 'utf-8'))
    print(write_csv([("word","count"),("test",3)], "data/check.csv"))