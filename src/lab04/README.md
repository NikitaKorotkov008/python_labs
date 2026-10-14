# Lab04-Файлы: TXT/CSV и отчёты по текстовой статистике
---
### io_txt_csv.py
```python
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

```

Файл читается целиком в память. Для очень больших файлов лучше
использовать построчное чтение.

Пустой текстовый файл возвращает пустую строку.
При пустом rows без header создаётся пустой CSV,
а с header — CSV только с заголовком.

Для другой кодировки нужно передать параметр encoding,
например: read_text("data/input.txt", encoding="cp1251").
---
### text_report.py
```python
from src.lab03.text import top_n
from src.lab04.io_txt_csv import read_text, write_csv
from collections import Counter
from src.lib.text import normalize, tokenize  # из ЛР3
import argparse

def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens) 

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

parser = argparse.ArgumentParser()
parser.add_argument("--in", dest="input_path", default="data/input.txt")
parser.add_argument("--encoding", default="utf-8")
args = parser.parse_args()

text = read_text(args.input_path, encoding=args.encoding)

text_frequencies_from_text = frequencies_from_text(text)
text_sorted_word_count = sorted_word_counts(text_frequencies_from_text)

write_csv(text_sorted_word_count, "data/report.csv",header=('word', 'count'))


if __name__ == '__main__':
    print("Всего слов:", sum(text_frequencies_from_text.values()))
    print("Уникальных слов:", len(text_frequencies_from_text))
    print("Топ-5:", top_n(text_frequencies_from_text, 5))
```
Запуск из корня проекта:
python -m src.lab04.text_report

Если входной файл отсутствует, программа завершается
с ошибкой FileNotFoundError.

При пустом входном файле report.csv содержит только
заголовок word,count.

По умолчанию читается data/input.txt в UTF-8.
Другой файл задаётся через --in, кодировка — через --encoding.
Отчёт сохраняется в data/report.csv.

--- 
### Test cases
# A
Terminal
![ExA](../../images/lab04/01.png)
CSV

![ExA](../../images/lab04/02.png)
---
# B
Terminal
![ExB](../../images/lab04/03.png)
CSV

![ExA](../../images/lab04/04.png)
---
# C
Terminal
![ExA](../../images/lab04/05.png)
CSV

![ExA](../../images/lab04/06.png)

Запускать:
```python
python -m src.lab04.text_report --in data/input.txt --encoding cp1251
```
---

