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
parser.add_argument("--in", dest="input_path", default="data/lab04/input.txt")
parser.add_argument("--out", dest="output_path", default="data/lab04/report.csv")
parser.add_argument("--encoding", default="utf-8")
args = parser.parse_args()
try:
    text = read_text(args.input_path, encoding=args.encoding)
except FileNotFoundError:
    print('Файл не найден')
else:
    text_frequencies_from_text = frequencies_from_text(text)
    text_sorted_word_count = sorted_word_counts(text_frequencies_from_text)

    write_csv(text_sorted_word_count, args.output_path, header=('word', 'count'))


    print("Всего слов:", sum(text_frequencies_from_text.values()))
    print("Уникальных слов:", len(text_frequencies_from_text))
    print("Топ-5:")
    for word, count in top_n(text_frequencies_from_text, 5):
        print(f"{word}:{count}")