# Lab06 — CLI-утилиты с argparse

## Файлы
- `src/lab06/cli_text.py` — подкоманды `cat` и `stats`
- `src/lab06/cli_convert.py` — подкоманды `json2csv`, `csv2json`, `csv2xlsx`
- `src/lib/text.py` — функции `normalize`, `tokenize`, `count_freq`, `top_n` (используются в `stats`)
- `src/lab05/` — функции конвертации (используются в `cli_convert.py`)
- `data/lab06/samples/` — входные файлы
- `data/lab06/out/` — результаты конвертаций
- `images/lab06/` — скриншоты

---

## Запуск
Все команды запускаются из корня проекта, с активированным `.venv` (для `csv2xlsx` нужен `openpyxl`).

```bash
pip install -r requirements.txt
```


---

## cli_text.py

```bash
python -m src.lab06.cli_text --help
```
![cli_text --help](../../images/lab06/01.png)

### cat — вывести файл построчно
| Параметр | Описание |
|---|---|
| `--input` | путь к файлу (обязательный) |
| `-n` | нумеровать строки |

```bash
python -m src.lab06.cli_text cat --help
python -m src.lab06.cli_text cat --input data/lab06/samples/people.csv -n
```
![cat --help](../../images/lab06/02.png)
![cat -n](../../images/lab06/03.png)

### stats — частоты слов
| Параметр | Описание |
|---|---|
| `--input` | путь к txt-файлу (обязательный) |
| `--top` | сколько слов выводить, по умолчанию 5 |

```bash
python -m src.lab06.cli_text stats --help
python -m src.lab06.cli_text stats --input data/lab06/samples/people.txt --top 5
```
![stats --help](../../images/lab06/04.png)
![stats --top 5](../../images/lab06/05.png)

---

## cli_convert.py

```bash
python -m src.lab06.cli_convert --help
```
![cli_convert --help](../../images/lab06/06.png)

Все три подкоманды принимают одни и те же параметры:

| Параметр | Описание |
|---|---|
| `--in` | входной файл (обязательный) |
| `--out` | выходной файл (обязательный) |

```bash
python -m src.lab06.cli_convert json2csv --in data/lab06/samples/people.json --out data/lab06/out/people.csv
python -m src.lab06.cli_convert csv2json --in data/lab06/samples/people.csv --out data/lab06/out/people.json
python -m src.lab06.cli_convert csv2xlsx --in data/lab06/samples/people.csv --out data/lab06/out/people.xlsx
```

### json2csv
```bash
python -m src.lab06.cli_convert json2csv --help
```
![json2csv --help](../../images/lab06/10.png)

Результат — `data/lab06/out/people.csv`:

![json2csv](../../images/lab06/07.png)

### csv2json
```bash
python -m src.lab06.cli_convert csv2json --help
```
![csv2json --help](../../images/lab06/11.png)

Результат — `data/lab06/out/people.json`:

![csv2json](../../images/lab06/08.png)

### csv2xlsx
```bash
python -m src.lab06.cli_convert csv2xlsx --help
```
![csv2xlsx --help](../../images/lab06/12.png)

Результат — `data/lab06/out/people.xlsx`:

![csv2xlsx](../../images/lab06/09.png)

---

## Ошибки
- Входного файла нет — выводится `Файл не найден`.
- `--top` меньше или равен 0 — `parser.error`: `--top должен быть больше 0`.
- Нет обязательного аргумента или подкоманда неверная — ошибку и подсказку выводит `argparse`.
- Запуск без подкоманды — выводится справка.
