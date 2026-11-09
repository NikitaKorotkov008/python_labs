import argparse
import csv
import random
import signal
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def stop_measurement(signum, frame):
    raise TimeoutError("Превышен лимит времени")


def measure(fn, limit=None) -> str:
    """Измеряет один запуск и возвращает время строкой для таблицы."""
    if limit is None:
        seconds = timeit.timeit(fn, number=1)
        return f"{seconds:.6f}"

    previous_handler = signal.signal(signal.SIGALRM, stop_measurement)
    try:
        signal.setitimer(signal.ITIMER_REAL, limit)
        seconds = timeit.timeit(fn, number=1)
        return f"{seconds:.6f}"
    except TimeoutError:
        return f"> {limit} с"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)


def bench_sorts(sizes=(1_000, 10_000, 100_000), limit=60):
    """Сравнивает четыре сортировки на одинаковых данных."""
    rows = []
    funcs = [
        ("sorted", sorted),
        ("bubble_sort", bubble_sort),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort),
    ]

    for n in sizes:
        data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]

        for name, fn in funcs:
            print(f"Сортировка: {name}, n={n}...", flush=True)
            if name == "sorted":
                seconds = measure(lambda: fn(data))
            else:
                seconds = measure(lambda: fn(data), limit=limit)

            rows.append(("sorting", n, name, seconds))
            print(f"Готово: {seconds} (секунды)", flush=True)

    return rows


def bench_search(n=100_000, queries=10_000):
    """Время поиска — суммарное для всех запросов."""
    data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
    targets = [random.choice(data) for _ in range(queries)]
    rows = []

    print("Поиск: измеряем подготовительную сортировку...", flush=True)
    seconds = measure(lambda: sorted(data))
    rows.append(("search", n, "sorted_preparation", seconds))
    sorted_data = sorted(data)

    print(f"Линейный поиск: {queries} запросов, n={n}...", flush=True)
    seconds = measure(lambda: [linear_search(data, x) for x in targets])
    rows.append(("search", n, "linear_search", seconds))
    print(f"Готово: {seconds} (секунды)", flush=True)

    print(f"Бинарный поиск: {queries} запросов, n={n}...", flush=True)
    seconds = measure(lambda: [binary_search(sorted_data, x) for x in targets])
    rows.append(("search", n, "binary_search", seconds))
    print(f"Готово: {seconds} (секунды)", flush=True)

    return rows


def bench_two_sum(sizes=(1_000, 10_000)):
    """Сравнивает два способа Two Sum на одинаковых данных."""
    rows = []
    funcs = [("two_sum_brute", two_sum_brute), ("two_sum_fast", two_sum_fast)]

    for n in sizes:
        data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
        a, b = random.sample(data, 2)
        target = a + b

        for name, fn in funcs:
            print(f"Two Sum: {name}, n={n}...", flush=True)
            seconds = measure(lambda: fn(data, target))
            rows.append(("two_sum", n, name, seconds))
            print(f"Готово: {seconds} (секунды)", flush=True)

    return rows


def print_table(rows):
    """Печатает таблицу с рамкой и разделителями между группами замеров."""
    widths = [10, 9, 20, 12]

    def border(left, middle, right):
        return left + middle.join("─" * (width + 2) for width in widths) + right

    labels = {"sorting": "Сортировка", "search": "Поиск", "two_sum": "Two Sum"}
    print("\nРезультаты бенчмарка:")
    print(border("┌", "┬", "┐"))
    print(f"│ {'Задача':<10} │ {'Элементов':>9} │ {'Алгоритм':<20} │ {'Время, с':>12} │")
    print(border("├", "┼", "┤"))

    previous_group = None
    for task, n, impl, seconds in rows:
        group = (task, n)
        if previous_group is not None and group != previous_group:
            print(border("├", "┼", "┤"))
        size = f"{int(n):,}".replace(",", " ")
        label = labels.get(task, task)
        print(f"│ {label:<10} │ {size:>9} │ {impl:<20} │ {seconds:>12} │")
        previous_group = group

    print(border("└", "┴", "┘"))


def main(show_only=False):
    """Запускает замеры или показывает уже сохранённые результаты."""
    path = Path("data/lab07/bench.csv")
    if show_only:
        with path.open(encoding="utf-8", newline="") as file:
            rows = [
                (row["task"], int(row["n"]), row["impl"], row["seconds"])
                for row in csv.DictReader(file)
            ]
    else:
        random.seed(42)
        rows = []
        rows.extend(bench_sorts())
        rows.extend(bench_search())
        rows.extend(bench_two_sum())
        path.parent.mkdir(parents=True, exist_ok=True)
        write_csv(rows, path, header=("task", "n", "impl", "seconds"))
        print(f"\nРезультаты сохранены: {path}")

    print_table(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Бенчмарк алгоритмов ЛР7")
    parser.add_argument("--show", action="store_true", help="Показать CSV без повторных замеров")
    args = parser.parse_args()
    main(show_only=args.show)
