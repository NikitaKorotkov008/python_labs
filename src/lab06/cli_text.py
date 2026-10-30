import argparse
from pathlib import Path
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n

def cat(path: str, number: bool) -> None:
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError('Файл не найден')
    with file.open(encoding = 'utf-8') as f:
        number_line = 1
        for line in f:
            line = line.strip('\n')
            if number: 
                print(number_line, line)
            else:
                print(line)
            number_line+=1

def stats(path: str, top: int) -> None:
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError('Файл не найден')
    with file.open(encoding = 'utf-8') as f:
        text = f.read()
        freq = count_freq(tokenize(normalize(text)))
        for key, value in top_n(freq, top):
            print(f'{key}: {value}')

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к txt-файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Сколько слов выводить")

    args = parser.parse_args()

    try:
        if args.command == 'cat':
            cat(args.input, args.n)
        elif args.command == 'stats':
            if args.top <=0:
                parser.error("--top должен быть больше 0")
            stats(args.input, args.top)
        else:
            parser.print_help()
    except FileNotFoundError:
        print("Файл не найден")

if __name__ == '__main__':
    main()
